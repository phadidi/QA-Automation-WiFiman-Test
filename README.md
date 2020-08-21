# Initialization Instructions
_Before running the WiFiman, Provide your own machine's filepath to the WiFiman APK under the declaration of the app argument in test.py line 9._

# Project Notes
This project was created in pycharm with pytest as the default test runner under Settings -> Python Integrated Tools.

Line 47 in WiFiman.py deliberately breaks the while loop after proving tests can occur a minute apart so that the pytest can be marked as passed.

Mandatory tests are in test.py, optional tests are in test_optional.py.

# Testing History
The WiFiman APK was successfully tested using AVD Andoid emulator and test.py, but the official plot of the movie appears to have changed from

_Tenet is an upcoming spy film written, produced, and directed by Christopher Nolan. It is a co-production between the United Kingdom and United States, and stars John David Washington, Robert Pattinson, Elizabeth Debicki, Dimple Kapadia, Michael Caine, and Kenneth Branagh._

to

_Tenet is an upcoming spy film written and directed by Christopher Nolan, **who produced it with Emma Thomas. A** co-production between the United Kingdom and United States, it stars John David Washington, Robert Pattinson, Elizabeth Debicki, Dimple Kapadia, Michael Caine, and Kenneth Branagh._

Therefore, I could not assert the plot matches the original requirements given to me for the test although I was able to successfully retrieve the new plot element in its place.
