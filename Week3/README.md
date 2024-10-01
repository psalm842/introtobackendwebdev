# Week 3 - Templating and HTTP GET Parameters

So far we've returned HTTP responses, but not any HTML. We haven't actually made a web page.

## Exercise 1 - Say Hello with Argument

Now we want to add the ability to customize our web page based on the name of the person using it. There are 2 ways to do this

### 1a - As an HTTP GET Parameter

1. Add the line `name = request.GET.get('name', 'World')` to the `sayHello` function in views.py. It should now look as follows:
    ```python
    def sayHello(request):
        name = request.GET.get('name', 'World')
        return HttpResponse(f"Hello {name}!")
    ```
    The line `name = ...` checks if the user passed in a http parameter named "name", if the user did not, then the default value of "World" is returned instead.

1. Go to `http://127.0.0.1:8000/hello` and you should still see the normal "Hello World!"

1. Go to `http://127.0.0.1:8000/hello?name=Tim` (or put in your name) and you should now see "Hello Tim!"

**Show google.com search GET parameters**

### 1b - As Part of the URL

Another way to do this is to make the name part of the path of the url, e.g. `http://127.0.0.1:8000/hello/tim` (notice there's no question mark or `name=`)

To do this we are going to add a new route to urls.py and a new function to views.py

1. In urls.py add the line following line to the urlpatterns array: `path('hello/<str:name>/', hello_views.sayHelloWithName),` so that now it looks as follows:
    ```python
    urlpatterns = [
        path('admin/', admin.site.urls),
        path('hello/', hello_views.sayHello),
        path('hello/<str:name>/', hello_views.sayHelloWithName),
    ]    
    ```
    The new path we added tells django that when it sees a url with hello and then ANOTHER string after it, to capture that string and call it "name". This means that the function that is called must have a second input named "name"

1. Now go to views.py and define a new function called `sayHelloWithName`:
    ```python
    def sayHelloWithName(request, name):
        return HttpResponse(f"Hello {name}!")
    ```
    Notice this is very similar to our previous `sayHello` function, but it has one more input parameeter, `name`.

1. Go to `http://127.0.0.1:8000/hello/Tim` (or put in your name) and you should now see "Hello Tim!"

## Exercise 2 - Say Hello with an HTML response

### HTML Recap

HTML Stands for Hypertext Markup Language. It describes the content and structure of a web page. An HTML web page consists of a series of tags (which you can look up on the internet by searching "HTML tags"), such as `<H1>My Header</H1>` 

It can be styled with CSS which changes the appearance of html.


1. Add some HTML tags to the sayHello function's response
    ```python
    def sayHello(request):
        name = request.GET.get('name', 'World')
        return HttpResponse(f"<H1>Hello {name}!</H1>")
    ```

1. Run your server and go to `http://127.0.0.1:8000/hello?name=Tim` (or put in your name) and you should now see "Hello Tim!"

    <img src="hello-world-html.png" width=300/>

## Templating and Static Files

So it is possible to return a web page using an http response as we just showed. However,
most web pages are large and it would make the python code really messy if we put the whole web page in there (it would become difficult to distinguish between what text was html and which was python code).

So how do we solve this problem? Templates (and static files, such as css, which we won't discuss today)

## Exercise 3 - Say Hello with an HTML Template

1. Create a directory in our hello folder (the app we began building last week) named "templates" (by default django is going to look for templates in this folder). 
1. Then inside create another folder named "hello". This is confusing, why create a folder named hello since we're already in the hello folder!? It has to do with how django resolves template names, and all I can say here is that it will make your life easier in the long run even though it doesn't make sense now. 
1. Inside the week 2 folder create a file named index.html (so the total path should be webdev_examples/hello/templates/hello/index.html)
1. Inside index.html put the following text:
    ```html
    <html>
    <head>
        <title>My first django template</title>
    </head>
    <body>
        <h1>Hello World!</h1>
    <body>
    </html>
    ```
1. Change views.py to use the template by using the render function 

    ```python
    def sayHello(request):
        name = request.GET.get('name', 'World') # not used here...yet
        return render(request, 'hello/index.html', {})
    ```

    The render function takes 3 inputs, first is the request from the host, second is the path/name of an html file template, last is the context. We'll use the context in the next step. For now we are passing an empty **dictionary**. 

    For now, load the /hello page in your web browser and notice it still says Hello World! (It will ignore any name parameter passed into it).

1. Go to `http://127.0.0.1:8000/hello?name=Tim` (or put in your name) and you should now see "Hello Tim!"

## Exercise 4 - Say hello with an HTML Template with Context

Now we're ready to add some context.

The context is a dictionary of data. A dictionary is a datatype in python that is what it sounds like, you can name a field and then give that field a value, e.g. `my_groceries_dict = {'apples': 3, 'bananas':4, cake: 1}`

```python
>>> my_groceries_dict = {'apples':3, 'bananas':4, 'cake':1}
>>> my_groceries_dict
{'apples': 3, 'bananas': 4, 'cake': 1}
>>> my_groceries_dict['bananas']
4
```
or
```python
>>> context_dictionary = {'name':'Tim'}
>>> context_dictionary['name']
Tim
```

1. Update the context dictionary to include the name in the sayHello view method:
    ```python
    def sayHello(request):
        name = request.GET.get('name', 'World')
        return render(request, 'hello/index.html', {'person_to_greet': name})
    ```

2. Update the body of the template (`index.html`) to read the name from the context dictionary
    ```html
    <body>
        <h1>Hello {{person_to_greet}}!</h1>
    </body>
    ```

Django will look in the context dictionary for a field with a name matching whatever is inside the curly braces `{{<context dictionary field name>}}`

3. Visit the page and pass in the name, e.g. `http://localhost:8000/hello?name=tim

It should now correct render the name of the person in the web page 

## Challenge

Using either of the 2 methods above make the web server accept a "title" parameter and then display `Hello <title> <name>`, e.g. "Hello Mr. Viola" if a title is provided and `Hello <name>`, e.g. "Hello Tim" if no title is provided.


https://docs.djangoproject.com/en/5.1/howto/static-files/deployment/