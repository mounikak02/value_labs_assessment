# value_labs_assessment
Tracking Number Generator API
Create a Django project for Tracking Number Generator API
The URL of the API endpoint, which is http://localhost:8000/api/next-tracking-number/.

params: A dictionary containing the parameters to be sent with the GET request. These parameters are:
origin_country_id: Set to 'MY', which likely represents Malaysia.
destination_country_id: Set to 'ID', which likely represents Indonesia.
weight: Set to '1.234', which represents the weight of the package.
customer_id: Set to a UUID ('de619854-b59b-425e-9db4-943979e1bd49'), which likely identifies the customer.
customer_name: Set to 'RedBox Logistics', which is the name of the customer.

1. first create django project using this command
django-admin startproject tracking_number_generator

# create app tracking
then cd tracking_number_generator
django-admin startapp tracking

# create virtual environment 
python -m virtualenv venv
source .\venv\Scripts\activate.bat

parallely in another terminal window run this command to check for alternative errors 
python manage.py runserver

2. setup rest api framework
# install djangorestframework 
pip install djangorestframework

# add rest framework to installed apps in settings.py
add rest_framework under installed_apps in settings.py file
and add the app tracking under installed_apps

3. Create the tracking model
in tracking/models.py
class name - TrackingNumber
create query parameters - tracking_number, origin_country_id, destination_country_id, weight, created_at,
customer_id, customer_name, customer_slug
initialise the variable values with the given parameter constraints

4. create the serializers
tracking/serializers.py 

5. create the views
tracking/views.py
get_tracking_number method
request the parameters from the get url and using the parameters 
generate a random number of 16 digits 

create generate_tracking_number method 
and add  @api_view(['GET']) to the method get_tracking_number

the response from the API endpoint using the response.json() method, which returns the response content in JSON format.


6. add urls in tracking/urls.py

7. add urls in tracking_number_generate and add include to the imports

8. in tests.py class, 
import the requests module
add the url trying to test
and params 


9. Go to postman 
select request type as Get and enter the url 
add the query parameters and click on send



