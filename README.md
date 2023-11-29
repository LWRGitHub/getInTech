# Get In Tech 

This platform will encompass not only a comprehensive guide for users aspiring to pursue a career as a software engineer (SWE), but it will also feature a repository of coding challenges I have personally resolved. Additionally, it will host a search engine capable of retrieving solutions to coding problems from various sources, including external websites and YouTube videos.


## Tech Used
- Python
    - Flask
    - Jinja2
    - Talisman >>> [Medium](https://betterprogramming.pub/from-http-to-https-easily-secure-flask-web-apps-with-talisman-3359692d3eac)
- HTML/CSS
- JavaScript
- Bootstrap
    - Bootstrap Icons
- MongoDB
    - Mongoos 
- [Figma](https://www.figma.com/file/NhVv9RBbRln5Y4RTX1M1Ph/How-to-get-into-Tech?type=design&node-id=0-1&mode=design&t=UnGo5DO8TltFNFDZ-0)
- Heroku
    - Heroku CLI
    - gunicorn
    - [https/SSL Certificate Setup](https://help.heroku.com/J2R1S4T8/can-heroku-force-an-application-to-use-ssl-tls)
- GitHub
- Google Adsence



## Install/Run

### Install
```
pip3 install -r requirements.txt
```

### Run
```
python3 app.py
```

## NOTES

- If you introduce new requirements, please regenerate the "requirements.txt" file.
    - `pip3 freeze > requirements.txt` 
    - If you are not utilizing a virtual environment, it will include all items, including those 
    - from other projects. ***Make sure to only add what is needed.*** 
- 

## Deploy

- Login to Heroku
- `heroku login`
- `git push heroku main`