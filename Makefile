setup: hello_world/requirements.txt
	pip3 install -r hello_world/requirements.txt

run:
	pycodestyle .\hello_world\app.py
	black .\hello_world\app.py
	isort .\hello_world\app.py