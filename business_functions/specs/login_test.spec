# Login spec
================

## Test Login
-----------
tags: positivetest, uitest

* Login to sauce demo page
* Enter "standard_user" and "secret_sauce"
* Click Login to sauce demo page
* Verify if the page got loaded successfully

## Test Login Invalid
---------------------
tags: negativetest, uitest

* Login to sauce demo page
* Enter "standard_user" and "secret_sauce1"
* Click Login to sauce demo page
* Verify if the page got loaded successfully