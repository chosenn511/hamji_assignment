# Hamji

Welcome to Tridge sandbox project!

We'd love to collaborate with amazing developers as we drive the development of "Global Sourcing Hub of Food & Agriculture" into the future.

## Guidelines
- Setup project on your local computer
- Achieve TODO items one by one
- Mark an item as done in the TODO list
    - [x] Like this
- After completion, please send it in a zip file


## Setup
- Install PIP packages
```
pip install -r requirements.txt
```
- Run server
```
python manage.py runserver
```
- Now that the server’s running, visit http://127.0.0.1:8000/polls/ with your Web browser


## TODO
1.  [ ] Raise 404 if no matching question
2.  [ ] Show only questions that are published and not yet closed
3.  [ ] Enable to comment on question
4.  [ ] Enable to comment on comment
5.  [ ] Enable to suggest new choice for question
6.  [ ] Limit the number of choices that can be suggested on one question
7.  [ ] Extends `Question.closed_at` by one day, when new choice is suggested for that question
     - Requirements:
         - Use Django signal/receiver system
8.  [ ] In `/polls/`, fetch only 5 questions through REST API
9.  [ ] Handle race condition on handling "vote" action
10. [ ] Implement login system
11. [ ] Implement system that a question creator can approve suggested choices
12. [ ] Implement global search for questions and choices

