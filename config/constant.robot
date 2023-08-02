*** Settings ***
Library         Collections
Library         BuiltIn
Library         String
Library         OperatingSystem
Library         SeleniumLibrary
Library         C:/pythonProject_Study/lib/utils.py
#Variables       C:/pythonProject_Study/lib/utils.py
Resource        C:/pythonProject_Study/config/setup_conf.robot
Resource        C:/pythonProject_Study/keyword/ui_keywords.robot
#Python Libraries
#Python file access as variable
#robot file access as Resource