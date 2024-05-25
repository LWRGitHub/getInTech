from flask import Flask, request, redirect, render_template, url_for
from flask_talisman import Talisman
import os
import time
# forms
from web_forms import SearchForm
# Data
from data.Solutions import Solutions
from data.Solutions_info import Solutions_info
from data.Swe_career_guide import Swe_career_guide 
from data.Markdown_to_json import Markdown_to_json
import pprint
import math
import re
import json

# Markdown 
from jinjaMarkdown.markdownExtension import markdownExtension
# from mistune import html
# import argparse
# import sys

# import jinja2
# import markdown




############################################################
# SETUP
############################################################


app = Flask(__name__)

# Secret Key for CSRF Protection in Flask-WTF
SECRET_KEY = os.urandom(32)
app.config['SECRET_KEY'] = SECRET_KEY

#add markdownExtension to enviroment (by default jinja_env)
app.jinja_env.add_extension(markdownExtension)

# Jija2 custom filters
def is_list(value):
    return isinstance(value, list)

def is_str(value):
    return isinstance(value, str)

app.jinja_env.filters['is_list'] = is_list
app.jinja_env.filters['is_str'] = is_str

############################################################
# DATA
############################################################


solutions = Solutions().solutions
solutions_info = Solutions_info().solutions_info


############################################################
# ROUTES
############################################################


# Home pg
@app.route('/')
def home():
    """Display the home page."""

    context = {}

    return render_template('pages/home.html', **context)


# Carreer Guide pg
@app.route('/swe_career_guide/<step>/<step_sections>')
def swe_career_guide(step, step_sections):
    """Display the swe_career_guide page."""

    step_num_idx = 0
    step_letter_idx = 0
    context = {}

    for idx1, step_data in enumerate(Swe_career_guide().swe_career_guide):
        
        if step_data["title"].replace(" ", "_") == step:

            step_num_idx = idx1
            for idx2, page in enumerate(step_data["pages"]):

                if page["title"].replace(" ", "_") == step_sections:

                    step_letter_idx = idx2
                    context = page
                    break
            break

    # set Breadcrumb variables
    context['step'] = step
    context['step_sections'] = step_sections
    context['step_display'] = step.replace('_', ' ')
    context['step_sections_display'] = step_sections.replace('_', ' ')

    # assign next page 
    if step_letter_idx+1 < len(Swe_career_guide().swe_career_guide[step_num_idx]['pages']):

        context['next_page'] = f"{Swe_career_guide().swe_career_guide[step_num_idx]['title'].replace(' ', '_')}/{Swe_career_guide().swe_career_guide[step_num_idx]['pages'][step_letter_idx+1]['title'].replace(' ', '_')}"
    else:
        if step_num_idx+1 < len(Swe_career_guide().swe_career_guide):
            context['next_page'] = f"{Swe_career_guide().swe_career_guide[step_num_idx+1]['title'].replace(' ', '_')}/{Swe_career_guide().swe_career_guide[step_num_idx+1]['pages'][0]['title'].replace(' ', '_')}"
        else:
            context['next_page'] = False
    
    # assign prev page
    if step_letter_idx-1 > -1:
        context['prev_page'] = f"{Swe_career_guide().swe_career_guide[step_num_idx]['title'].replace(' ', '_')}/{Swe_career_guide().swe_career_guide[step_num_idx]['pages'][step_letter_idx-1]['title'].replace(' ', '_')}"
    else:
        if step_num_idx-1 > -1:
            context['prev_page'] = f"{Swe_career_guide().swe_career_guide[step_num_idx-1]['title'].replace(' ', '_')}/{Swe_career_guide().swe_career_guide[step_num_idx-1]['pages'][-1]['title'].replace(' ', '_')}"
        else:
            context['prev_page'] = False



    return render_template('pages/career_guide/guide.html', **context)


# 404 pg
@app.errorhandler(404)
def page_not_found(e):
    return render_template('pages/404.html'), 404


# Code Solutions pg
@app.route('/code_solution/<solution_id>')
def code_solution(solution_id):
    """Display the Code Solution page."""

    context = {}

    for product in solutions_info:
        if product["_id"] == solution_id:
            context = product
            if not "search_res" in product:
                context["search_res"] = False
            break
    
    # def markdown_to_json(context):
    #     print("here")
    #     how_to = []

    #     # split contest["markdown_how_to_solve"] at \n to get the list of lines
    #     markdown_list = [line for line in context["markdown_how_to_solve"].split("\n") if line.strip() != ""]

    #     # find all pairs🍐 of a * | ** | *** in a string
    #     def find(s):
    #         patterns = {
    #             3: r'\*\*\*[^*]+\*\*\*',
    #             2: r'\*\*[^*]+\*\*',
    #             1: r'\*[^*]+\*'
    #         }
            
    #         result = []
    #         i = 0
    #         while i < len(s):
    #             match = None
    #             for type_, pattern in patterns.items():
    #                 regex = re.compile(pattern)
    #                 current_match = regex.match(s, i)
    #                 if current_match:
    #                     match = {'type': type_, 'idxs': [current_match.start(), current_match.end() - 1]}
    #                     break
                
    #             if match:
    #                 result.append(match)
    #                 i = match['idxs'][1] + 1
    #             else:
    #                 i += 1
            
    #         return result
    
    #     # find all pairs🍐 of ` in a string
    #     def find_back_ticks(s):
    #         patterns = {
    #             1: r'`[^`]+`'
    #         }
            
    #         result = []
    #         i = 0
    #         while i < len(s):
    #             match = None
    #             for type_, pattern in patterns.items():
    #                 regex = re.compile(pattern)
    #                 current_match = regex.match(s, i)
    #                 if current_match:
    #                     match = {'type': type_, 'idxs': [current_match.start(), current_match.end() - 1]}
    #                     break
                
    #             if match:
    #                 result.append(match)
    #                 i = match['idxs'][1] + 1
    #             else:
    #                 i += 1
            
    #         return result

    #     # check if line starts with >
    #     # if so get indent
    #     def bd_callout(markdown_list, idx):
    #         html_data = {}

    #         if markdown_list[idx][0:1] == '>':
    #             html_data["bd_callout"] = {}

    #             if markdown_list[idx][0:2] == '>>':
    #                 if markdown_list[idx][0:3] == '>>>':
    #                     html_data["bd_callout"]["indent"] = 3
    #                 else:
    #                     html_data["bd_callout"]["indent"] = 2
    #             else:
    #                 html_data["bd_callout"]["indent"] = 1

    #         # remove all > from the front of the line
    #         markdown_list[idx] = markdown_list[idx].lstrip('>')

    #         return html_data
    #     prior_line_has_callout = False

    #     # check if prior_line_has_callout & "bd_callout" in html_data add to last dict in how_to
    #     def if_need_add_callout_line(prior_line_has_callout, how_to, html_data):
    #         if prior_line_has_callout and "bd_callout" in html_data:
                    
    #             # check if str, list or dict
    #             if type(how_to[-1]["content"]) == list:
    #                 how_to[idx-1]["content"].append([*how_to[idx-1]["content"], html_data])
    #             else: # type(how_to[-1]["content"]) == str or type(how_to[-1]["content"]) == dict
    #                 how_to[idx-1]["content"].append([how_to[idx-1]["content"], html_data])

    #     # order data acording to Md `
    #     def sort_buld_sm_code_block(data, ch_idxs):
    #         code_data = {}
            
    #         code_data["tag"] = "span"
    #         code_data["content"] = []

    #         if ch_idxs[0]["idxs"][0] != 0:
    #             content = data[0:ch_idxs[0]["idxs"][0]]
    #             code_data["content"].append({
    #                 "tag": "span",
    #                 "content": content
    #             })

    #         # loop through ch_idxs
    #         last_i2 = None
    #         for code_info in ch_idxs:
    #             [i1, i2] = code_info["idxs"]

    #             # if last_i2 is not None add the text between the last_i2 and i1 to the list
    #             if last_i2 != None:
    #                 content = data[last_i2:i1]
    #                 code_data["content"].append({
    #                     "tag": "span",
    #                     "content": content
    #                 })

    #             content = data[i1+1:i2]
    #             code_data["content"].append({
    #                 "tag": "code",
    #                 "content": content
    #             })

    #             last_i2 = i2 + 1


    #         # if last the last list in ch_idxs at index 1 is not the last index of text add the text between the last_i2 and the end of the text to the list
    #         if last_i2 != None and last_i2 < len(data):
    #             content = data[last_i2:]
    #             code_data["content"].append({
    #                 "tag": "span",
    #                 "content": content
    #             })
            
    #         return code_data

    #     # order data acording to Md * | ** | ***
    #     # **Trie Initialization (`__init__` method)**
    #     # Trie **Initialization** (`__init__` method)
    #     def sort_buld_italic(text, ch_idxs):
    #         astrict_data = {}

    #         astrict_data["tag"] = "span"
    #         astrict_data["content"] = []

    #         def has_backticks(content):
    #             # if even instances of ` 
    #             if content.find('`') != -1 and content.count("`") % 2 == 0:
    #                 ch_idxs = find_back_ticks(content)
    #                 content = sort_buld_sm_code_block(content, ch_idxs)
    #             return content

            
    #         if ch_idxs[0]["idxs"][0] != 0:
    #             content = text[0:ch_idxs[0]["idxs"][0]]

    #             # if even instances of ` 
    #             content = has_backticks(content)

    #             astrict_data["content"].append({
    #                 "tag": "span",
    #                 "content": content
    #             })
    #         #     astrict_data["tag"] = "span"
    #         # elif text[0] == "***":

    #         # loop through ch_idxs
    #         last_i2 = None
    #         for astrict_info in ch_idxs:
    #             [i1, i2] = astrict_info["idxs"]
    #             astrid_count = astrict_info["type"]

    #             # if last_i2 is not None add the text between the last_i2 and i1 to the list 
    #             if last_i2 != None:
    #                 content = text[last_i2:i1]

    #                 # if even instances of ` 
    #                 content = has_backticks(content)

    #                 astrict_data["content"].append({
    #                     "tag": "span",
    #                     "content": content
    #                 })
                    
    #             if astrid_count == 3:
    #                 content = text[i1+3:i2-2]

    #                 # if even instances of ` 
    #                 content = has_backticks(content)

    #                 # add the text between i1 and i2 to the list as a bold tag
    #                 astrict_data["content"].append({
    #                     "tag": "strong",
    #                     "content": {
    #                         "tag": "em",
    #                         "content": content,
    #                     }
    #                 })
    #             else:
    #                 content = text[i1+astrid_count:i2-astrid_count+1]

    #                 # if even instances of ` 
    #                 content = has_backticks(content)

    #                 # add the text between i1 and i2 to the list as a bold tag
    #                 # astrict_data["tag"] = "strong" if astrid_count == 2 else "em"
    #                 astrict_data["content"].append({
    #                     "tag": "strong" if astrid_count == 2 else "em",
    #                     "content": content
    #                 })

                
                    
    #             last_i2 = i2 + 1  
            
    #         # if last the last list in ch_idxs at index 1 is not the last index of text add the text between the last_i2 and the end of the text to the list
    #         if last_i2 != None and last_i2 < len(text):
    #             content = text[last_i2:]

    #             # if even instances of ` 
    #             content = has_backticks(content)

    #             astrict_data["content"].append({
    #                 "tag": "span",
    #                 "content": content
    #             })

    #         return astrict_data
        
    #     # make html list data >>> ol | ul
    #     def make_html_list_data(html_data, markdown_list, idx, prior_line_has_callout, how_to, depth):
            
    #         li_data = {}
    #         li_data["tag"] = "ol" if markdown_list[idx].lstrip()[0].isnumeric() else "ul"
    #         li_data["content"] = []

    #         # use to keep track of the parent type (e.g. ol | ul) incase of children so onece the children are done we can continue with the sibling node of the parent
    #         main_old_idx = idx 
    #         is_ol_main = "ol" if li_data["tag"] == "ol" else "ul" 
            
    #         # while not empty line and starts with number immediately followed by '.' or starts with space(s) then number immediately followed by '.'
    #         def make_li_tags(idx, markdown_list, depth, li_data):

    #             # while current is <li> 
    #             while (idx < len(markdown_list) and len(markdown_list[idx]) > 0 and markdown_list[idx] != '') and (markdown_list[idx].lstrip()[0] == '-' or (markdown_list[idx].lstrip()[0].isnumeric() and markdown_list[idx].lstrip()[1] == '.') or (markdown_list[idx].lstrip()[0:2].isnumeric() and markdown_list[idx].lstrip()[2] == '.')):
                    
    #                 spaces = len(markdown_list[idx]) - len(markdown_list[idx].lstrip())

    #                 # if line spaces in front of the number make sub list
    #                 if spaces > depth:

    #                     content_res, idx = make_html_list_data(html_data, markdown_list, idx, prior_line_has_callout, how_to, spaces)
    #                     li_data["content"].append(content_res)
    #                     idx += 1
                        
    #                     continue

    #                 elif spaces < depth:
    #                     return [idx, li_data]
                    
    #                 # remove the number and the '.' or the '-' and the spaces
    #                 rm_count = 2 if markdown_list[idx].lstrip()[0] == '-' else 3 

    #                 data = markdown_list[idx].lstrip()[rm_count:]

    #                 # check if even instances of ** are present in the line
    #                 if data.find('*') != -1 and data.count("*") % 2 == 0:
    #                     ch_idxs = find(data)
    #                     data = sort_buld_italic(data, ch_idxs)
    #                 elif data.find('`') != -1 and data.count("`") % 2 == 0:
    #                     ch_idxs = find_back_ticks(data)
    #                     data = sort_buld_sm_code_block(data, ch_idxs)
                        
    #                 # make {tag: li, content: data}
    #                 li_data["content"].append({
    #                     "tag": "li",
    #                     "content": data,
    #                 })

    #                 idx += 1
                
    #             return [idx, li_data]

    #         idx, li_data = make_li_tags(idx, markdown_list, depth, li_data)


    #         # if prior_line_has_callout & "bd_callout" in html_data add to last dict in how_to
    #         # if_need_add_callout_line(prior_line_has_callout, how_to, html_data)
    #         # def is_ol_sibling(idx, markdown_list):
    #         #     return True if idx < len(markdown_list) and len(markdown_list[idx]) != 0 and markdown_list[idx].lstrip()[0].isnumeric() else False

    #         # # is_ol_sibling = markdown_list[idx].lstrip()[0].isnumeric()

    #         # siblying_l_type = "ol" if markdown_list[idx].lstrip()[0].isnumeric() else "ul" if markdown_list[idx].lstrip()[0] == "-" else False

    #         # while idx < len(markdown_list) and is_ol_main == ("ol" if markdown_list[idx].lstrip()[0].isnumeric() else "ul" if markdown_list[idx].lstrip()[0] == "-" else False):
            
    #         #     idx, li_data = make_li_tags(idx, markdown_list, depth, li_data)

    #         return [li_data, idx-1]

    #     idx = 0  
    #     # loop through markdown_list
    #     while idx < len(markdown_list):
            
    #         """
    #             html_data = {
    #                 # key: Str | List | Dict

    #                 # Optional ⌥
    #                 "bd_callout": {"indent": Int},

    #                 # Required❗️
    #                 "tag": Str,
    #                 # Str >>> "tag": "h2" | "h4" | "h5" | "p" | "fenced_code_block" | "code" | "strong" | "ul" | "ol" | "li" | "span" | "hr" | "em" 
    #                 # TODO: add to Str >>> "a" | "img" | "iframe" | "table" | "tr" | "th" | "td" | "pre" | "b" | "div" | "br" | 

    #                 # Required❗️ unless otherwise specified 
    #                 # ∞ Infinite Possible nested tags 🆘 
    #                 "content": Str | List | Dict
    #                 # "Content_Str" >>> "content": "text to display",
    #                 ''' [Content_List] >>> 
    #                 "content": [
    #                     # Str | [Content_List] | {Content_Dict} 
    #                     "text to display",
    #                     [ [Content_List] ],
    #                     {Content_Dict}
    #                 ],'''
    #                 ''' {Content_Dict} >>> 
    #                 "content": {
    #                     "tag": Str, 
    #                     "content": Str | [Content_List] | {Content_Dict},
    #                     "bd_callout": {"indent": Int} # Optional ⌥
    #                 },'''
    #             }
    #         """
            
    #         html_data = {}  

    #         # check if line starts with >
    #         html_data = bd_callout(markdown_list, idx)

    #         # check if code block e.g. ``` 
    #         if markdown_list[idx].find("```") != -1:
    #             # loop through the list until the next ``` is found
    #             idx += 1
    #             # make {tag: code, content: code}
    #             html_data["tag"] = "fenced_code_block"
    #             html_data["content"] = '\n'

    #             # loop through code_lines and add each line to the content keep indentations "space(s)" the same
    #             while idx < len(markdown_list) and markdown_list[idx].find("```") == -1:
    #                 html_data["content"] += f"{markdown_list[idx]}\n"
    #                 idx += 1

    #             # if prior_line_has_callout & "bd_callout" in html_data add to last dict in how_to
    #             if_need_add_callout_line(prior_line_has_callout, how_to, html_data)
                
    #         # check if line starts with # | ## | ### followed by a space
    #         elif markdown_list[idx][0] == "#":
    #             symbol_count = 1
    #             if markdown_list[idx][0:2] == "##":
    #                 if markdown_list[idx][0:3] == "###":

    #                     symbol_count = 3
    #                     html_data["tag"] = "h5"
    #                 else:
    #                     symbol_count = 2
    #                     html_data["tag"] = "h4"
    #             else:
    #                 html_data["tag"] = "h2"
                
    #             html_data["content"] = f"{markdown_list[idx][symbol_count+1:]}"

    #         # if --- create hr tag & continue
    #         elif markdown_list[idx][0:3] == "---":
    #             html_data["tag"] = "hr"
    #             html_data["content"] = ""

    #         # ? Starts w/ (num >>> '.' | '-')  | space(s) >>> ( "-" | num >>> '.' )  
    #         elif markdown_list[idx].lstrip()[0].isnumeric() and markdown_list[idx].lstrip()[1] == '.' or markdown_list[idx].lstrip()[0] == '-':

    #             # get indent info
    #             depth = len(markdown_list[idx]) - len(markdown_list[idx].lstrip())
                
    #             # make html list data
    #             li_data, idx = make_html_list_data(html_data, markdown_list, idx, prior_line_has_callout, how_to, depth)


    #             html_data["tag"] = li_data["tag"]
    #             html_data["content"] = li_data["content"]

    #         # check if even instances of ** are present in the line
    #         elif markdown_list[idx].find('*') != -1 and markdown_list[idx].count("*") % 2 == 0:

    #             ch_idxs = find(markdown_list[idx])
                
    #             # order data acording to Md * | ** | ***
    #             res = sort_buld_italic(markdown_list[idx], ch_idxs)

    #             html_data["tag"] = res["tag"]
    #             html_data["content"] = res["content"]
            
    #         # if even instances of ` are present in the line
    #         elif markdown_list[idx].find('`') != -1 and markdown_list[idx].count("`") % 2 == 0:
    #             ch_idxs = find_back_ticks(markdown_list[idx])

    #             # order data acording to Md `
    #             data_res = sort_buld_sm_code_block(markdown_list[idx], ch_idxs)

    #             if data_res["tag"] == "span":
    #                 html_data["tag"] = "p"
    #             else:
    #                 html_data["tag"] = data_res["tag"]

    #             html_data["content"] = data_res["content"]
                
            
    #         else:
    #             html_data["tag"] = "p"
    #             html_data["content"] = markdown_list[idx]


    #         # if prior_line_has_callout & "bd_callout" in html_data add to last dict in how_to
    #         if_need_add_callout_line(prior_line_has_callout, how_to, html_data)
    #         # if html_data["bd_callout"] prior_line_has_callout = True
    #         if "bd_callout" in html_data: 
    #             prior_line_has_callout = True
    #         else:
    #             prior_line_has_callout = False

    #         how_to.append(html_data)
    #         idx += 1

    #     context["how_to"] = how_to

    #     print(how_to)

    #     return how_to


    # print("markdown_how_to_solve" in context)
    if "markdown_how_to_solve" in context:
        context["how_to"] = Markdown_to_json().markdown_to_json(context)

    # loop through coding solution & 
    # if coding solution block doesn't start with \n add it
    for solution in context["languages"]:
        # check if solution["code"] starts with \n
        if solution["code"][:1] != '\n':
            solution["code"] = '\n' + solution["code"]

    return render_template('pages/code_solutions/code_solution.html', **context)

# About pg
@app.route('/about')
def about():
    """Display the About page."""

    return render_template('pages/about.html')

@app.route('/cookie_policies')
def cookie_policies():
    """Display the cookie_policies page."""

    return render_template('pages/privacy/cookie_policies.html')

@app.route('/privacy_policy')
def privacy_policy():
    """Display the privacy_policy page."""

    return render_template('pages/privacy/privacy_policy.html')

@app.route('/sitemap.xml')
def sitemap_xml():
    """Display the sitemap page."""

    return render_template('pages/sitemap.xml')    

@app.route('/test')
def test():
    """Display the test page."""
   

    context = {
        "name": "Test",
        "site": "LeetCode",
        "_id": "LeetCode-test",
        "href": "/solution/LeetCode-test",
        "video": {
            "has_video": True,
            "scripts": ["https://www.youtube.com/embed/qmntcyBt-5s?si=nUJQ3Unrd6RDdKzG"]
        },
        "how_to": False,
        "markdown_how_to_solve": "To solve this `coding` challenge, we first need to understand the structure and functioning of a Trie (Prefix Tree). A Trie is a tree-like data structure that stores strings in a way that allows for efficient retrieval of words, especially when dealing with operations like prefix searches.\n\n# Explanation\n\n1. Trie **Initialization** (`__init__` method):\n   - We initialize our Trie with an empty dictionary `root` which will act as the root node of the Trie.\n\n2. Insert a **Word into the Trie** (insert method):\n   - We start at the root of the Trie.\n   - For each character in the word, if the character is not already present as a child of the current node, we create a new dictionary for that character.\n   - We then move to the next level (child node) and repeat until all characters are inserted.\n   - After inserting all characters of the word, we mark the end of the word by adding a special symbol `$` with a value of `True`.\n\n3. **Search for a Word in the Trie (`search` method)**:\n   - We start at the root and traverse through each character of the word.\n   - For each character, if the character is not found in the current node, the word does not exist in the Trie and we return `False`.\n   - If we successfully traverse through all characters, we then check for the special end-of-word symbol `$` to confirm the presence of the complete word.\n\n4. **Check for a Prefix in the Trie (`startsWith` method)**:\n   - Similar to the search method, we start at the root and traverse through each character of the prefix.\n   - If any character in the prefix is not found in the current node, the prefix does not exist in the Trie and we return `False`.\n   - If we successfully traverse through all characters, we return `True` since the prefix exists in the Trie.\n\n# Pseudocode\n\n```pseudo\nclass Trie:\n    # Initialize the Trie with an empty dictionary as root\n    method __init__():\n        root = {}\n\n    # Insert a word into the Trie\n    method insert(word):\n        node = root\n        for each char in word:\n            if char not in node:\n                node[char] = {}\n            node = node[char]\n        node['$'] = True  # Mark the end of the word\n\n    # Search for a word in the Trie\n    method search(word) -> boolean:\n        node = root\n        for each char in word:\n            if char not in node:\n                return False\n            node = node[char]\n        return '$' in node  # Return True if the end of word marker is found\n\n    # Check if there is any word in the Trie that starts with the given prefix\n    method startsWith(prefix) -> boolean:\n        node = root\n        for each char in prefix:\n            if char not in node:\n                return False\n            node = node[char]\n        return True  # All characters in prefix are found, so return True\n```\n\nThis pseudocode covers the initialization, insertion of words, searching for words, and checking for prefixes in a Trie data structure. This is the methodology for solving the coding challenge.",
        "languages": [
            {
                "name": "Python",
                "abbreviation_for_prism_styles": "py",
                "code": '''
def threeSum(nums):

    nums.sort()
    res = []

    for i in range(len(nums)):

        if nums[i] > 0:
            break
        elif i == 0 or nums[i-1] != nums[i]:
            sum0(nums, i, res)

    return res

def sum0(nums, i, res):

    sm = i + 1
    lg = len(nums) - 1

    while sm < lg:
        sum = nums[i] + nums[sm] + nums[lg]

        if sum < 0:
            sm+= 1
        elif sum > 0:
            lg-= 1
        else:
            res.append([nums[i], nums[sm], nums[lg]])
            sm+= 1
            lg-= 1
            while(sm < len(nums) and nums[sm] == nums[sm-1]):
                sm+= 1'''
            },
            {
                "name": "JavaScript",
                "abbreviation_for_prism_styles": "js",
                "code": '''
const threeSum = function(nums, res=[]) {
    nums.sort((a,b) => a - b);
    for(let i = 0; i < nums.length; i++){
        if(nums[i] > 0){
            break;
        } else if(i === 0 || nums[i-1] !== nums[i]){
            sum0(nums, i, res);
        }
    }
    return res;
};

const sum0 = (nums, i, res, sm=i+1, lg=nums.length-1) => {
    while(sm < lg){
        const sum = nums[i] + nums[sm] + nums[lg];
        if(sum < 0){
            sm++;
        } else if(sum > 0) {
            lg--;
        } else {
            res.push([nums[i], nums[sm], nums[lg]]);
            sm++;
            lg--;
            while(nums[sm] === nums[sm-1]){
                sm++;
            }
        }
    }
};'''
            }
        ],
        "search_res": {
            "video": {
                "has_video": True,
                "src": [
                    "https://www.youtube.com/embed/jzZsG8n2R9A?si=uwDfaIS98YU3Xb0T",
                    "https://www.youtube.com/embed/cRBSOz49fQk?si=jTOTlZh0rFbZnmPF",
                    "https://www.youtube.com/embed/qJSPYnS35SE?si=uLOE-LePO8NRJa8Q"
                ]
            },
            "languages": [
                {
                    "name": "Python",
                    "solutions": [
                        {
                            "site_name": "Coding Broz",
                            "href": "https://www.codingbroz.com/3sum-leetcode-solution/"
                        },
                        {
                            "site_name": "Medium @Norman Aranez",
                            "href": "https://medium.com/@araneznorman/15-3sum-leetcode-31ab6df7969e"
                        }
                    ],
                },
                {
                    "name": "JavaScript",
                    "solutions": [
                        {
                            "site_name": "Medium @Norman Aranez",
                            "href": "https://medium.com/@araneznorman/15-3sum-leetcode-31ab6df7969e"
                        }
                    ],
                },
                {
                    "name": "TypeScript",
                    "solutions": [
                        {
                            "site_name": "Medium @Norman Aranez",
                            "href": "https://medium.com/@araneznorman/15-3sum-leetcode-31ab6df7969e"
                        }
                    ],
                },
                {
                    "name": "PHP",
                    "solutions": [
                        {
                            "site_name": "Medium @Norman Aranez",
                            "href": "https://medium.com/@araneznorman/15-3sum-leetcode-31ab6df7969e"
                        }
                    ],
                },
                {
                    "name": "C-Sharp",
                    "solutions": [
                        {
                            "site_name": "Medium @Norman Aranez",
                            "href": "https://medium.com/@araneznorman/15-3sum-leetcode-31ab6df7969e"
                        }
                    ],
                },
                {
                    "name": "C-Plus-Plus",
                    "solutions": [
                        {
                            "site_name": "Coding Broz",
                            "href": "https://www.codingbroz.com/3sum-leetcode-solution/"
                        },
                        {
                            "site_name": "Tutorial Cup",
                            "href": "https://tutorialcup.com/leetcode-solutions/3sum-leetcode-solution.htm"
                        }
                    ],
                },
                {
                    "name": "Java",
                    "solutions": [
                        {
                            "site_name": "Coding Broz",
                            "href": "https://www.codingbroz.com/3sum-leetcode-solution/"
                        },
                        {
                            "site_name": "Tutorial Cup",
                            "href": "https://tutorialcup.com/leetcode-solutions/3sum-leetcode-solution.htm"
                        },
                        {
                            "site_name": "Medium @Norman Aranez",
                            "href": "https://medium.com/@araneznorman/15-3sum-leetcode-31ab6df7969e"
                        }
                    ],
                }
            ]
        },
    }
    
    how_to = []

    # split contest["markdown_how_to_solve"] at \n to get the list of lines
    markdown_list = [line for line in context["markdown_how_to_solve"].split("\n") if line.strip() != ""]

    # markdown_list = context["markdown_how_to_solve"].split("\n")

    f = open('markdown_list.json', 'w', encoding="utf-8")
    json.dump(markdown_list, f, indent=4)
    f.close() 

    # find all pairs🍐 of a * | ** | *** in a string
    def find(s):
        patterns = {
            3: r'\*\*\*[^*]+\*\*\*',
            2: r'\*\*[^*]+\*\*',
            1: r'\*[^*]+\*'
        }
        
        result = []
        i = 0
        while i < len(s):
            match = None
            for type_, pattern in patterns.items():
                regex = re.compile(pattern)
                current_match = regex.match(s, i)
                if current_match:
                    match = {'type': type_, 'idxs': [current_match.start(), current_match.end() - 1]}
                    break
            
            if match:
                result.append(match)
                i = match['idxs'][1] + 1
            else:
                i += 1
        
        return result
  
    # find all pairs🍐 of ` in a string
    def find_back_ticks(s):
        patterns = {
            1: r'`[^`]+`'
        }
        
        result = []
        i = 0
        while i < len(s):
            match = None
            for type_, pattern in patterns.items():
                regex = re.compile(pattern)
                current_match = regex.match(s, i)
                if current_match:
                    match = {'type': type_, 'idxs': [current_match.start(), current_match.end() - 1]}
                    break
            
            if match:
                result.append(match)
                i = match['idxs'][1] + 1
            else:
                i += 1
        
        return result

    # check if line starts with >
    # if so get indent
    def bd_callout(markdown_list, idx):
        html_data = {}

        if markdown_list[idx][0:1] == '>':
            html_data["bd_callout"] = {}

            if markdown_list[idx][0:2] == '>>':
                if markdown_list[idx][0:3] == '>>>':
                    html_data["bd_callout"]["indent"] = 3
                else:
                    html_data["bd_callout"]["indent"] = 2
            else:
                html_data["bd_callout"]["indent"] = 1

        # remove all > from the front of the line
        markdown_list[idx] = markdown_list[idx].lstrip('>')

        return html_data
    prior_line_has_callout = False

    # check if prior_line_has_callout & "bd_callout" in html_data add to last dict in how_to
    def if_need_add_callout_line(prior_line_has_callout, how_to, html_data):
        if prior_line_has_callout and "bd_callout" in html_data:
                
            # check if str, list or dict
            if type(how_to[-1]["content"]) == list:
                how_to[idx-1]["content"].append([*how_to[idx-1]["content"], html_data])
            else: # type(how_to[-1]["content"]) == str or type(how_to[-1]["content"]) == dict
                how_to[idx-1]["content"].append([how_to[idx-1]["content"], html_data])

    # order data acording to Md `
    def sort_buld_sm_code_block(data, ch_idxs):
        code_data = {}
        
        code_data["tag"] = "span"
        code_data["content"] = []

        if ch_idxs[0]["idxs"][0] != 0:
            content = data[0:ch_idxs[0]["idxs"][0]]
            code_data["content"].append({
                "tag": "span",
                "content": content
            })

        # loop through ch_idxs
        last_i2 = None
        for code_info in ch_idxs:
            [i1, i2] = code_info["idxs"]

            # if last_i2 is not None add the text between the last_i2 and i1 to the list
            if last_i2 != None:
                content = data[last_i2:i1]
                code_data["content"].append({
                    "tag": "span",
                    "content": content
                })

            content = data[i1+1:i2]
            code_data["content"].append({
                "tag": "code",
                "content": content
            })

            last_i2 = i2 + 1


        # if last the last list in ch_idxs at index 1 is not the last index of text add the text between the last_i2 and the end of the text to the list
        if last_i2 != None and last_i2 < len(data):
            content = data[last_i2:]
            code_data["content"].append({
                "tag": "span",
                "content": content
            })
        
        return code_data

    # order data acording to Md * | ** | ***
    # **Trie Initialization (`__init__` method)**
    # Trie **Initialization** (`__init__` method)
    def sort_buld_italic(text, ch_idxs):
        astrict_data = {}

        astrict_data["tag"] = "span"
        astrict_data["content"] = []

        def has_backticks(content):
            # if even instances of ` 
            if content.find('`') != -1 and content.count("`") % 2 == 0:
                ch_idxs = find_back_ticks(content)
                content = sort_buld_sm_code_block(content, ch_idxs)
            return content

        
        if ch_idxs[0]["idxs"][0] != 0:
            content = text[0:ch_idxs[0]["idxs"][0]]

            # if even instances of ` 
            content = has_backticks(content)

            astrict_data["content"].append({
                "tag": "span",
                "content": content
            })
        #     astrict_data["tag"] = "span"
        # elif text[0] == "***":

        # loop through ch_idxs
        last_i2 = None
        for astrict_info in ch_idxs:
            [i1, i2] = astrict_info["idxs"]
            astrid_count = astrict_info["type"]

            # if last_i2 is not None add the text between the last_i2 and i1 to the list 
            if last_i2 != None:
                content = text[last_i2:i1]

                # if even instances of ` 
                content = has_backticks(content)

                astrict_data["content"].append({
                    "tag": "span",
                    "content": content
                })
                
            if astrid_count == 3:
                content = text[i1+3:i2-2]

                # if even instances of ` 
                content = has_backticks(content)

                # add the text between i1 and i2 to the list as a bold tag
                astrict_data["content"].append({
                    "tag": "strong",
                    "content": {
                        "tag": "em",
                        "content": content,
                    }
                })
            else:
                content = text[i1+astrid_count:i2-astrid_count+1]

                # if even instances of ` 
                content = has_backticks(content)

                # add the text between i1 and i2 to the list as a bold tag
                # astrict_data["tag"] = "strong" if astrid_count == 2 else "em"
                astrict_data["content"].append({
                    "tag": "strong" if astrid_count == 2 else "em",
                    "content": content
                })

               
                
            last_i2 = i2 + 1  
          
        # if last the last list in ch_idxs at index 1 is not the last index of text add the text between the last_i2 and the end of the text to the list
        if last_i2 != None and last_i2 < len(text):
            content = text[last_i2:]

            # if even instances of ` 
            content = has_backticks(content)

            astrict_data["content"].append({
                "tag": "span",
                "content": content
            })

        return astrict_data
    
    # make html list data >>> ol | ul
    def make_html_list_data(html_data, markdown_list, idx, prior_line_has_callout, how_to, depth):

        
        li_data = {}
        li_data["tag"] = "ol" if markdown_list[idx].lstrip()[0].isnumeric() else "ul"
        li_data["content"] = []

        # use to keep track of the parent type (e.g. ol | ul) incase of children so onece the children are done we can continue with the sibling node of the parent
        main_old_idx = idx 
        is_ol_main = "ol" if li_data["tag"] == "ol" else "ul" 

        
        # while not empty line and starts with number immediately followed by '.' or starts with space(s) then number immediately followed by '.'
        def make_li_tags(idx, markdown_list, depth, li_data):

            # print("here 2")
            # print("\n*****\n", "\n li_data['content']: ", li_data["content"], "\n*****\n")

            loop_count = 0

            while (idx < len(markdown_list) and len(markdown_list[idx]) > 0 and markdown_list[idx] != '') and (markdown_list[idx].lstrip()[0] == '-' or (markdown_list[idx].lstrip()[0].isnumeric() and markdown_list[idx].lstrip()[1] == '.') or (markdown_list[idx].lstrip()[0:2].isnumeric() and markdown_list[idx].lstrip()[2] == '.')):
                loop_count += 1
                print("\n loop_count: ", loop_count, "\n*****\n")

                # print("here 3")
                spaces = len(markdown_list[idx]) - len(markdown_list[idx].lstrip())
                # if line spaces in front of the number make sub list
                if spaces > depth:

                    # sub_old_idx = idx
                    # is_ol_sub = True if markdown_list[idx].lstrip()[0].isnumeric() else False

                    content_res, idx = make_html_list_data(html_data, markdown_list, idx, prior_line_has_callout, how_to, spaces)
                    li_data["content"].append(content_res)
                    idx += 1
                    print("\n*****\n", "\n SPACE li_data['content']:\n ", li_data["content"], "\n*****\n")
                    continue
                elif spaces < depth:
                    # print("here 4")
                    return [idx, li_data]
                
                # remove the number and the '.' or the '-' and the spaces
                rm_count = 2 if markdown_list[idx].lstrip()[0] == '-' else 3 

                data = markdown_list[idx].lstrip()[rm_count:]

                # check if even instances of ** are present in the line
                if data.find('*') != -1 and data.count("*") % 2 == 0:
                    ch_idxs = find(data)
                    data = sort_buld_italic(data, ch_idxs)
                elif data.find('`') != -1 and data.count("`") % 2 == 0:
                    ch_idxs = find_back_ticks(data)
                    data = sort_buld_sm_code_block(data, ch_idxs)
                    
                # make {tag: li, content: data}
                li_data["content"].append({
                    "tag": "li",
                    "content": data,
                })

                idx += 1
            
            return [idx, li_data]

        idx, li_data = make_li_tags(idx, markdown_list, depth, li_data)


        # if prior_line_has_callout & "bd_callout" in html_data add to last dict in how_to
        # if_need_add_callout_line(prior_line_has_callout, how_to, html_data)
        # def is_ol_sibling(idx, markdown_list):
        #     return True if idx < len(markdown_list) and len(markdown_list[idx]) != 0 and markdown_list[idx].lstrip()[0].isnumeric() else False

        # # is_ol_sibling = markdown_list[idx].lstrip()[0].isnumeric()

        # siblying_l_type = "ol" if markdown_list[idx].lstrip()[0].isnumeric() else "ul" if markdown_list[idx].lstrip()[0] == "-" else False

        # while idx < len(markdown_list) and is_ol_main == ("ol" if markdown_list[idx].lstrip()[0].isnumeric() else "ul" if markdown_list[idx].lstrip()[0] == "-" else False):
        #     # print("\n*****\n", "\n in 2nd while loop \n", [idx, depth, li_data], "\n*****\n")
            
        #     if markdown_list[idx] == "":
        #         idx += 1
        #         continue

        #     # print(idx < len(markdown_list) and is_ol_main == markdown_list[idx].lstrip()[0].isnumeric())
            
        #     # print("\n*****\n", "\n is_ol_main \n: ", is_ol_main == markdown_list[idx].lstrip()[0].isnumeric(), "\n*****\n")
        #     # print("\n*****\n", "\n is_ol_main \n: ", is_ol_main, "\n*****\n")
        #     # print("\n*****\n" "\n is_ol_sibling \n: ", markdown_list[idx].lstrip()[0].isnumeric(), "\n*****\n")
        #     # print("\n*****\n", markdown_list[idx], "\n*****\n")
        #     # f = open('in 2nd while loop [idx, depth, li_data].json', 'w', encoding="utf-8")
        #     # json.dump([markdown_list, idx, depth, li_data], f, indent=4)
        #     # f.close() 
        #     print("here 1")
        #     idx, li_data = make_li_tags(idx, markdown_list, depth, li_data)

        return [li_data, idx-1]

    idx = 0  
    # loop through markdown_list
    while idx < len(markdown_list):
        
        # if empty line continue
        if markdown_list[idx] == "":
            idx += 1
            continue
        
        """
            html_data = {
                # key: Str | List | Dict

                # Optional ⌥
                "bd_callout": {"indent": Int},

                # Required❗️
                "tag": Str,
                # Str >>> "tag": "h2" | "h4" | "h5" | "p" | "fenced_code_block" | "code" | "strong" | "ul" | "ol" | "li" | "span" | "hr" | "em" 
                # TODO: add to Str >>> "a" | "img" | "iframe" | "table" | "tr" | "th" | "td" | "pre" | "b" | "div" | "br" | 

                # Required❗️ unless otherwise specified 
                # ∞ Infinite Possible nested tags 🆘 
                "content": Str | List | Dict
                # "Content_Str" >>> "content": "text to display",
                ''' [Content_List] >>> 
                "content": [
                    # Str | [Content_List] | {Content_Dict} 
                    "text to display",
                    [ [Content_List] ],
                    {Content_Dict}
                ],'''
                ''' {Content_Dict} >>> 
                "content": {
                    "tag": Str, 
                    "content": Str | [Content_List] | {Content_Dict},
                    "bd_callout": {"indent": Int} # Optional ⌥
                },'''
            }
        """
        
        html_data = {}  

        # check if line starts with >
        html_data = bd_callout(markdown_list, idx)

        # check if code block e.g. ``` 
        if markdown_list[idx].find("```") != -1:
            # loop through the list until the next ``` is found
            idx += 1
            # make {tag: code, content: code}
            html_data["tag"] = "fenced_code_block"
            html_data["content"] = '\n'

            # loop through code_lines and add each line to the content keep indentations "space(s)" the same
            while idx < len(markdown_list) and markdown_list[idx].find("```") == -1:
                html_data["content"] += f"{markdown_list[idx]}\n"
                idx += 1

            # if prior_line_has_callout & "bd_callout" in html_data add to last dict in how_to
            if_need_add_callout_line(prior_line_has_callout, how_to, html_data)
            
        # check if line starts with # | ## | ### followed by a space
        elif markdown_list[idx][0] == "#":
            symbol_count = 1
            if markdown_list[idx][0:2] == "##":
                if markdown_list[idx][0:3] == "###":

                    symbol_count = 3
                    html_data["tag"] = "h5"
                else:
                    symbol_count = 2
                    html_data["tag"] = "h4"
            else:
                html_data["tag"] = "h2"
            
            html_data["content"] = f"{markdown_list[idx][symbol_count+1:]}"

        # if --- create hr tag & continue
        elif markdown_list[idx][0:3] == "---":
            html_data["tag"] = "hr"
            html_data["content"] = ""

        # ? Starts w/ (num >>> '.' | '-')  | space(s) >>> ( "-" | num >>> '.' )  
        elif markdown_list[idx].lstrip()[0].isnumeric() and markdown_list[idx].lstrip()[1] == '.' or markdown_list[idx].lstrip()[0] == '-':

            # get indent info
            depth = len(markdown_list[idx]) - len(markdown_list[idx].lstrip())

            # print(depth)
            # make html list data
            li_data, idx = make_html_list_data(html_data, markdown_list, idx, prior_line_has_callout, how_to, depth)


            html_data["tag"] = li_data["tag"]
            html_data["content"] = li_data["content"]

        # check if even instances of ** are present in the line
        elif markdown_list[idx].find('*') != -1 and markdown_list[idx].count("*") % 2 == 0:

            ch_idxs = find(markdown_list[idx])
            
            # order data acording to Md * | ** | ***
            res = sort_buld_italic(markdown_list[idx], ch_idxs)

            html_data["tag"] = res["tag"]
            html_data["content"] = res["content"]
        
        # if even instances of ` are present in the line
        elif markdown_list[idx].find('`') != -1 and markdown_list[idx].count("`") % 2 == 0:
            ch_idxs = find_back_ticks(markdown_list[idx])

            # order data acording to Md `
            data_res = sort_buld_sm_code_block(markdown_list[idx], ch_idxs)

            if data_res["tag"] == "span":
                html_data["tag"] = "p"
            else:
                html_data["tag"] = data_res["tag"]

            html_data["content"] = data_res["content"]
            
        
        else:
            html_data["tag"] = "p"
            html_data["content"] = markdown_list[idx]


        # if prior_line_has_callout & "bd_callout" in html_data add to last dict in how_to
        if_need_add_callout_line(prior_line_has_callout, how_to, html_data)
        # if html_data["bd_callout"] prior_line_has_callout = True
        if "bd_callout" in html_data: 
            prior_line_has_callout = True
        else:
            prior_line_has_callout = False

        how_to.append(html_data)
        idx += 1

    context["how_to"] = how_to

    # turn how_to into json
    # write data to JSON file
    f = open('how_to.json', 'w', encoding="utf-8")
    json.dump(how_to, f, indent=4)
    f.close()  

    print('DONE✨')

    return render_template('pages/test.html', **context)

@app.route('/sitemap')
def sitemap():
    """Display the sitemap page."""

    context = {}
    context["solutions"] = []
    context["steps"] = []

    for product in solutions_info:
        solution = {}

        solution["id"] = product["_id"]
        solution["name"] = product["name"]

        context["solutions"].append(solution)

    for step in Swe_career_guide().swe_career_guide:

        step_info = {}
        step_info['title'] = step["title"]
        step_info['url'] = f'{step["title"].replace(" ", "_")}/Getting_Started'
        step_info["pages"] = []

        for page in step['pages']:
            page_info = {}

            page_info["title"] = page["title"]
            page_info["url"] = f'{step["title"].replace(" ", "_")}/{page["title"].replace(" ", "_")}'

            step_info["pages"].append(page_info)


        context["steps"].append(step_info)
        
    return render_template('pages/sitemap.html', **context)

# Pass Stuff to Navbar
@app.context_processor
def base():
    form = SearchForm()
    return dict(form=form)

# Pass Stuff to Navbar
# @app.context_processor
# def search(query):
#     form = SearchForm()
#     form.searched.data = query
#     return dict(form=form)


@app.route('/search', methods=['GET','POST'])
def search():
    form = SearchForm()
    
    """
        TODO: 
            - fix issue with search not working due to validation
            - then Add back in validation here & in base.html 👇👇👇 
                if form.validate_on_submit():
    """

    # if form.validate_on_submit():
    if form.searched.data != None and form.searched.data != "":
       

        # remove extra spaces
        query = " ".join(form.searched.data.strip().split())
        
        
        return redirect(url_for('search_solutions', query=query, page_number=0))
    
    else:
        return redirect(url_for('search_solutions', query="None", page_number=0))


# Search res pg
@app.route('/search_solutions/<query>/<page_number>') 
def search_solutions(query, page_number):
    """Display the search_solutions page."""

    page_number = int(page_number)
    context = {}
    context["page_number"] = page_number

    def get_24_seach_res(res):
        solution_to_send  = []
        idx = page_number*24

        # jump straight to the starting index based on page number use while loop
        while idx < page_number*24+24 and idx < len(res):
            # only send the necessary data
            solution_to_send.append({
                "name": res[idx]["name"],
                "site": res[idx]["site"],
                "_id": res[idx]["_id"],
                "href": res[idx]["href"]
            })
            idx += 1
        
        return solution_to_send

    if query != "None":
        context["searched"] = query
        # get all solutions that match the query
        search_res = [solution for solution in solutions_info if query.lower() in solution["name"].lower()]

        context["solutions"] = get_24_seach_res(search_res)
        context["res_count"] = len(search_res)

        # context["solutions"] = [solution for solution in solutions if query.lower() in solution["name"].like('%{query}%')]
        # context["solutions"] = solutions.filter(solutions.name.like(f"%{query}%"))
    else:
        context["searched"] = "None"
        context["solutions"] = get_24_seach_res(solutions_info)
        context["res_count"] = len(solutions_info)

    # Global variables to store pagination numbers
    # pg_nav1_var = pg_nav2_var = pg_nav3_var = pg_nav4_var = None

    def set_pagination_numbers(page_number, search_solutions_count):

        # Get the current page number from the URL
        pg_num = page_number + 1

        # Determines how many pagination navigation numbers will show,
        # depending on the current page and the number of search results
        if pg_num > 3:
            pg_nav4_var = math.ceil(search_solutions_count / 24)  # last page number

            if pg_num != pg_nav4_var:
                pg_nav1_var = pg_num - 2
                pg_nav2_var = pg_num - 1
                pg_nav3_var = pg_num
            else:
                pg_nav1_var = pg_num - 3
                pg_nav2_var = pg_num - 2
                pg_nav3_var = pg_num - 1

        else:
            if search_solutions_count > 95:
                pg_nav1_var = 1
                pg_nav2_var = 2
                pg_nav3_var = 3
                pg_nav4_var = math.ceil(search_solutions_count / 24)

            elif search_solutions_count > 24:
                pg_nav1_var = 1
                pg_nav2_var = 2
                pg_nav3_var = False
                pg_nav4_var = math.ceil(search_solutions_count / 24)

            else:
                pg_nav1_var = 1
                pg_nav2_var = False
                pg_nav3_var = False
                pg_nav4_var = False

        return pg_nav1_var, pg_nav2_var, pg_nav3_var, pg_nav4_var
    
    # Set the pagination numbers
    context["pg_nav1_var"], context["pg_nav2_var"], context["pg_nav3_var"], context["pg_nav4_var"] = set_pagination_numbers(page_number,context["res_count"])
    pg_nav1_var = context["pg_nav1_var"]
    pg_nav2_var = context["pg_nav2_var"]
    pg_nav3_var = context["pg_nav3_var"]
    pg_nav4_var = context["pg_nav4_var"]


    # Define the underline style for page number workarounds for Safari & Firefox
    pg_num_underline = 'text-decoration: underline solid #0280C8 !important; -webkit-text-decoration-line: underline !important;-webkit-text-decoration-color: #0280C8 !important; -webkit-text-decoration-style: solid !important;-webkit-text-decoration-thickness: 2px !important;' 

    def set_page_link_style_1(page_number, pg_nav1_var, pg_nav2_var):

        # Determine the border-radius style
        if not pg_nav2_var:
            border_radius = '5px 5px'
        else:
            border_radius = '0px 0px'

        # Determine if underline style should be added
        if pg_nav1_var == page_number+1:
            underline_style = f'; {pg_num_underline}'
        else:
            underline_style = ';'

        # Combine all styles
        return f'border-radius: 5px {border_radius} 5px{underline_style}'

    context["page_link_style_nav1"] = set_page_link_style_1(page_number, pg_nav1_var, pg_nav2_var)

    def build_pagination_pg_num(pg_nav_var, next_pg_nav_var, pg_num, right_border_radius, pg_num_underline):
        if pg_nav_var:
            page_link_style = pg_num_underline if pg_nav_var == pg_num else ""
            if not next_pg_nav_var:
                page_link_style += right_border_radius
            return {
                'pg_nav_var': pg_nav_var,
                'page_link_style': page_link_style
            }
        return None
    
    # Define the right border radius style
    right_border_radius = "border-radius: 0px 5px 5px 0px;"

    # Build pagination data
    pagination_links = []
    pagination_links.append(build_pagination_pg_num(pg_nav2_var, pg_nav3_var, page_number+1, right_border_radius, pg_num_underline))
    pagination_links.append(build_pagination_pg_num(pg_nav3_var, pg_nav4_var, page_number+1, right_border_radius, pg_num_underline))
    pagination_links = [link for link in pagination_links if link]

    context["pagination_links"] = pagination_links

    
    
    show_last_page_link = pg_nav4_var and pg_nav4_var != pg_nav2_var and pg_nav4_var != pg_nav3_var
    last_page_link_style = None
    # Determine the style for the last page link
    if show_last_page_link:
        if pg_nav4_var == page_number+1:
            last_page_link_style = f"{right_border_radius} {pg_num_underline}"
        else:
            last_page_link_style = right_border_radius

    context["show_last_page_link"] = show_last_page_link
    context["last_page_link_style"] = last_page_link_style


    return render_template('pages/code_solutions/search_solutions.html', **context)


# Wrap Flask app with Talisman
Talisman(app, content_security_policy=None)

if __name__ == '__main__':
    app.run(debug=True)