# django-flutter-todo
Django based desktop/mobile/web application.

## Instalation
- Install all python packages:

        $ pip install -r requirements.txt
- Migrate database:

        $ python manage.py migrate

## Run and usage
- To run app use todo django command:
    
        $ python manage.py todo
- To run server use --view parameter:
  
        $ python manage.py todo --view flet_app_hidden
- Compile ./frontend futter app to have separate ready to install application:

        $ cd frontend
        $ flutter run --dart-entrypoint-args http://94.23.247.130:8085
- You can use simple script to run separate flutter application:

        $ python run.py