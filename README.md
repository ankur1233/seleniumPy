# seleniumPy

##Run using CLI 

report 1: pytest-html
pytest tests\myStore\test_checkout_product.py --browser chrome --url http://automationpractice.com/index.php --html=reports/report.html

report 2 : pytest-html1 .. edit index.html to stop warning 
pytest test_checkout_product.py --browser chrome --url http://automationpractice.com/index.php --template=html1/index.html --report=./report/report.html

report 3: pytest-html-reporter
pytest test_checkout_product.py --browser chrome --url http://automationpractice.com/index.php --html-report=./report/report.html


## Run on Pycharm 
I do Run -> Edit Configurations... Then click the + in the upper left of the modal dialog. Select "python tests" -> py.test Then I give it a name like "All test with py.test"

I select Target: module name and put in the module where my tests are (that is 'tests' for me) or the module where all my code is if my tests are mixed in with my code. This was tripping me up.

I set the Python interpreter.

I set the working directory to the project directory.

Add argument like --browser chrome , --url https://xyz.com  to Additional Argument section [Pytest Edit]