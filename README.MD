Thanks for checking out my code! This could have been a single file app but I designed it with modularity and scalability in mind, which is why the project structure might seem excessive for such a small project. The "meat"
of the application is in all the files called item.py. These files are self-contained and could easily be transferred into an existing REST framework. 

### to run ####
clone the repo
python3 -m venv env (optional, but preferable if you don't want extra packages on your main system)
pip install -r requirements.txt
python3 wsgi.py