# Gagarain backend  

[Django rest framework](https://www.django-rest-framework.org/) is used for Authorization, Authentication and User management.  

## How to run  

Backend is hosted on heroku: [GagarianRest](https://gagarianrest.herokuapp.com/ "https://gagarianrest.herokuapp.com/")  


### `docker-compose up`  
    
Runs django server on local machine at http://0.0.0.0:8000/  
*Requires docker-compose*  
  
If you don't have docker  
### `python manage.py runserver`  
    
*first install all requirements using* `pip install -r requirements.txt`  
Change:  
'NAME': 'd67kqbq6hnmd66'  
'USER': 'igzqcxmdmlmblc'  
'PASSWORD'='170311d87ffbd680ee89a6ae9edb811bc438720b1f4892c46ba2438f0cf5bfc4'  
in the settings.py file, DATABASES - default    
*Requires Python 3 and pip is required to run.*  

#### superuser login:  
username: matt  
password: Password`123  

