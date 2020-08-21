# Initialization Instructions
_Before running the WiFiman, Provide your own machine's filepath to the WiFiman APK under the declaration of the app argument in test.py line 9._

# Project Notes
This project was created in pycharm with pytest as the default test runner under Settings -> Python Integrated Tools.

Line 47 in WiFiman.py deliberately breaks the while loop after proving tests can occur a minute apart so that the pytest can be marked as passed.

Mandatory tests are in test.py, optional tests are in test_optional.py.

# Testing History
The WiFiman APK was successfully tested using AVD Andoid emulator and test.py, but the selenium tests in test_optional.py could not be run due to technical difficulties with AVD on an AMD processor and troubles booting up after enabling Windows Hypervisor Platform. The selenium tests were coded to the best of my ability without the emulation option as a result.
