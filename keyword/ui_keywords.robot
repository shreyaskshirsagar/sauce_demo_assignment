*** Settings ***
Documentation    This file is for all ui related keywords

*** Keywords ***
Ui Login
    [Documentation]     Verify UI login
    [Arguments]    ${URL}    ${USER_NAME}    ${PASSWORD}
    Login To Ui    ${URL}    ${USER_NAME}    ${PASSWORD}

Add Single Item To Cart
    [Documentation]     Verify add to cart functionality
    Add Bike Light To Cart

Remove Added Itme from Cart
    [Documentation]    Verify remove from cart functionality
    Remove Added Bike Light To Cart

Checkout From Cart Page1
    [Documentation]    Verify checkout functionality
    Check Out Step One

Checkout From Cart Page2
    [Documentation]    Verify price and tax at the time of checkout
    Check Out Step Two

Logout Functionality
    [Documentation]    Verify logout functionality
    Logout From Cart
