.PHONY: flake8 pylint

flake8:
	flake8 manage.py todo_app

pylint:
	pylint --load-plugins pylint_django manage.py todo_app todos
