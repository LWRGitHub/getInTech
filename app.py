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
from data.Search_solutions import Search_solutions


# import pprint
import math
# import re
# import json

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
    
    # check if "markdown_how_to_solve" in context
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

    return render_template('pages/test.html')

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

    old_url = request.referrer
    # "/search_solutions" in old_url 
    # print(request.referrer)

    search_text = old_search_text = page = topic = platform = language = sort = None

    # assing search_text
    if "/search_solutions/" in old_url:

        old_query = request.referrer.split("/search_solutions/")[1]
        # splite request.referrer at "/search_solutions/"
        search_text = old_query

        # split at "%3F" || "?"
        search_text = search_text.split("%3F")[0]
        if "%20" in search_text:
            search_text = search_text.split("%20")
            search_text = " ".join(search_text)
        
        # if old_query has platform
        if "platform" in old_query:
            platform = old_query.split("platform=")[1]
            if "&" in platform:
                platform = platform.split("&")[0]
            if "%20" in platform:
                platform = platform.split("%20")
                platform = " ".join(platform)
        # if old_query has topic
        if "topic" in old_query:
            topic = old_query.split("topic=")[1]
            if "&" in topic:
                topic = topic.split("&")[0]
            if "%20" in topic:
                topic = topic.split("%20")
                topic = " ".join(topic)
        # if old_query has language
        if "language" in old_query:
            language = old_query.split("language=")[1]
            if "&" in language:
                language = language.split("&")[0]
            if "%20" in language:   
                language = language.split("%20")
                language = " ".join(language)
        # if old_query has sort
        if "sort" in old_query:
            sort = old_query.split("sort=")[1]
            if "&" in sort:
                sort = sort.split("&")[0]
            if "%20" in sort:
                sort = sort.split("%20")
                sort = " ".join(sort)

    if form.searched.data != None:
        new_search_text = " ".join(form.searched.data.strip().split())
        if new_search_text == "":
            search_text = None
        else:
            # remove extra spaces
            search_text = new_search_text

    # get the search filter data
    if "topic" in form and form.topic.data != None: 
        topic = form.topic.data if form.topic.data != "All" else None
    if "platform" in form and form.platform.data != None: 
        platform = form.platform.data if form.platform.data != "All" else None
    if "language" in form and form.language.data != None: 
        language = form.language.data if form.language.data != "All" else None
    if "sort" in form and form.sort.data != None: 
        sort = form.sort.data if form.sort.data != "..." else None
    
    query = f"{search_text}?page={page if page else 0}{f'&platform={platform}'if platform else ''}{f'&topic={topic}'if topic else ''}{f'&language={language}'if language else ''}{f'&sort={sort}'if sort else ''}"

    return redirect(url_for('search_solutions', query=query))


# Search res pg
@app.route('/search_solutions/<query>') 
def search_solutions(query):
    """Display the search_solutions page."""
    context = {}

    # search data
    sort = all_query_data = other_query_data = page_number = platform = topic = language = None
    filter_data = ""

    # print(query)

    # filter data (not page or search text)
    if "&" in query:
        idx = query.index("&")
        filter_data = query[idx:]

    print(filter_data)

    context["filter_data"] = filter_data

    if "?" in query:
        all_query_data = query.split("?")
        query = all_query_data[0]
        other_query_data = all_query_data[1]

        # check if <search filter> is in query
        # if it is get the <search filter>
        if "page" in other_query_data:
            print("HERE_page")
            # find index of page
            page_number = other_query_data.split("page=")[1]
            # remove & and all after if it exists
            if "&" in page_number:
                page_number = page_number.split("&")[0]
            page_number = int(page_number)
        else:
            page_number = 0
            
        if "platform" in other_query_data:
            platform = other_query_data.split("platform=")[1]
            if "&" in platform:
                platform = platform.split("&")[0]

        if "topic" in other_query_data:
            topic = other_query_data.split("topic=")[1]
            if "&" in topic:
                topic = topic.split("&")[0]

        if "language" in other_query_data:
            language = other_query_data.split("language=")[1]
            if "&" in language:
                language = language.split("&")[0]

        if "sort" in other_query_data:
            sort = other_query_data.split("sort=")[1]
            if "&" in sort:
                sort = sort.split("&")[0]
        
    else:
        query = "None"


    # page_number = int(page_number)
    
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

    # Add search filter data
    search_filters = {}
    search_filters["platforms"] = Search_solutions().platforms
    search_filters["topics"] = Search_solutions().topics
    search_filters["languages"] = Search_solutions().languages
    context["search_filters"] = search_filters

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