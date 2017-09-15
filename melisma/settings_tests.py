from settings import *
from . import _confidential

DATABASES = {
  'default': {                                                                
     	'ENGINE': 'django.db.backends.postgresql_psycopg2',                    
    	'NAME': _confidential.CONFIDENTIAL_KEYS['test_db_name'],                   
        'USER': _confidential.CONFIDENTIAL_KEYS['db_username'],                 
        'PASSWORD': _confidential.CONFIDENTIAL_KEYS['db_password'],             
        'HOST': '127.0.0.1',                                                    
        'PORT': '5432',                                                         
  }
}
