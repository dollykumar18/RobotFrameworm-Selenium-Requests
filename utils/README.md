**Robotframework Selenium RequestLibray**

This repo has few examples how to use robotframework to automate UI and API interfaces.

To Use this locally

1. git clone https://github.com/dollykumar18/RobotFramework-Selenium-Requests.git
2. Open ENV file and change the base url to https://python-flask-apis.onrender.com/
3. Install Python and PiP
4. From RobotFramework-Selenium-Requests folder, run pip install -r requirements.txt
5. From RobotFramework-Selenium-Requests folder, rum robot -V env.py --outputdir reports/api_results tests/api_tests.robot

To run it as container

1. git clone https://github.com/dollykumar18/RobotFramework-Selenium-Requests.git
2. Open ENV file and change the base url to https://python-flask-apis.onrender.com/
3. From RobotFramework-Selenium-Requests folder, run docker build -t <image-name> .
4. docker run -i -t <docker-image-name>

