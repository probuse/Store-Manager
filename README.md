# Store Manager

[![Build Status](https://travis-ci.org/myrdstom/Store-Manager.svg?branch=challenge-2)](https://travis-ci.org/myrdstom/Store-Manager)
[![Coverage Status](https://coveralls.io/repos/github/myrdstom/Store-Manager/badge.svg?branch=challenge-2)](https://coveralls.io/github/myrdstom/Store-Manager?branch=challenge-2)  

Store Manager is a web application that helps store owners manage sales and product inventory records. 
This application is meant for use in a single store.



## Setup

To setup,

1. Git

2. python 3.6 or higher

3. Install pip [here](https://pip.pypa.io/en/stable/installing/)

4. To setup the virtual environment ``` pip install virtualenv venv ```

5. To activate virtual environment ``` venv/scripts/activate ``` 

6. Install all dependencies in the ```requirements.txt``` to finalise setting up the environment.



## Build

1. Run the file run.py``` python run.py ``` in the root directory and follow  the prompts

2. Test all endpoints with [POSTMAN](https://www.getpostman.com/apps)

## Tests

1. pip install nose

2. Run ```nosetests --with-coverage --cover-package=app``` to run all tests with coverage


## The endpoints:
| End Point  | Description |
| ------------- | ------------- |
|GET /api/v1/products | Get all products
|POST /api/v1/products  | Post a new product
|GET /api/v1/products/<int:product_id> | Return a single product
|GET /api/v1/sales | Get all sales
|POST /api/v1/sales  | Post a new sale
|GET /api/v1/products/<int:sale_id> | Return a single sale


## Badges:


[![Build Status](https://travis-ci.org/myrdstom/Store-Manager.svg?branch=challenge-2)](https://travis-ci.org/myrdstom/Store-Manager)
[![Coverage Status](https://coveralls.io/repos/github/myrdstom/Store-Manager/badge.svg?branch=challenge-2)](https://coveralls.io/github/myrdstom/Store-Manager?branch=challenge-2)   


## Author
Paul Kayongo

