# Activity Period API

A REST API to get a list of Users and their Activity Periods.

Live at https://activityperiodapi.herokuapp.com/api/users
Hosted Using Heroku, PostgreSQL.

### Cloning The Repo

Clone the repository using the command

`git clone https://github.com/roopeshvs/ActivityPeriodAPI.git`

### Creating A Python Virtual Environment

For Linux, use
`python3 -m venv APAPI`

For Windows, use
`python -m venv APAPI`

### Activating The Python Virtual Environment

For Linux Bash, use
`APAPI/bin/activate`

For Windows Command Prompt, use
`APAPI\Scripts\activate.bat`

### Installing Dependencies

Install the required dependencies by running the command,
`pip install -r requirements.txt`

### Setting Up

In settings, configure the Secret Key and Database.

Set Up Your Database Tables by running the commands

`python manage.py makemigrations`

`python manage.py migrate`

### Populating The Database

Two custom commands have been set up to populate.

Populate the Users table using the command

`python manage.py populate_users --path users.yaml`

Populate the ActivityPeriod table using the command

`python manage.py populate_activity_periods --path activity_periods.yaml`

You can choose to add or edit the contents to be populated by editing the users.yaml and activity_periods.yaml file.

### You Are All Set

Run using the command

`python manage.py runserver`

or 

`python3 manage.py runserver`

Now you can access the API endpoint at http://localhost:8000/api/users/