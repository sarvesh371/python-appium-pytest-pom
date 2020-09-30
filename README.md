# python-appium-pytest-pom-
This is a framework repo for automating mobile application using python with pytest and pom framework

**Pre Requisites**
1. Before starting the tests install dependencies and appium using the official documentation here : https://github.com/appium/appium

**Setup the framework and requirements and execute Test**
1. Run venv_setup.sh if you are mac or change the commands according to your os for setting up venv and downloading packages
    
    `sh venv_setup.sh`

2. Select the interpreter by going into preferences 
3. Run test using pytest command and tests directory

    ` pytest tests`

**Project Structure**
1. base - It contains all the web/appium drivers, common functions and workers functions
2. resources - It contains all the apk's and url configurations which will be used throughout the project
3. pages - It contains all the pages class and their methods to implement POM
4. tests - It contains all the flow class and their calling functions using pytest
5. screenshots - We will store all our screenshots in this folder
6. allure_results - folder to save our allure report
    
    a. run `allure serve` to get the allure report on localhost
    
    b. run `allure generate` to generate a allure report and it will be saved under /allure-report

7. conftest - as it is heart of pytest, we will keep only fixture and pytest methods there
8. requirements.txt - we will write all our dependency there and then download in one shot using `venv_setup.sh`