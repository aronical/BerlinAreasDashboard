# Berlin Areas Quality of Life


## Description

This tool visualizes datasets on Berlin's map and produces a score for each area based on the loaded datasets.


![image](https://user-images.githubusercontent.com/73293783/152703893-8cdbdb76-374a-4c54-b41d-91146a847249.png)


To start the dashboard, go to the directory src/main/python and run this code after installation of the requirements.txt:

python BerlinPop.py

Then visit http://127.0.0.1:8050/ in browser.

# UML Diagrams

Diagrams can be found in here: https://github.com/aronical/BerlinAreasDashboard/tree/main/docs/UML


# DDD - Domain Driven Design

The DDD-Diagram and the ubiquitous language description can be found in here: https://github.com/aronical/BerlinAreasDashboard/tree/main/docs/DDD

# Metrics

SonarCloud is chosen because of the easy GitHub integration. Aside from some smelly code, everything looks good.

[![Bugs](https://sonarcloud.io/api/project_badges/measure?project=aronical_BerlinAreasDashboard&metric=bugs)](https://sonarcloud.io/summary/new_code?id=aronical_BerlinAreasDashboard)

[![Code Smells](https://sonarcloud.io/api/project_badges/measure?project=aronical_BerlinAreasDashboard&metric=code_smells)](https://sonarcloud.io/summary/new_code?id=aronical_BerlinAreasDashboard)

[![Duplicated Lines (%)](https://sonarcloud.io/api/project_badges/measure?project=aronical_BerlinAreasDashboard&metric=duplicated_lines_density)](https://sonarcloud.io/summary/new_code?id=aronical_BerlinAreasDashboard)

[![Lines of Code](https://sonarcloud.io/api/project_badges/measure?project=aronical_BerlinAreasDashboard&metric=ncloc)](https://sonarcloud.io/summary/new_code?id=aronical_BerlinAreasDashboard)

[![Maintainability Rating](https://sonarcloud.io/api/project_badges/measure?project=aronical_BerlinAreasDashboard&metric=sqale_rating)](https://sonarcloud.io/summary/new_code?id=aronical_BerlinAreasDashboard)

[![Quality Gate Status](https://sonarcloud.io/api/project_badges/measure?project=aronical_BerlinAreasDashboard&metric=alert_status)](https://sonarcloud.io/summary/new_code?id=aronical_BerlinAreasDashboard)

[![Reliability Rating](https://sonarcloud.io/api/project_badges/measure?project=aronical_BerlinAreasDashboard&metric=reliability_rating)](https://sonarcloud.io/summary/new_code?id=aronical_BerlinAreasDashboard)

[![Security Rating](https://sonarcloud.io/api/project_badges/measure?project=aronical_BerlinAreasDashboard&metric=security_rating)](https://sonarcloud.io/summary/new_code?id=aronical_BerlinAreasDashboard)

[![Technical Debt](https://sonarcloud.io/api/project_badges/measure?project=aronical_BerlinAreasDashboard&metric=sqale_index)](https://sonarcloud.io/summary/new_code?id=aronical_BerlinAreasDashboard)

[![Vulnerabilities](https://sonarcloud.io/api/project_badges/measure?project=aronical_BerlinAreasDashboard&metric=vulnerabilities)](https://sonarcloud.io/summary/new_code?id=aronical_BerlinAreasDashboard)

# Clean Code Development:

The Clean Code Cheet Sheet with code snippets as example from my code can be found in [here](https://github.com/aronical/BerlinAreasDashboard/blob/main/docs/CleanCode_Cheat.jpg).

# Build Management

The Build Management files can be found in [here](https://github.com/aronical/BerlinAreasDashboard/tree/main/src/main/python):

    build.py 
    setup.py 
    pyproject.toml 


# Unit-Tests

The Unit-Tests can be found in here: 


The Unit-Test package used in my code is the built-in module unittest. The modules for which a test-code is written are the 'budget.py', 'expense.py', 'help_functions.py' and 'viewer.py'. All of them except the 'help_functions.py' represent the core domains in the ExpenseTracker. The 'help_functions.py' represents functions which are often used in the whole application and are shared between the core domains. The tests get automatically started and are integrated in the build management.


# Continuous Delivery

I used Github Actions for building a CD pipeline. [Here](https://github.com/aronical/BerlinAreasDashboard/blob/main/docs/CD_Success.png) is the successful run.

The pipeline for the continuous delivery can be found in [here](https://github.com/aronical/BerlinAreasDashboard/blob/main/.github/workflows/python-app.yml). 

 

# IDE

My go-to IDE was Microsoft Visual Studio Code. I chose it mainly due to the simplicity and speed of it. It seemed to load projects way faster than PyCharm, which is a plus for my non-patient self. Besides I found a color palette that I liked. The project is done in Python 3.9.0. I was able to easily integrate my GitHub to it and choose needed environment.

My most-used shortcuts were:

CTRL + F5: Run without debugging

CTRL + SHIFT + F5: Restart run

CTRL + S: :)


# DSL-Demo

I made a simple expense tracker. Here is a link to the DSL file I created: https://github.com/aronical/BerlinAreasDashboard/blob/main/src/main/python/dsl_int.py


# Functional Programming

The functional programming aspects and its examples can be found in here: https://github.com/FelixLehn/ExpenseTracker/blob/main/docs/Functional_Programming/FP_Aspects.md
