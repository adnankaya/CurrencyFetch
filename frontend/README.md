     _                      _                 ____ _     ___
    / \   _ __   __ _ _   _| | __ _ _ __     / ___| |   |_ _|
   / △ \ | '_ \ / _` | | | | |/ _` | '__|   | |   | |    | |
  / ___ \| | | | (_| | |_| | | (_| | |      | |___| |___ | |
 /_/   \_\_| |_|\__, |\__,_|_|\__,_|_|       \____|_____|___|
                |___/
    

Angular CLI: 11.1.4
Node: 14.15.0
OS: linux x64

Angular: 11.1.2
... animations, common, compiler, compiler-cli, core, forms
... platform-browser, platform-browser-dynamic, router
Ivy Workspace: Yes

Package                         Version
---------------------------------------------------------
@angular-devkit/architect       0.1101.4
@angular-devkit/build-angular   0.1101.4
@angular-devkit/core            11.1.4
@angular-devkit/schematics      11.1.4
@angular/cli                    11.1.4
@schematics/angular             11.1.4
@schematics/update              0.1101.4
rxjs                            6.6.7
typescript                      4.1.5
bootstrap                       4.5.3

### Development
- `npm install -g @angular/cli`
- `npm install` this command will install all packages

## Compile code
- `ng build --prod`
- This command will export the fronend compiled files into backend/www-static/angular
- edit `index.html` like this. `{% load static %}` and `{% static 'main.12345.js' %}` and other js & css files.
```html
{% load static %}
<!doctype html>
<html lang="en">

<head>
  <meta charset="utf-8">
  <title>Website</title>
  <base href="/">
  <meta name="viewport" content="width=device-width, initial-scale=1">
  <link rel="icon" type="image/x-icon" href="favicon.ico">
  <link rel="stylesheet" href="{% static 'styles.9c791ff615dbc53d1167.css' %}">
</head>

<body>
  <app-root></app-root>
  <script src="{% static 'runtime.7b63b9fd40098a2e8207.js' %}" defer></script>
  <script src="{% static 'polyfills.00096ed7d93ed26ee6df.js' %}" defer></script>
  <script src="{% static 'scripts.a2bdafcd693adeb1e0a2.js' %}" defer></script>
  <script src="{% static 'main.4c4f1df1b42727a99ef6.js' %}" defer></script>
</body>

</html>

```
## OR better way
`ng build --prod --deploy-url=www-static/angular/`
