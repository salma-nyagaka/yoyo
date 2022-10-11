### yoyo

#### Description
As an API user I want to get the minimum, maximum, average and median temperature for a
given city and period of time.

#### Development set up
-   Check that python 3.10.0 is installed:

    ```
    python --version
    >> Python 3.10.0
    ```

-   Clone the repo and:

    ```
    git clone https://github.com/salma-nyagaka/yoyo.git
    ```

-   Change directories into the project folder by running:

    ```
    cd weatherapi
    ```

-   Create a virtual environment and activate it:

    ```
    virtualenv venv
    source venv/bin/activate
    ```

-   Install the dependencies:

    ```
    pip install -r requirements.txt
    ```

-   Run the tests:

    ```
    pytest
    ```

-   Start the server
    ```
    python manage.py runserver
    ```