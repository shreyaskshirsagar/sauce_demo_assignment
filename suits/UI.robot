*** Settings ***
Resource    C:/pythonProject_Study/config/constant.robot

*** Test Cases ***
Verify Ui Login
    Ui Login    ${LOGIN_URL}    ${USER_NAME}    ${PASSWORD}
    sleep    3s

Verify Add To Cart
    Ui Login    ${LOGIN_URL}    ${USER_NAME}    ${PASSWORD}
    Add Single Item To Cart

Verify Remove From Cart
    Ui Login    ${LOGIN_URL}    ${USER_NAME}    ${PASSWORD}
    Add Single Item To Cart
    Remove Added Itme from Cart

Verify Checkout from cart step1
    Ui Login    ${LOGIN_URL}    ${USER_NAME}    ${PASSWORD}
    Add Single Item To Cart
    Checkout from cart page1

Verify Checkout from cart step2
    Ui Login    ${LOGIN_URL}    ${USER_NAME}    ${PASSWORD}
    Add Single Item To Cart
    Checkout from cart page1
    Checkout from cart page2

Verify Logout Functionality
    Ui Login    ${LOGIN_URL}    ${USER_NAME}    ${PASSWORD}
    Logout Functionality





    