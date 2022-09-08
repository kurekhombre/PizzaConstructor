# Pizza Constructor
### About
The website where customer can create his own pizza (size/crust/toppings) and send a confirmation email

## DEMO
![Alt text](/pizza_constructor_index.png?raw=true "Pizza Constructor")
![Alt text](/pizza_constructor_order.png?raw=true "Order")
![Alt text](/pizza_constructor_email_message.png?raw=true "Email Message")

## Setup
- ``` git clone https://github.com/kurekhombre/GoldenThought.git ```
- Create virtual environment ```python3 -m venv venv``` and activate it
  - Linux/Mac ``` source venv/bin/activate ```
  - Windows ``` venv\Scripts\activate.bat ```
- ``` pip install -r requirements.text ```
- Generate SECRET KEY with 
  - https://djecrety.ir/ or 
  - ``` python manage.py shell ``` 
   ``` >>> from django.core.management.utils import get_random_secret_key``` 
  ``` print(get_random_secret_key) ```
- Create  file '.env' in project folder and paste ``` SECRET_KEY='<your_key>' ```
- Same with ``` EMAIL_HOST_USER  ``` and  ``` EMAIL_HOST_PASSWORD```
- ``` python manage.py makemigrations ```
- ``` python manage.py migrate ```
- ``` python manage.py runserver ```


## TODO
- Frontend look
- Separate OrderOptions to Size and Crust Models
- Email confirmation with activation link
