#my_settings.py
DATABASES = {
    'default': {
        'ENGINE': 'django.db.backends.mysql', #1
        'NAME': 'assj', #2
        'USER': 'root', #3                      
        'PASSWORD': '12345678',  #4              
        'HOST': 'localhost',   #5                
        'PORT': '3306', #6
    }
}
SECRET_KEY ='django-insecure-f$5sgt141xy3y^0eowa@7i$-yf8!ydp01y8&s&r+wa59^r$$v8'