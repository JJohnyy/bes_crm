# BES CRM

\
&nbsp;
Live link can be found here - [link]( "live app")
\

&nbsp;
# Table of Contents
* [Background](#background "Background")
* [Mission Statement](#mission-statement "Mission Statement")
* [Target Audience](#target-audience "Target Audience")
    * [User Goals](#user-goals "User Goals")
    * [User Stories](#user-stories "User Stories")
    * [Requirements and Expectations](#requirements-and-expectations)
    * [Wireframes](#wireframes "Wireframes")
    * [Design Choices](#design-choices "Design Choices")
        * Fonts
            * Content
            * Headings
        * Colours
        * Images
    * [Structure](#structure "Structure")
        * Models
        * Forms
    * [Features](#features "Features")
        * Existing Features
        * Features to be implemented
    * [Technologies used](#technologies-used "Technologies used")
        * Languages
        * Libraries, Frameworks and Tools
    * [Testing](#testing "Testing")
        * UX Testing
        * Manual Testing
        * Code Validation
        * Bugs
        * Unfixed Bugs
    * [Deployment](#deployment "Deployment")
        * Local Deployment
        * Deployment via Heroku
    * [Credits](#credits "Credits")


# Background
 CRM was created for sales persons of Bohemian Estates with their constant need to be on the move in mind.
Therefore mobile first apporach was done. With the most important thing to able to do while with customer, to be able to quickly create a new lead with couple of clicks.

# Mission Statement
to create an app which makes life of a sales person easier thanks to its ability to do everything opn the go.

# Target audience
employees who could use this app

&nbsp;

| Name | Age | years of experience |
| -- | -- | -- |
|Robert Poppl|35|15|
|Yury Vachugov|38|4|
|Tereza Hanzlik|45|2|

&nbsp;

## User goals
1. create update and delete leads
2. quickly be able to do everything on the mobile phone
3. login and logout
4. view own details

## User stories
| ID | User Category | User wants to... | So they can... |
|--|--|--|--|
|01|app user|create lead|create and mantain list of leads|
|02|app user|update lead|update any changes on a lead|
|03|app user|delete a lead|delete a lead if needed|
|04|app user|login, logout|to be able to login and logout|
|05|app user|delete profile|delete own profile if needed|
|06|app user|register|easily register for an account|
|07|app user|list of leads|maintain a list of leads|

&nbsp;

## Requirements and Expectations

| Requirement | Expectation
| -- | --
| Visually appealing and well laid out | Colours to be complimentary, text to be clear. Navigation to be logical and simple
| Responsive design (Mobile first) | The screen size to not affect the look of the application 
| CRUD functionality | Easily maintain leads and profile


\
&nbsp;
[Back to Top](#table-of-contents)
\
&nbsp;

# Wireframes
| type | name | link | 
|--|--|--|
|PC|home page|[homepage](media/readmedocs/wireframes/home-page.png)|
|mobile|home page mobile|[homepagemobile](media/readmedocs/wireframes/mobile/home_page.png)|
|PC|login page|[homepage](media/readmedocs/wireframes/login.png)|
|mobile|login page||
|PC|signup page|[homepage](media/readmedocs/wireframes/signup.png)|
|mobile|signup page||
|PC|dashboard|[homepage](media/readmedocs/wireframes/dashboard.png)|
|mobile|dashboard||
|PC|lead list|[homepage](media/readmedocs/wireframes/lead list.png)|
|mobile|lead list||
|PC|create a lead|[homepage](media/readmedocs/wireframes/create a lead.png)|
|mobile|create a lead||
|PC|delete a lead|[homepage](media/readmedocs/wireframes/deleate a lead.png)|
|mobile|delete a lead||
|PC|update a lead|[homepage](media/readmedocs/wireframes/lead update.png)|
|mobile|udpate a lead||
|PC|udpate a profile|[homepage](media/readmedocs/wireframes/update profile.png)|
|mobile|update a profile||
|PC|delete a profile|[homepage](media/readmedocs/wireframes/profile delete.png)|
|mobile|delete a profile||

\
&nbsp;
[Back to Top](#table-of-contents)
\
&nbsp;


## Design Choices

### Fonts
there was no choice of a new font, everythnig was clearly visible with the default one

### Colors
[link](media/readmedocs/colors.png 'colors')

#### Colors and contrast validations
[contrast1](media/readmedocs/contrast-1.png 'colors contrast')
[contrast2](media/readmedocs/contrast-2.png 'colors contrast')

| Hex Value |Text | Button | Background |
| -- | -- | -- | -- |
|#FFFFF|||x|
|#285677||x||
|#285670|x|x||
|#|678D86||x|

&nbsp;


## Models

### leads
| Name | Key | Type | Other Details
| -- | -- | -- | --
|first_name||CharField|max_length=20
|last_name||CharField|max_length=20
|description||TextField|
|date_added||DateTimeField|auto_now_add=True
|phone_number||CharField|max_length=20
|email||EmailField|
|agent|User|ForeignKey|null=True, blank=True, on_delete=CASCADE


## Forms

LeadModelForm 
fields
* first name
* last name
* description
* phone number
* email

CustomerCretionForm
fields
* username
* email
* password1
* password2
* first_name
* last_name

CustomUserEdit
excludefields
* password
* last-login
* is_superuser
* groups
* date_joined
* user permissions
* is_active
* is_staff


\
&nbsp;
[Back to Top](#table-of-contents)
\
&nbsp;


## features

## Existing Features

### Navbar

## Authentication
The authentication process for the application has three parts.

* Sign Up
* Sign In
* Log out

### Sign Up
The signup process requests following required fields from the user:

* Username
* First name
* Last name
* Password
* Password confirmation

### Sign In
The sign-in form requires only two fields to be entered. 

* Username
* Password

## Features to be Implemented

\
&nbsp;
[Back to Top](#table-of-contents)
\
&nbsp;


## Languages
| Languages | Description | Link |
|--|--|--|
|HTML|[HTML](https://en.wikipedia.org/wiki/HTML5 "HTML") | for the structure of the site
|CSS|[CSS](https://en.wikipedia.org/wiki/CSS "CSS") | for the design of the site
|JavaScript|[JavaScript](https://en.wikipedia.org/wiki/JavaScript "JS") | for the design of the site
|jQuery|[jQuery](https://jquery.com/ "jQuery") | for animations in the site
|Python|[Python](https://en.wikipedia.org/wiki/Python_(programming_language) "Python") | for the backend interactions
|Markdown|[Markdown](https://en.wikipedia.org/wiki/Markdown) | for the content in my README file


## Libraries and Frameworks
| Libraries / Frameworks | Description | Link |
|--|--|--|
|Django|Database Driven Framework| [django](https://en.wikipedia.org/wiki/Django_(web_framework) "django")|
|gunicorn|HTTP Interface Server|[gunicorn](https://en.wikipedia.org/wiki/Gunicorn "gunicorn")|
|psycopg2| Database adaptor | [psycopg2](https://wiki.postgresql.org/wiki/Psycopg "psycogg2")
|cloudinary |Image management|[cloudinary](https://cloudinary.com/ "cloudinary")|
|django auth|User authentication|[auth](https://docs.djangoproject.com/en/3.2/topics/auth/ "auth")|


## Tools
| Tools | Description | Link |
|--|--|--|
| ColorMind|Colour palet| [coolors](http://colormind.io/ "colormind")|
| GitPod | Development environment |[Gitpod](https://www.gitpod.io/ "Gitpod")|
| Balsamic | Wireframes |[Balsamic](https://balsamiq.com/wireframes/ "Balsamic")|
| W3C | Markup Validation | [W3C Markup Validation Service](https://validator.w3.org/ "W3C")|
| W3C | CSS Validation | [W3C CSS Validation Service](https://jigsaw.w3.org/css-validator/ "W3C")|
| PEP8 | Python Validation | [PEP8](http://pep8online.com/ "PEP8")|

# Deployment

This project was created using GitHub and the code was written using Gitpod. This project is also deployed to Heroku with Heroku deployment set to *Enable Automatic Deploys*. This means that every time that the repository was pushed to, Heroku was updated also.

The live link to the application can be found [here](https://bescrm.herokuapp.com)

## Local Deployment

As Gitpod was the IDE that was used to create the project, the following local deployment steps are specific to Gitpod.

### Cloudinary
* Visit Cloudinary by following this [link](https://cloudinary.com)
* Click on the *Sign Up For Free* button
* When the account is created, you should see the *API Environment variable*, we will need this for a later process.

### GitHub
* Visit Github by following this [link](https://github.com/JJohnyy/bes_crm)
* Create an account or log in


* In the terminal run
```
pip3 install -r requirements.txt
```
* In the root directory create a file called **env.py** and add the following content, the content of these, must match the Config Vars in the Heroku deployment section

```py
import os

os.environ['DATABASE_URL'] = "FROM HEROKU DEPLOYMENT SECTION, DATABASE_URL CONFIG VAR"
os.environ['SECRET_KEY'] = "FROM HEROKU DEPLOYMENT SECTION SECRET_KEY CONFIG VAR"
os.environ['CLOUDINARY_URL'] = "API ENVIRONMENT VARIABLE REMOVE 'CLOUDINARY_URL=' FROM BEGINING"
os.environ['DEVELOP'] = '1'


* Add the env.py file to the .gitignore file to ensure that its contents are not made public

* Migrate the database models with the following command in the terminal

* Create a superuser and set up the credentials with the following command
```
python3 manage.py createsuperuser
```

* Run the application locally with the command
```
python3 manage.py runserver



### Deployment via Heroku
* Visit [heroku.com]()
* Create a new account or sign in
* From the dashboard, select **New** and then **Create new app**
* Enter an individual app name into the text box, select a region from the dropdown and then press **Create app**
* A Heroku app has now been created and the **Deploy** tab is opened. 
* Open the *Resources* tab and in the search bar for *Add-ons* type *Postgres*
* Select *Heroku Postgres*, on the popup, ensure the dropdown is set to *Hobby Dev - Free* and then *Submit Order Form*
* Open the *Settings* tab and then click on the *Reveal Config Vars* button and the database_url should be populated.
* Fill out the rest of the config vars with the content of the table below by filling out the *Key* and *Value* and clicking on *Add* for each entry 


* In the buildpacks section of the settings tab, click on **Add Buildpack**, select **python** and then save changes
* Open the **Deploy** tab
* In the deployment method section, select **GitHub** and confirm the connection.
* Enter the repo-name into the text box and click **Search**. When the correct repo appears below, click **Connect**
* Return to the Gitpod workspace and in the root directory create a file called *Procfile*
* In the *Procfile* enter the following line including your project name
```
web: gunicorn YOUR_PROJECT_NAME.wsgi
```
* Add and commit to GitHub
```
git add .
git commit -m "commit message goes here"
git push
```
* Add your Heroku app URL to ALLOWED_HOSTS in your settings.py file
```
ALLOWED_HOSTS = ['YOUR_PROJECT_NAME.herokuapp.com', 'localhost']
```

## Code Validation

### HTML

### CSS

### Python

