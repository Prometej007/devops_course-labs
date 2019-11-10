.DEFAULT_GOAL := all

all: install test run deploy

install:
	@echo "Installing pipenv and dependencies."
	@apt install -y python3.7
	@apt install -y python-pip
	@apt install -y python3-pip
	@pip install pipenv
	@pipenv --python 3.7
	@pipenv install requests
	@pipenv install ntplib
	@pipenv install pytest

test:
	@pipenv run pytest tests.py | tee results.txt

run:
	@echo "Run Python app."
	@pipenv run python app.py | tee -a results.txt

deploy:
	@echo "Adding and Committing results.txt to git."
	@git add results.txt
	@git commit -m "Auto push file"
	@git push origin master
