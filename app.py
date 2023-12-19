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

    context = {}

    return render_template('pages/home.html', **context)

@app.route('/swe_career_guide')
def swe_career_guide():
    """Display the swe_career_guide page."""

    return render_template('pages/swe_career_guide.html')

@app.errorhandler(404)
def page_not_found(e):
    return render_template('pages/404.html'), 404

@app.route('/code_solution/<solution_id>')
def code_solution(solution_id):
    """Display the Code Solution page."""

    solutions = [
            {
                "name": "3 Sum",
                "site": "LeetCode",
                "_id": "9827643rb27b27v",
                "href": "/solution/9827643rb27b27v"
            },
            {
                "name": "Two Sum",
                "site": "LeetCode",
                "_id": "liauwehfipuwefhlkw98237r23",
                "href": "/solution/liauwehfipuwefhlkw98237r23"
            },
            {
                "name": "Add Two Numbers",
                "site": "LeetCode",
                "_id": "lknas2387b24897b2",
                "href": "/solution/lknas2387b24897b2"
            }
    ]

    context = {}

    for product in solutions:
        if product["_id"] == solution_id:
            context = product
            break

    return render_template('pages/code_solutions/code_solution.html', **context)

@app.route('/search_solutions')
def art_supplies():
    """Display the search_solutions page."""

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
                "name": "3 Sum",
                "site": "LeetCode",
                "_id": "9827643rb27b27v",
                "href": "/solution/9827643rb27b27v"
            },
            {
                "name": "Two Sum",
                "site": "LeetCode",
                "_id": "liauwehfipuwefhlkw98237r23",
                "href": "/solution/liauwehfipuwefhlkw98237r23"
            },
            {
                "name": "Add Two Numbers",
                "site": "LeetCode",
                "_id": "lknas2387b24897b2",
                "href": "/solution/lknas2387b24897b2"
            },
            {
                "name": "Add Two Promises",
                "site": "LeetCode",
                "_id": "injr237823b2497824",
                "href": "/solution/injr237823b2497824"
            },
            {
                "name": "All Paths From Source to Target",
                "site": "LeetCode",
                "_id": "kj23498234b2498724",
                "href": "/solution/kj23498234b2498724"
            },
            {
                "name": "Array Wrapper",
                "site": "LeetCode",
                "_id": "bkhj23893by234872",
                "href": "/solution/bkhj23893by234872"
            },
            {
                "name": "Binary Search Tree to Greater Sum Tree",
                "site": "LeetCode",
                "_id": "bh238713yuv2397213vyu2398h",
                "href": "/solution/bh238713yuv2397213vyu2398h"
            }
        ]
    }

    return render_template('pages/code_solutions/search_solutions.html', **context)

# Wrap Flask app with Talisman
Talisman(app, content_security_policy=None)

if __name__ == '__main__':
    app.run(debug=True)