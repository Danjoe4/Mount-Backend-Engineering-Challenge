Thanks for checking out my code! This could have been a single file app but I designed it with a specific architectural pattern and scalability in mind, which is why the project structure is rather complex for a rather simple app. The meat of the application is in all the files called item.py. These files are self-contained and could easily be transferred into an existing REST framework. 

I was explicit with the HTTP response to showcase that I understand the importance of status codes, but depending on the style for a specific application I may have left them implicit. I didn't use type hints and would do so if the rest of application did, consistency is key for readability. I use NameError quite a bit, throwing an error could be useful for logging, if we're failing API calls we might want to know, but a different type of error or custom error may be more appropriate. I used a json file instead of a database because a db might require some extra configuration on your end which would be a hassle. 

A note on testing, the design choice is highly workflow dependent. For more robust testing, I'd leave the tests outside the application, then deploy the app to a docker container or staging server and test it there with real API calls. I bundled my tests with the app and used pytest-mock because it was straighforward and easy to use. 

### to run ####
clone the repo
python3 -m venv env (optional, but preferable if you don't want extra packages on your main system)
pip install -r requirements.txt
python3 wsgi.py