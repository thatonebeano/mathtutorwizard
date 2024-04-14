# Math Tutor Wizard   

This is a web application that utalizes generative AI in order to pose simple math equation questions for elementary school students. Upon correctly or incorrectly answering the question, the following question will be of an increased or decreased difficulty respectively.    

## Table of Contents   

* [Introduction](#introduction)   
* [Requirements](#requirements)   
* [Installation](#installation)   
* [Usage](#usage)   
* [Limitations](#limitations)   
* [License](#license)  

### Introduction   

Generative AI often gets a bad rap in regard to its use in public and postsecondary education due to the prevalant misuse of tools such as ChatGPT for things such as quick essay writing and problem solving. While I believe these to be problems as well, I think that GenAI offers more positives than negatives within the education field. Instead of using AI as an ends to a means for solving a problem and moving on, what if it was used as a tool to improve our skills in the problem solving phase altogether, while also educating the newest generations on how to properly use AI in order to foster a healthy relationship with the technology from a young age? This is the inspiration behind the 'Math Tutor Wizard'.   

This app is in a very early and rudimentary stage. Problems in development and future plans are stated in the Limitations section of the readme.   

### Requirements   

The Math Tutor Wizard web application is designed to be used with Python, Flask, and OpenAI's Chat API.   

### Installation   

This installation guide will assume that you already have Python installed. As Flask and the OpenAI library are also required for this app, they can be installed through your terminal with...   

`pip install flask`   

and   

`pip install --upgrade openai`   

Lastly, you are going to have to create and configure your OpenAI API key. This can be done by creating an OpenAI account, navigating to the "API Keys" section, generating a new secret key, and then copying the key string. You'll then have to set your key as an Environment Variable on your device so that you can connect to the OpenAI API when running the app. On Windows this can be done by navigating to the 'Environment Variables' section of 'Advanced System Settings'. Just enter 'OPENAI_API_KEY' as the variable name, and the key as the variable value.   

Once all of the requirements have been met, you can launch the Flask app by navigating to the root of the app in your terminal and typing...   

`python -m flask --app app run`   

### Usage   

The REB App is comprised of the following...   
  
- app.py   
- init_db.py   
- db_test.py    
- static    
    1. styles.css     
    2. wizard.png    
    3. background.jpg    
- templates      
    1. base.html   
    2. initial.html   
    3. question.html   
- database.db   
- schema.sql    
- requirements.txt   
- LICENSE  

###### app.py

This Python script is main component of the app. When ran, it will import all of the necessary modules from Flask, OpenAI, and SQLite used within the script so that it will run correctly. There are two app routes, one for when the web app is first accessed, and another for once the first initial prompt is submitted in the form section. The first route is the root of the app and uses the design of 'initial.html'. The user is prompted to input what grade they are in and what difficulty math question they would like into the form, where upon submitting their info the app makes a POST request to the OpenAI Chat API where the system has been given a prompt about their role as a math tutor and that they will provide math questions suitable for the asked difficulty. Upon receiving a question from ChatGPT, the app will redirect to the 'question.html' page and display the question to the user. The user then inputs the given question and their answer into the form where the app will follow its other route. Upon submission, another POST request is made, and ChatGPT will determine whether the answer is correct. If it is, the response will congratulate the user and give them a slightly harder question. If it is incorrect, the response will give the user a slightly easier question. For both outcomes, the 'question.html' template is rendered once again, and this loop will continue until the user exits the app.   

The app also records all initial user prompts, AI questions, and user answers in a local SQLite database file. This is done any time a POST request is made.    

###### database.db   

A database file for a very basic SQLite database used to record user and system questions and responses.    

###### scheme.sql   

An SQL file detailing the schema used for the creation of the local database file, and what information will be present in the table.   

###### init_db.py   

A Python script used to initially create a database file with the required table for prompt and answer information from the app. It can also be used to refresh the database and start from blank.   

###### db_test.py   

A simple Python script that can be run in Terminal to fetch and print all entries present in the app's database file.   

###### static   

A folder that consists of three files that relate to the visual design of the web app and are used with the HTML files. Files are 'background.jpg', 'wizard.png', and 'styles.css'.   

###### templates   

A folder that consists of two HTML files used for the page design and structure of the web app. Flask utalizes HTML files as 'Templates' and is able to render them in ways that expand on normal HTML capabilities. Files are 'initial.html', and 'question.html'.    

###### requirements.txt   

A simple text file which conveys what software and minimum supported versions are required to run the app.   

###### LICENSE   

A simple document file which contains license, copyright, and use information.  

### Limitations   

While this app was really fun to make, it is currently in a very basic and janky state. I could not find out a way to implement an on-going conversation between the user and the AI, and because of this, the user has to input the question as well as their answer into their response since the system does not remember the question they asked. I feel like this could be solved by using another Python script specifically for chat completions? Having the database entries of the AI's responses fed back to it each time? I don't know, but more learning online once the semester is over is in my plans because this sort of problem solving is so fun and satisfying.    

Also, currently the database schema being used is pretty basic just as a means of recording inputted and outputted text from the app. In theory I would like to be able to connect an individual's prompts and answers to their own unique "TutorID", so that their knowledge level and progress would not only be able to be measured, but more importantly so that the questions asked to them would be at the perfect level of difficulty that challenges them enough to learn, but not hard enough to discourage. If this information was recorded and accessible, the AI Chat prompt could be improved and expanded upon to ask questions of a dynamic difficulty that relates to their strengths and weaknesses.    

### Credits   

The intial inspiration for this app, as well as a large portion of the code and syntax, is taken from Colin Conrad's 'SnapTutor' Flask application (cdconrad).   

### License   

This project is licensed under the [MIT License](LICENSE). Copyright (c) 2024 Ben Forsyth. Full permissions viewable in the provided 'LICENSE' document file.    
