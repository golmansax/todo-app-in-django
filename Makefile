.PHONY: pylint

pylint:
	pylint --load-plugins pylint_django manage.py todo_app todos
