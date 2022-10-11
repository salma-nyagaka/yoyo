[![Build Status](https://app.travis-ci.com/salma-nyagaka/yoyo.svg?branch=develop)](https://app.travis-ci.com/salma-nyagaka/yoyo)
[![Coverage Status](https://coveralls.io/repos/github/salma-nyagaka/yoyo/badge.svg?branch=develop)](https://coveralls.io/github/salma-nyagaka/yoyo?branch=develop)

### yoyo
#### Description
As an API user I want to get the minimum, maximum, average and median temperature for a
given city and period of time.

#### Development set up
-   Check that python 3.9.7 is installed:

    ```
    python --version
    >> Python 3.9.7
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

 #### Endpoints
| REQUEST | DESCRIPTION  | URL  |
| :-----: | :-: | :-: |
| GET | Get weather api data |  {{BASE_URL}}}}/api/locations/{{city}}/?days={{days}} |