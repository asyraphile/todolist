
# ToDoList App

This is a simple project given by Cognixus as a take-home assessment. The project objective is to produce API of todo list with OAuth. In this project, Google SSO is chosen for its simplicity and effectiveness. Thank you for the opportunity given because I learned so much from the take-home assessment.


## Instructions

- You need to have git and docker installed on your computer.
- Create a folder for this project. Run command prompt and nagivate to the project directory.
- Prompt "git init" and "git pull https://github.com/asyraphile/todolist master".
- Delete the venv folder and prompt "python -m venv venv" to install a new python virtual environment.
- After that, prompt ".\venv\Scripts\activate" to active the virtual environment.
- Now prompt "pip install -r requirements.txt" to install all the required packages.
- Last but not least, prompt "docker compose up -d" to create docker images and containerize the application.


## Testing the API

Actually there is one issue with this application, even though it has Google-SSO installed, there is no token for authorization yet due to the package I need to use is currently unavailable. Regardless of that, I still manage to ensure the API is working. Upon the completion of docker compose, you need to wait a few seconds to let the "web" services to run after mysql installation is complete.

Admin Login URL: http://localhost:8000/admin/
Admin Username: admin
Admin Password: admin

### Add Todo Item
- url: http://localhost:8000/add_item/?user_id={value}&title={value}
- keyword parameters: user_id, title
- Request Method: POST

### Delete Todo Item
- url: http://localhost:8000/delete_item/?task_id={value}
- keyword parameters: task_id
- Request Method: DELETE

### List All Todo Item
- url: http://localhost:8000/list_all/
- Request Method: GET

### Mark complete
- url: http://localhost:8000/mark_complete/<task_id>/
- parameters: task_id
- keyword parameters: complete -> the value is either 0 or 1 only.
- Request Method: PUT



## Author

- [@Asyraf](https://www.github.com/asyraphile)

