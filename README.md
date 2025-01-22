# Gauge-Python-TestAutomationFramework

Install all the dependencies
pip install -r requirements.txt

This has two parts
framework and business functions
framework- contains all the resuable libraries, it supports multiple tools -playwright, selenium, mobile emulator, api etc.,

business functions- all the application specific tests are written inside this, internally it use the framework and helps in designing testcase easily and effectively with less maintenance

hooks - precondition/postcondition to run the test
pageobjects-locators will be mentioned based on each page
page-contains application specific functions which helps to design testcase
specs-helps to design test case in simple english
step_impl-all the tests written in specs will be converted into logic via step implmentation
env-default- all configurations were managed in this file
             

To run gauge in sequential, open Terminal and give the following command
gauge run  --env='default' .\specs\

To run gauge in parallel, open Terminal and give the following command
gauge run --parallel -n4 --env='default' .\specs\

To run failed test case
gauge run --failed

To run test case based on tags
gauge run .\business_functions\specs_api --tags positivetest

Rerun failure with max iteration count
gauge run --max-retries-count=4

To generate flash report open browser and paste url

    Add port number in default env file (FLASH_SERVER_PORT=1443)
    Flash report URL - http://127.0.0.1:1443/

To run performance test execute below powershell
 .\framework\perf_test\run_perf.ps1


Framework Flow chart

To record playwright in python
playwright codegen --target python https://example.com

To record in specific browser
playwright codegen --browser=firefox --target=python https://example.com

Automatically run pipeline whenever new commit happens

