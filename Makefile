.PHONY: flake8 pylint coverage

coverage:
	coverage run --source='.' manage.py test || true
	coverage report --fail-under=50

flake8:
	flake8 manage.py todo_app

pylint:
	pylint --load-plugins pylint_django manage.py todo_app
