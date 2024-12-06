# Week 6 - Databases and Templating Functions

## What is a database?

A database is simply a specific way of organizing data to store for later retrieval.

Common things a database might be used for include a list of all the users of the website, their email addresses, and mailing list preferences.

In the case of really large websites like Amazon the database is a list of millions of items, their prices, descriptions, and even images. 

Today we're going to create an extremely simple database of all the responses that we receive to our quiz

## Exercise 1 - A pseudo database

In your quiz app add the below code *to the appropriate function* (which function **reads** the response from the user?)

The code below opens a file named responses.txt (our "database") and then **appends** each new response to it

*Note:* You will need to replace "question1_answer" with the name of whatever variable is holding the answer to your question
```python
with open('responses.txt', 'a') as f:
    f.write(f"{question1_answer}, {question2_answer}, {question3_answer}\n")
```

Take your quiz 3 or 4 times and then open the file responses.txt and look at it's contents

## Exercise 2 - Add a new page to quizzer called "History"

Add a url in urls.py for "/history" and have it call a new function called "history"

Define the history function as shown below. This reads the file

```python
def history(request):
    with open('responses.txt', 'r') as f:
        responses = f.readlines()
    return render(request, 'quizzer/history.html', {"responses": responses})
```

`f.readlines` reads a file and adds each line of the file into an array element. 

Create the history.html template. the `{%for ...}` statement below takes each element of the array (in this case each element is a line from the responses.txt file) and generates the specified html for each element of the array.

```html
<html>
    <head>
        <title>Quiz History</title>
    </head>
    <body>
        <h1>Responses</h1>
        {%for resp in responses%}
            <p>{{resp}}</p>
        {%endfor%}
    </body>
</html>
```

Now go to 127.0.0.1:8000/history and you should see all the quiz responses

