from flask import Flask, request, redirect, render_template, url_for
from flask_talisman import Talisman

############################################################
# SETUP
############################################################

app = Flask(__name__)


############################################################
# ROUTES
############################################################

@app.route('/')
def home():
    """Display the home page."""

    context = {
        "array": [
            {
                "src": "",
                "alt": "img",
                "href": "/",
                "title": "example"
            },
            {
                "src": "",
                "alt": "img",
                "href": "/art",
                "title": "example2"
            },
        ],
        "array2": [
            {
                "src": "",
                "alt": "img",
                "title": "Example Product",
                "_id": 764524756,
                "info": "Ex",
                "href": "/item/764524756"
            },
        ]
    }

    return render_template('home.html', **context)

@app.route('/swe_career_guide')
def swe_career_guide():
    """Display the swe_career_guide page."""

    return render_template('swe_career_guide.html')

@app.errorhandler(404)
def page_not_found(e):
    return render_template('404.html'), 404

@app.route('/code_solution/<solution_id>')
def art():
    """Display the Code Solutions page."""
    

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
        "products": [
            {
                "src": "",
                "alt": "img",
                "title": "Example Product",
                "_id": 764524756,
                "info": "Ex",
                "href": "/solution/764524756"
            },
            {
                "src": "",
                "alt": "img",
                "title": "Example Product",
                "_id": 764524756,
                "info": "Ex",
                "href": "/solution/764524756"
            },
            {
                "src": "",
                "alt": "img",
                "title": "Example Product",
                "_id": 764524756,
                "info": "Ex",
                "href": "/solution/764524756"
            },
            {
                "src": "",
                "alt": "img",
                "title": "Example Product",
                "_id": 764524756,
                "info": "Ex",
                "href": "/solution/764524756"
            },
            {
                "src": "",
                "alt": "img",
                "title": "Example Product",
                "_id": 764524756,
                "info": "Ex",
                "href": "/solution/764524756"
            },
            {
                "src": "",
                "alt": "img",
                "title": "Example Product",
                "_id": 764524756,
                "info": "Ex",
                "href": "/solution/764524756"
            },
            {
                "src": "",
                "alt": "img",
                "title": "Example Product",
                "_id": 764524756,
                "info": "Ex",
                "href": "/solution/764524756"
            }
        ]
    }

    return render_template('code_solutions.html', **context)

@app.route('/search_solutions')
def art_supplies():
    """Display the search_solutions page."""

    context = {
    }

    return render_template('search_solutions.html', **context)

# Wrap Flask app with Talisman
Talisman(app, content_security_policy=None)

if __name__ == '__main__':
    app.run(debug=True)