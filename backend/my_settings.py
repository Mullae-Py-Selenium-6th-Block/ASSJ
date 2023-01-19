#my_settings.py
DATABASES = {
    'default': {
        'ENGINE': 'django.db.backends.mysql', #1
        'NAME': 'assj', #2
        'USER': 'team_6', #3                      
        'PASSWORD': '247990',  #4              
        'HOST': '43.201.96.246',   #5                
        'PORT': '3306', #6
    }
}
SECRET_KEY ='django-insecure-f$5sgt141xy3y^0eowa@7i$-yf8!ydp01y8&s&r+wa59^r$$v8'