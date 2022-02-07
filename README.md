## Berlin Areas Quality of Life


# Description

This tool visualizes datasets on Berlin's map and produces a score for each area based on the loaded datasets.


![image](https://user-images.githubusercontent.com/73293783/152703893-8cdbdb76-374a-4c54-b41d-91146a847249.png)


To start the dashboard, go to the directory src/main/python and run this code after installation of the requirements.txt:

python BerlinPop.py

Then visit http://127.0.0.1:8050/ in browser.

# UML Diagrams

Diagrams can be found in here: https://github.com/aronical/BerlinAreasDashboard/tree/main/docs/UML


# DDD - Domain Driven Design

The DDD-Diagram and the description can be found in here: https://github.com/aronical/BerlinAreasDashboard/tree/main/docs/DDD

# Metrics

SonarCloud is chosen because of the easy GitHub integration. Aside from some smelly code, everything looks good. Metrics screenshot can be found in here: https://github.com/aronical/BerlinAreasDashboard/blob/main/docs/Metrics_SonarCloud.png


# Clean Code Development:

The Clean Code Cheet Sheet with code snippets as example from the code can be found in here: 

# Build Management

The Build Management files can be found in [here](https://github.com/aronical/BerlinAreasDashboard/tree/main/src/main/python):

    build.py 
    setup.py 
    pyproject.toml 


# Unit-Tests

The Unit-Tests can be found in here: 


The Unit-Test package used in my code is the built-in module unittest. The modules for which a test-code is written are the 'budget.py', 'expense.py', 'help_functions.py' and 'viewer.py'. All of them except the 'help_functions.py' represent the core domains in the ExpenseTracker. The 'help_functions.py' represents functions which are often used in the whole application and are shared between the core domains. The tests get automatically started and are integrated in the build management.


# Continuous Delivery

The pipeline for the continoues delivery can be found in here: 


The CD-pipeline is built with Github Actions. The tasks to be done are:

    set up ubuntu environment
    set up Python with Version 3.8
    installs or upgrades pip
    installs or upgrades flake8
    installs (if provided) the requirements.txt
    checks if there are syntax errors in python
    runs the Unit-Tests

# IDE

My go-to IDE was Microsoft Visual Studio Code. I chose it mainly due to the simplicity and speed of it. It seemed to load projects faster than PyCharm. The project is done in Python 3.9.0. I was able to easily integrate my GitHub to it and choose needed environment.

My most-used shortcuts were:

CTRL + F5: Running without debugging
CTRL + SHIFT + F5: Restart run
CTRL + S: :)


# DSL-Demo

The DSL-Demo can be found in here: https://github.com/FelixLehn/ExpenseTracker/blob/main/src/main/python/dsl_example.py It uses the predefined Budget Class from the ExpenseTracker.

# Functional Programming

The functional programming aspects and its examples can be found in here: https://github.com/FelixLehn/ExpenseTracker/blob/main/docs/Functional_Programming/FP_Aspects.md
