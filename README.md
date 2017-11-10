A djano app for showing database queries statistics


> Profiling requests is done by adding a middlware which save data in RequestProfile
> Average value show in site.
> For popultaing db craete super user and sign in to django admin and refresh pages several times

--------------------------------------------------------
--------------------------------------------------------
--------------------------------------------------------

sample output:

![alt text](https://raw.githubusercontent.com/beheshtraya/django-performance-view/master/screenshot.png)


How to run:

	- $: pip install -r requirements.txt
	- $: python manage.py makemigrations
	- $: python manage.py migrate
	- $: python manage.py createsuperuser (optional: for managing tickets in django admin)
	- $: python manage.py runserver 127.0.0.1:7000
		
				
--------------------------------------------------------
--------------------------------------------------------
--------------------------------------------------------
		
		
Additional Info:

	tested on:
		- OS: Windows 10
		- Interpreter: Python 3.5.2
		- Web framework: Django 1.10
		- Database: Sqlite
		
--------------------------------------------------------
--------------------------------------------------------
--------------------------------------------------------

Future works:

	- Add other parameter
	
	

