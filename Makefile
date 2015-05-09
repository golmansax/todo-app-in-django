.PHONY: pylint

pylint:
	pylint --load-plugins pylint_django manage.py my_project todos
