Set-ExecutionPolicy RemoteSigned


# Define the path to your Locust test script
$locustTestScript = ".\framework\perf_test\test_locust.py"

# Define the host URL
$hostUrl = "http://localhost:5000"

# Run the Locust test using the locust command
locust -f $locustTestScript --host $hostUrl

# Open a web browser after starting the Locust test
Start-Process "http://localhost:8089" 