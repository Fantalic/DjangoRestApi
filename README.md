# Code Challange Task: simple REST-API with Pyhton

Task:


Objective	Develop a read-only web API which provides specific energy yields (kWh/kWp/year) of photovoltaic systems in Germany. 
Technology setup	
- Python 3
- Pipenv (or similar tools)
- Django 
- Django Rest Framework
- Heroku (free plan)

Minimal viable product	The API provides one value per federal state. Example for bavaria:
Request:
https://<APPNAME>.herokuapp.com/api/pv_yield?state=by
Response: 
{“yield”: 1100, “state”: “by”}

Optional feature	
The API provides the yield of a PV system (kWh/year) if the installed capacity (in kWp) is provided:
Request:
https://<APPNAME>.herokuapp.com/api/pv_yield?plz=07349&capacity=10
Response: 
{“yield”: 11000, “plz”: “by”}

Note: The calculation is done by a multiplication of the specific yield with the capacity.
Hints:	The focus is on the API, not the exact figures. You can roughly estimate the specific energy yield per federal state from the map below.
Look for tutorials on how to deploy a Django app on heroku and set up the local and production environment first.
Django Rest Tutorial (https://www.django-rest-framework.org/tutorial/quickstart/)
Make use of ViewSets (https://www.django-rest-framework.org/api-guide/viewsets/#api-reference) 
Make use of DjangoFilterBackend (https://www.django-rest-framework.org/api-guide/filtering/#djangofilterbackend) 
