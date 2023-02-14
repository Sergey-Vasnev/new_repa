# Testing Authentication for Altoro Mutual

Testing Authentication with Pytest and Silenium Using BaseObject and Factors Patterns.

## Installing

These instructions will get you a copy of the project up and running on your local machine for development and testing purposes.<br>
For this project, you will need Python, the Selenium and Pytest libraries.<br>
You can install the latest Python version from the official website, libraries can be installed using these commands:

```
pip install pytest
pip install Selenium
```
### Running the tests

To start tests enter the following command in the terminal:
```
pytest main.py
```
When you will receive the results of the test run, they will look like this:
![image](https://user-images.githubusercontent.com/93818945/208954742-1687b47d-8014-4529-904b-011495c3251c.png)
If you want to see more information, you can add a flag "-v" to a command in the terminal:
```
pytest -v main.py
```
![image](https://user-images.githubusercontent.com/93818945/208955120-95d902e8-2ecb-4f35-b25c-f61490735887.png)

## Description
In the sign-in section of the Altoro Mutual website we can find an authorization form. The task is to conduct several tests for this form.<br>
Therefore, three tests were created:
<ol>
<li>a test with input of valid data,</li>
<li>a test with input of invalid data,</li>
<li>a test with input of only one field (with a username, in our case).</li>
</ol>
The last one should trigger JavaScript alert.

![image](https://user-images.githubusercontent.com/93818945/208936548-df8285b1-455f-4b53-b6fe-492c35c2830a.png)

The test uses a pattern PageObject, so:
<ul>
<li>The class Locators from PageObject.py contains username,password fields and submit button locators. </li>
<li>The class AuthForm from PageObject.py contains functions for finding locators from class Locators and interacting with them.</li>
<li>The class BasePage from page.py contains functions for interaction with the browser.</li>
<li>The conftest.py contains a fixture to launch and quit the browser.</li>
<li>The class Factory from actions.py represents the user actions and and determines the behavior of the program.</li>
<li>The main.py contains the tests that are carried out.</li>
</ul>
Factory class result depends on the number of introduced variables: 
<ol>
<li>If both variables are entered, the function checks whether the url has changed from the login page to the welcome page or not.</li>
<li>If a single variable is entered, the function returns a variable that contains data about the occurrence of a warning.</li>
</ol>

[**Yuliya Mirko**](https://github.com/SirPelmesh)
