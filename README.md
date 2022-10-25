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

-   Clone the repo:

    ```
    git clone https://github.com/salma-nyagaka/yoyo.git
    ```

-   Access the project folder by running:

    ```
    cd weatherapi
    ```

-   Install **pip** first

    ```
    sudo apt-get install python3-pip
    ```

-   Then install **virtualenv** using pip3

    ```
     sudo pip3 install virtualenv 
    ```

-   Create a virtual environment and activate it:

    ```
    virtualenv venv
    source venv/bin/activate
    ```

- Create a .env file on the root directory
    ```
     touch .env
    ```

- Add the following keys in your .env file
    ```
    SECRET_KEY='stz-6*!-!vri1n$@hmx1h_n=o^gj$aj=mzzov@vc&6#(!=v6s9'
    API_KEY='0873153d0367435db6a113510221010'
    ```


-   Install the dependencies:

    ```
    pip install -r requirements.txt
    ```

-   Run the tests:

    ```
    pytest
    ```

-   Start the server to access the endpoint below
    ```
    python manage.py runserver
    ```

 #### Endpoint
| REQUEST | DESCRIPTION  | URL  |
| :-----: | :-: | :-: |
| GET | Get weather api data |  {{BASE_URL}}}}/api/locations/{{city}}/?days={{days}} |