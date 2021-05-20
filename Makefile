init:
	pip install pipenv
	pipenv install --dev
test:
	pipenv run python manage.py test -v2
build_image:
	./push_image.sh
