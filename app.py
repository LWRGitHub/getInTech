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



############################################################
# SETUP
############################################################



app = Flask(__name__)

# Secret Key for CSRF Protection in Flask-WTF
SECRET_KEY = os.urandom(32)
app.config['SECRET_KEY'] = SECRET_KEY

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

    form = SearchForm()

    context = {
        "page": {
            "name": "Code Solutions"
        },
        "other_example": [
            {
                "name": "Example",
                "src": "",
                "alt": "img"
            },
        ],
        "form": form
    }

    if query != "None":
        context["searched"] = query
        context["solutions"] = [solution for solution in solutions if query.lower() in solution["name"].lower()]
        # context["solutions"] = [solution for solution in solutions if query.lower() in solution["name"].like('%{query}%')]
        # context["solutions"] = solutions.filter(solutions.name.like(f"%{query}%"))
    else:
        context["searched"] = False
        context["solutions"] = solutions   

    return render_template('pages/code_solutions/search_solutions.html', **context)


# Wrap Flask app with Talisman
Talisman(app, content_security_policy=None)

if __name__ == '__main__':
    app.run(debug=True)