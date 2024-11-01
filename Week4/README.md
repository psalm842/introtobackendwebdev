# Week 4 - Forms

## What is a form?

Unless you’re planning to build websites and applications that do nothing but publish content, and don’t accept input from your visitors, you’re going to need to understand and use forms.[^1]

HTML Forms are all the interactive bits on web pages, e.g. the search box on the google home page, or the text fields to enter your user name and password. Even the add to cart button on a shopping site. 

## Quick Review of Forms

A form is a collection of html tags that starts with `<form>` and ends with `</form>`. Usually inside the form are one or more `<input>` tags. 

There are several types of input tags. The most common are shown below. 

The `<input>` tag has a **required** attribute, `type=`. The `type` attribute can be set to any of the following:
- `text` - A single line text box
- `password` - A single line text box, but all characters show up as dots when the users enters typed characters.
- `radio` - A radio button, only one button in a radio button group can be selected at a time
- `checkbox` - A checkbox, similar to a radio, but multiple checkboxes can be selected at once
- `file` - lets the user select a file (looks like a single line text box with a "browse" button next to it)
- `submit` - Creates a button that submits the form to a web server. ~~We won't be covering that in this class. But maybe next semester.~~ **Welcome to next semester! :)**

Lastly, for radio buttons you will want to use the `name` attribute as it makes it so that you can only select ONE radio buttons of all the radio buttons that have the same name.

```html
<h4>Places to Go</h4>
<form>
    <input type="checkbox">Italy</input><br/>
    <input type="checkbox">Canada</input><br/>
    <input type="checkbox">Uruguay</input><br>
    <input type="checkbox">Lithia</input>
</form>
```

<h4>Places to Go</h4>
<form>
    <input type="checkbox">Italy</input><br/>
    <input type="checkbox">Canada</input><br/>
    <input type="checkbox">Uruguay</input><br>
    <input type="checkbox">Lithia</input>
</form>


```html
<h4>Vote for Lithian President</h4>
<form>
    <input type="radio" name="vote">Elizabeth Laws</input>
    <br>
    <input type="radio" name="vote">Donald Duck</input>
    <br>
    <input type="radio" name="vote">
        Write-In:
        <input type="text"></input>
    </input>
    <input type=submit>
</form>
```

<h4>Vote for Lithian President</h4>
<form>
    <input type="radio" name="vote">Elizabeth Laws</input>
    <br>
    <input type="radio" name="vote">Donald Duck</input>
    <br>
    <input type="radio" name="vote">
        Write-In:
        <input type="text"></input>
    </input>
    <br>
    <input type=submit>
</form>

## How form data gets to Django

Form data is sent from the web page to the web server as either a GET request OR a POST request. 
The difference is pretty simple

- GET (as we saw last week) puts the data into the url via query parameters (i.e. `?<param>=<value>`). Django reads the GET data with request.GET

- POST data is invisible to the user but it sent via HTTP. Certain things like passwords (sensitive  information) should only be sent via POST and not GET. Django reads POST data with request.POST

- GET is often convenient for things that the user may want to bookmark or share a link to. There is no way to share a link for POST data, but a URL containing a search query can be shared

## Example 1 - Hello Forms!

Let's have a form get the user's name, and then render a hello page with that name.

```mermaid
sequenceDiagram
User->>Web Browser: Enter URL
Web Browser->>Django: Get index.html
Django-->>Web Browser: Send index.html
Web Browser-->>User: Show form (webpage)
User->>Web Browser: Fill out form (enter username)
Web Browser->>Django: Send name as GET request
Django-->>Web Browser: Send new html for name
Web Browser--)User: Show new web page content
```

1. Edit index.html and replace everything inside the `<body>` tag with the below code

    ```html
    <form action="/hello" method="get">
        <label for="user_name">Your name:</label>
        <input id="user_name" type="text" name="name" value="World">
        <br>
        <input type="submit">
    </form>
    ```

which will appear as below:
<br>
<form action="" method="get">
    <label for="user_name">Your name:</label>
    <input id="user_name" type="text" name="name" value="World">
    <br>
    <input type="submit">
</form>
<br>

1. Change urls.py so that the root of your website calls a "home" function
    ```python
    urlpatterns = [
        path('admin/', admin.site.urls),
        path('', hello_views.home), # this is new
        path('hello/', hello_views.sayHello),
    ]
    ``` 

1. Create the "home" method in views.py to render the index.html template
    ```python
    def home(request):
        return render(request, 'hello/index.html', {})
    ```

1. Create a new page named hello.html in hello/templates/hello/hello.html with the following html
    ```html
    <html>
        <head>
            <title>Hello!</title>
        </head>
        <body>
            <h1>Hello {{name}}!</h1>
        </body>
    </html>
    ```

1. The sayHello function should pass `name` in the context dictionary to the new hello.html template
    ```python
    def sayHello(request):
        name = request.GET.get('name', 'World')
        return render(request, 'hello/hello.html', {'name': name})
    ```

5. Run your web server and test it out


## Challenge!
Add a set of radio buttons that allows the user to select a title (e.g. Mr. or Mrs. or Ms.)
 
Hints:
1. Radio button inputs should be defined in the following format: `<input type="radio" name="some_shared_name" value="value_to_send_in_get_request_if_this_button_is_selected">What the user sees next to this button</input>`

1. All radio buttons should have the same name, but a unique value. The "name" of the radio buttons will be the name of the GET parameter, the "value" of the radio button will be the unique value assigned to the name. So in the URL after you click the submit button you will see "?name=something&radio_button_name=radio_button_value"

1. You will need to edit views.py to read the new GET parameter for title being passed in by the radio buttons and insert the person's title before their name 

[^1]: https://docs.djangoproject.com/en/5.1/topics/forms/
