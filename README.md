# Get In Tech 

This platform will encompass not only a comprehensive guide for users aspiring to pursue a career as a software engineer (SWE), but it will also feature a repository of coding challenges I have personally resolved. Additionally, it will host a search engine capable of retrieving solutions to coding problems from various sources, including external websites and YouTube videos.



## Tech Used
- Python
    - pip3
    - Flask
        - flask-talisman
            - Talisman >>> [Medium](https://betterprogramming.pub/from-http-to-https-easily-secure-flask-web-apps-with-talisman-3359692d3eac)
            - `pip3 install flask-talisman`
        - flask-wtf
            - wtforms
    - MarkupSafe
    - Werkzeug
    - blinker
    - click
    - itsdangerous
    - Jinja2 
- HTML/CSS
- JavaScript
- Bootstrap
    - Bootstrap Icons
<!-- - MongoDB
    - Mongoos  -->
- Figma
<!-- - [Figma](https://www.figma.com/file/NhVv9RBbRln5Y4RTX1M1Ph/How-to-get-into-Tech?type=design&node-id=0-1&mode=design&t=UnGo5DO8TltFNFDZ-0) -->
- Heroku
    - Heroku CLI
    - gunicorn
    - [Heroku/NameCheep Setup Video](https://www.youtube.com/watch?v=51j_mhje9Kk)
    - [Enforce https](https://help.heroku.com/J2R1S4T8/can-heroku-force-an-application-to-use-ssl-tls)
- Git / GitHub
- Shell / bash / Terminal / CLI
- Web Advertising/Affiliate Marketing (Ads)
- Photoshop
- Google Analytics



## Helpful Tutorials    
- [YouTube: Flask/Jina2 Nav Search Component](https://www.youtube.com/watch?v=kmtZTo-_gJY)
    


## Install/Run

### Install
```
pip3 install -r requirements.txt
```

### Run
```
python3 app.py
```

## When Updating

- `git checkout -b <branch_name>`
- If you introduce new requirements, please regenerate the "requirements.txt" file.
    - `pip3 freeze > requirements.txt` 
    - If you are not utilizing a virtual environment, it will include all items, including those 
    - from other projects. ***Make sure to only add what is needed.*** 
- 

## Deploy

- Login to Heroku
- `heroku login`
- `git push heroku main`