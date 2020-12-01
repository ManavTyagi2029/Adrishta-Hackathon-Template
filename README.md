## Team Number \<Your Team Number> - \<Your Project Name>

Team 36 - I Voted ! 


### Project Overview

* With everything going online, why not the elections? And the major concern is security! As all elections are not such upscale like the college council elections, Disha Mamani, Vice President, College Council, wants to conduct the college council elections online and wants a secure platform to do so? She has the E-mail IDs of all the students  for any sort of communication. A solution is needed to her problem.

Here we are asked to make a college council election portal to conduct college council elections where the anonymity of the voter is maintained to the admin(which indicates security) knowing that the admin has the email IDs of all the students.

* Team 36 focused on a good user experience. It ensures that the voter does not vote twice.It allows administrator to add and remove candidate and have dynamic results.

### Solution Description

This project is mainly to help the colleges with college council elections since everything is going online. It’s a highly secured portal for college council elections(any other type of elections can also be hosted, but here talking of college council) where the anonymity of the voter is maintained to the admin. Here we have considered two positions who can login to the portal, an admin and a voter. The admin after logging in can add a new candidate, deleted an existing candidate and also check the results after voting. The voter after logging in can only vote for the standing positions, and once the voter completes their voting for all the positions among multiple candidates they automatically get logged out. And once a voter has logged in and voted they cannot re enter the portal and hence it provides more security. When the voter tries to re enter after voting once, in the url a message is shown “msg=Already+voted” For a candidate all their details i.e. name, email id, passport size photo, department, post for which they are standing and agenda are shown. These fields can only be entered by the admin while adding one candidate. All the details are shown to the voters for voting.

#### Architecture Diagram

 
 
 
 
 
 
 
 

#### Technical Description
* What technologies/versions were used
###Flask
###Inbuilt module SQLite3 database of Python using flask
###Python
###HTML
###CSS
###Javascript
###Sublime/Atom text editors

* Setup/Installations required to run the solution
 Pip install flask(and in that all the required dependencies come installed)
* Instructions to run the submitted code
py -m venv env
env\Scripts\activate
set FLASK_APP=app.py

### Screenshots











### Team Members
|Manav Tyagi | manav507@gmail.com|Frontend, Flowchart|
|Kritika Berry|kritikaberry@gmail.com|Backend and Documentation|
|Preeti Das|preetidas1609@gmail.com| Frontend, Presentation and Documentation|

### References
https://stackoverflow.com/
https://www.javatpoint.com/
https://www.tutorialspoint.com/sqlite/sqlite_create_database.htm
https://developer.mozilla.org/en-US/

