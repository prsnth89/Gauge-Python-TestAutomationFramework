# Gauge-Python-TestAutomationFramework

Install all the dependencies
pip install -r requirements.txt

To run gauge in sequential, open Terminal and give the following command
gauge run  --env='default' .\specs\

To run gauge in parallel, open Terminal and give the following command
gauge run --parallel -n4 --env='default' .\specs\

To run failed test case
gauge run --failed

Rerun failure with max iteration count
gauge run --max-retries-count=4

To generate flash report open browser and paste url

    Add port number in default env file (FLASH_SERVER_PORT=1443)
    Flash report URL - http://127.0.0.1:1443/



