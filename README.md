# Flask practice

Six independent local apps cover routes, HTTP methods and Jinja templates. Use Python 3 and Flask. From this directory:

```text
python -m pip install Flask
python 04_templatesAndStaticFiles/main.py
```

Visit `http://127.0.0.1:5000/profile/Alex`: expect a green “Hey there Alex” heading. Lesson 04 has no `/` route. Keep each app with its own `templates` and `static` directories where present.

Stop the development server with Ctrl+C before running another `main.py`. In 03, GET and POST to `/bacon` return different messages; in 05, `/shopping` renders a three-item list. Lessons 01–05 were checked with Flask’s local test client, including template and stylesheet responses. The development server is not a production deployment.

Lesson 06: run `python 06_bootstrap/main.py` and visit `/` for three navigation tabs. It ships the relevant Bootstrap 3.4.1 navigation rules and the accompanying MIT notice in `static`; no CDN, fonts or JavaScript are required. The route and stylesheet passed local client checks. `python test.py` is a separate loopback-address example, not a test suite.
