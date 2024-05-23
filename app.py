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
import pprint
import math
from jinjaMarkdown.markdownExtension import markdownExtension




############################################################
# SETUP
############################################################


app = Flask(__name__)

# Secret Key for CSRF Protection in Flask-WTF
SECRET_KEY = os.urandom(32)
app.config['SECRET_KEY'] = SECRET_KEY

#add markdownExtension to enviroment (by default jinja_env)
app.jinja_env.add_extension(markdownExtension)


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
        print('\n\n*********\n\n',Swe_career_guide().swe_career_guide[step_num_idx]['title'].replace(' ', '_'),'\n\n*********\n\n')
        print('\n\n*********\n\n',Swe_career_guide().swe_career_guide[step_num_idx]['pages'][step_letter_idx+1]['title'].replace(' ', '_'),'\n\n*********\n\n')

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
        "markdown_how_to_solve": "To solve this coding challenge, we first need to understand the structure and functioning of a Trie (Prefix Tree). A Trie is a tree-like data structure that stores strings in a way that allows for efficient retrieval of words, especially when dealing with operations like prefix searches.\n\n## Explanation\n\n1. **Trie Initialization (`__init__` method)**:\n   - We initialize our Trie with an empty dictionary `root` which will act as the root node of the Trie.\n\n2. **Insert a Word into the Trie (`insert` method)**:\n   - We start at the root of the Trie.\n   - For each character in the word, if the character is not already present as a child of the current node, we create a new dictionary for that character.\n   - We then move to the next level (child node) and repeat until all characters are inserted.\n   - After inserting all characters of the word, we mark the end of the word by adding a special symbol `$` with a value of `True`.\n\n3. **Search for a Word in the Trie (`search` method)**:\n   - We start at the root and traverse through each character of the word.\n   - For each character, if the character is not found in the current node, the word does not exist in the Trie and we return `False`.\n   - If we successfully traverse through all characters, we then check for the special end-of-word symbol `$` to confirm the presence of the complete word.\n\n4. **Check for a Prefix in the Trie (`startsWith` method)**:\n   - Similar to the search method, we start at the root and traverse through each character of the prefix.\n   - If any character in the prefix is not found in the current node, the prefix does not exist in the Trie and we return `False`.\n   - If we successfully traverse through all characters, we return `True` since the prefix exists in the Trie.\n\n## Pseudocode\n\n```pseudo\nclass Trie:\n    # Initialize the Trie with an empty dictionary as root\n    method __init__():\n        root = {}\n\n    # Insert a word into the Trie\n    method insert(word):\n        node = root\n        for each char in word:\n            if char not in node:\n                node[char] = {}\n            node = node[char]\n        node['$'] = True  # Mark the end of the word\n\n    # Search for a word in the Trie\n    method search(word) -> boolean:\n        node = root\n        for each char in word:\n            if char not in node:\n                return False\n            node = node[char]\n        return '$' in node  # Return True if the end of word marker is found\n\n    # Check if there is any word in the Trie that starts with the given prefix\n    method startsWith(prefix) -> boolean:\n        node = root\n        for each char in prefix:\n            if char not in node:\n                return False\n            node = node[char]\n        return True  # All characters in prefix are found, so return True\n```\n\nThis pseudocode covers the initialization, insertion of words, searching for words, and checking for prefixes in a Trie data structure. This is the methodology for solving the coding challenge.",
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
    markdown_list = context["markdown_how_to_solve"].split("\n")
  
    idx = 0
    # loop through markdown_list
    while idx < len(markdown_list):
        # check if line starts with # followed by a space
        if markdown_list[idx][0] == "#":
            # add a class to the line
            how_to[idx] = {
                "tag": "h2",
                "content": f"{markdown_list[idx][2:]}"
            }

        # check if line starts with a number followed by a period
        elif markdown_list[idx].isdigit() and markdown_list[idx][1] == ".":
            # add a class to the line
            how_to[idx] = {
                "tag": "h5",
                "content": f"{markdown_list[idx]}"
            }
        else:
            

        idx += 1


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
        # 
    else:
        # print('form.searched.data: ',  type(form.searched.data))
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

    # print('\n ********** \n')
    # pprint.pprint(context["solutions"]) 
    # print('\n ********** \n')

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