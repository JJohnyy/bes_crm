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
|PC|login page|[login](media/readmedocs/wireframes/login.png)|
|mobile|login page|[loginmobile](media/readmedocs/wireframes/mobile/login.png)|
|PC|signup page|[signup](media/readmedocs/wireframes/signup.png)|
|mobile|signup page|[signupmobile](media/readmedocs/wireframes/mobile/signup.png)|
|PC|dashboard|[dashboard](media/readmedocs/wireframes/dashboard.png)|
|mobile|dashboard|[dashboardmobile](media/readmedocs/wireframes/mobile/dashboard.png)|
|PC|lead list|[leadlist](media/readmedocs/wireframes/leadlist.png)|
|mobile|lead list|[leadsmobile](media/readmedocs/wireframes/mobile/leadlist.png)|
|PC|create a lead|[createalead](media/readmedocs/wireframes/createalead.png)|
|mobile|create a lead|[createleadmobile](media/readmedocs/wireframes/mobile/createalead.png)
|PC|delete a lead|[deletealead](media/readmedocs/wireframes/deleatealead.png)|
|mobile|delete a lead|[deletealeadmobile](media/readmedocs/wireframes/mobile/deletealead.png)|
|PC|update a lead|[leadupdate](media/readmedocs/wireframes/leadupdate.png)|
|mobile|udpate a lead|[leadupdatemobile](media/readmedocs/wireframes/mobile/updateyourlead.png)|
|PC|udpate a profile|[updateprofile](media/readmedocs/wireframes/updateprofile.png)|
|mobile|update a profile|[updateprofilemobile](media/readmedocs/wireframes/mobile/updateyourprofile.png)|
|PC|delete a profile|[profiledelete](media/readmedocs/wireframes/profiledelete.png)|
|mobile|delete a profile|[profiledeletemobile](media/readmedocs/wireframes/mobile/profiledelete.png)|

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

|Name|link|function|comments|
|--|--|--|--|
|navbar|[link](media/readmedocs/features/navbar.png)|helps navigate a site|from bootstrap without additional changes|
|login button|[link](media/readmedocs/features/login button.png)|positiove button|this style of button is used trhu the page to confirm/submit positive actions|
|delete button|[link](media/readmedocs/features/delete button.png)|negative button|this style of button is used trhu the page to confirm negative actions|
|home button|[link](media/readmedocs/features/home button.png)|positive button|very similar to login button|
|hover|[link](media/readmedocs/features/hover.png)|hobvering effect|indicates a hover with the mouse over the button|
|success message|[link](media/readmedocs/features/successmessage.png)|signals postive actions|is used whener there is a positive action on a page|
|delete message|[link](media/readmedocs/features/info-deletemedia/readmedocs/features/info - delete message.pngmessage.png)|signals negative actions|is used whenever there is a negative action on a page|


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
* lead count
* reward input
* follow up feature

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
| File Name | link | Result | Comments |
|--|--|--|--|
|homepage|[link](media/readmedocs/html/homepage.png)|PASS||
|login|[link](media/readmedocs/html/login.png)|PASS||
|register|[link](media/readmedocs/html/register.png)|4 errors|all coming from django builtin form|

### CSS
| File Name | Link | Result | Comments |
|--|--|--|--|
|base|[link](media/readmedocs/css/base.png)|PASS||
|leads|[link](media/readmedocs/css/leads.png)|PASS||

### Python
| File Name | link | Result | Comments |
|--|--|--|--|
|leads views|[link](media/readmedocs/pep8/leads-views.png)|PASS||
|leads urls|[link](media/readmedocs/pep8/leads-urls.png)|PASS||
|leads forms|[link](media/readmedocs/pep8/leads-forms.png)|PASS||
|leads models|[link](media/readmedocs/pep8/leads-models.png)|PASS||
|members forms|[link](media/readmedocs/pep8/memebers-forms.png)|1 warning|trailing whitespace - could get rid of it even after many tries|
|members urls|[link](media/readmedocs/pep8/members-urls.png)|PASS||
|members views|[link](media/readmedocs/pep8/members-views.png)|PASS||

\
&nbsp;
[Back to Top](#table-of-contents)
\
&nbsp;

## Creadits
* [Simen Daehlin](https://github.com/Eventyret "Simen Daehlin") for advice and direction and continual support
* [Codemy.com](https://www.youtube.com/channel/UCFB0dxMudkws1q8w5NJEAmw "Codemy.com") for help on Django

\
&nbsp;
[Back to Top](#table-of-contents)
\
&nbsp;