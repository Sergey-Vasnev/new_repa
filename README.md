# Testing Authentication and Feedback forms for Altoro Mutual

Testing Authentication and Feedback with Pytest and Silenium Using BaseObject and Factors Patterns.

## Installing

These instructions will get you a copy of the project up and running on your local machine for development and testing purposes.<br>
For this project, you will need Python, the Selenium and Pytest libraries.<br>
You can install the latest Python version from the official website, libraries can be installed using these commands:

```
pip install pytest
pip install Selenium
```
There is also a requirements.txt.

### Running the tests

To start tests enter the following command in the terminal:
```
pytest
```
When you will receive the results of the test run, they will look like this:
![image](https://user-images.githubusercontent.com/93818945/218304697-63c74f55-7490-43a0-a1d9-e1959fb4755d.png)
Also, all information about the tests will be saved in a file log_for_test.log:
![image](https://user-images.githubusercontent.com/93818945/218304719-0b5d24b6-ae6e-468d-82ef-d65e94b51e0e.png)

## Description
In the sign-in section of the Altoro Mutual website we can find an authorization form.<br>
Following tests were created:
<ol>
<li>a test with input of valid data,</li>
<li>a test with input of invalid data,</li>
<li>a test with input of only one field (with a username, in our case).</li>
</ol>
The last one should trigger JavaScript alert.

![image](https://user-images.githubusercontent.com/93818945/208936548-df8285b1-455f-4b53-b6fe-492c35c2830a.png)

In the feedback section of the Altoro Mutual website we can find a feedback form.<br>
Following tests were created:
<ol>
<li>a test with input of only one field (with a name, in our case).</li>
</ol>

The test uses a pattern PageObject, so:
<ul>
<li>The class BaseElement is an abstract class which contains methods to interact with elements on the page (searching for elements, clicking on the elements for example). </li>
<li>The class BasePage is an abstract class which contains methods to interact with the page (checking whether page is open, for example),</li>
<li>The class Browser contains methods for interaction with the browser (go to site with specifed url, or refresh the page),</li>
<li>The class Driver is a BrowserFactory which provide different options for different browsers (Firefox or Chrome),</li>
<li>The conftest.py contains a fixture to launch and quit the browser,</li>
<li>The Singleton contains Singletone for the Browser.</li>
</ul>

