docker-compose exec web python manage.py createsuperuser

docker-compose exec web python manage.py makemigrations library_app

docker-compose exec web python manage.py createsuperuser