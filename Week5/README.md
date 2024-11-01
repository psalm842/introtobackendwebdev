# Week 5 - Practice makes perfect!

## Review

- A Django **project** is made up of one or more **apps**
- each app is a self contained unit of functionality, such as our **hello** app
- `manage.py` is created when `python -m django startproject` is called, it can then be used to start new **apps** within the project, e.g. `python manage.py startapp`
    - don't forget to add your app to the **middleware** section in `settings.py`
- The workflow for starting a new page is:
    1. Create the url in **urls.py** that calls a new view function
    1. Create the function that **urls.py** calls for that url in **views.py** that renders a template (remember to pass in any context needed!)
    1. Create the **template** rendered by **views.py** as `<appfolder>/template/<appname>/<template_name>.html`

## Exercise 1

Create a new app in your existing webdev_examples project called quizzer.

Don't forget to "install" your app in settings.py

## Exercise 2

Create two new html templates quiz.html and results.html.

Create a new route so the user can get to quiz.html with the url `http://127.0.0.1:8000/quiz`

Quiz.html should have a 3 question multiple choice quiz and a submit button. The questions can be any 3 questions you like.

Results.html should show the user their score after they hit the submit button.

## Exercise 3

Set up your index.html to include a hyperlink to the quiz