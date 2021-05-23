init:
	pip install pipenv
	pipenv install --dev
test:
	python manage.py test -v2
static:
	python manage.py collectstatic --no-input
build_image:
	./push_image.sh
