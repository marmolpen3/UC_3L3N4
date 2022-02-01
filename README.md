# UC_3L3N4

Test application. The intention is to store the results of the users for each challenge purpose. After that, you can get all the information about the final results like a list with all the marks of all the users, only the results of a user or the user with the best and the worst mark.

Here you can see the first class model:
![model](https://user-images.githubusercontent.com/44238816/151700130-0980dad6-626e-4b8f-8bc2-59cd5f974121.jpg)

---

To run the code, you need to do some configuration. First of all, you need to create a virtual environment to download all the dependencies of the project. I recommend you to create a folder to add the virtualenv and download the project from GitHub. You can follow these steps:

1.  Create a workspace for this project.

    ```sh
    mkdir workspace_uc
    ```

2.  Create a virtual environment.

    ```sh
    python3 -m venv uc
    ```

3.  Clone the project, open with vscode or similar IDE and open a terminal.

    ```sh
    git clone https://github.com/marmolpen3/UC_3L3N4.git
    ```

5.  Activate the virtualenv.

    ```sh
    source ../uc/bin/activate
    ```

6.  Download all the dependencies.

    ```sh
    pip install -r requirements.txt
    ```

7.  Create an `.env` file with the following content.

    ```text
    SECRET_KEY = 'SECRET'
    ```

8.  Do the migrations.

    ```sh
    python manage.py migrate
    ```

9.  Run the server.

    ```sh
    python manage.py runserver
    ```
