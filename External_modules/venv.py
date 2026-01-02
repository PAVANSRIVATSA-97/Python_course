''' Virtual environment in oython is completely different from the global pyhton environment. It is used for projects that requre special libraries or certain versions of libraries/modules thatare diffeent from the global environment.
pip install virtualenv  -- Install virtual environment.
python -m venv tutorial-env -- creating vir env named tutorial-env and 
.\tutorial-env\Scripts\Activate.ps1 -- activate the env
deactivate -- deactivate the enivironment
You can install the packeges in the env as usual like "pip install pandas"
pip list -- lists all the installed libraries
pip ininstall pandas -- uninstalls the pandas library
pip freeze -- it gives all the libraries with their versions
pip freeze > requirements.txt -- creates a text file having all the packages with their versions. this is useful when you want to twll others that these are all the packages required to run you your project.
pip install -r .\requirements.txt -- installs the packages that are in requirements.txt
'''