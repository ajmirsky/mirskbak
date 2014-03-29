

# backup.handlers.MySQLBackup
# backup.handlers.TarFiles
# backup.handlers.PostgresSQL
# . . .

# backup.handlers.RotatingFileHandler
# backup.handlers.FileNow

# backup.storage.S3
# backup.




# combining multiple backup files into a set
#backup.set.FileGroup ('<timestamp>_asset.ext')
#backup.set.Directory ('/<timestamp>/asset.ext')


BACKUP = {
    'version': 1,
    'disable_existing_loggers': True,
    'filters': {
         'require_debug_false': {
             '()': 'django.utils.log.RequireDebugFalse',
         }
     },    
    'formatters': {
        'standard': {
            'format' : "[%(asctime)s] %(levelname)s [%(name)s:%(lineno)s] %(message)s",
            'datefmt' : "%d/%b/%Y %H:%M:%S"
        },
        'simple': {
            'format': '%(levelname)s %(message)s'
        },        
    },
    'handlers': {
        'null': {
            'level':'DEBUG',
            'class':'django.utils.log.NullHandler',
        },
        'mail_admins': {
            'level': 'ERROR',
            'filters': ['require_debug_false'],
            'class': 'django.utils.log.AdminEmailHandler',
            'formatter': 'standard',
        },        
        'logfile': {
            'level':'DEBUG',
            'class':'logging.handlers.RotatingFileHandler',
            'filename': PROJECT_PATH + "/logfile",
            'maxBytes': 50000,
            'backupCount': 2,
            'formatter': 'standard',
        },
        'console':{
            'level':'DEBUG',
            'class':'logging.StreamHandler',
            'formatter': 'standard'
        },
    },
    'assets': {
        'MyWP': {
            'handlers':['database', 'media'],
            #'propagate': True,
            #'level':'WARN',
        },
        #'django.db.backends': {
            #'handlers': ['console'],
            #'level': 'DEBUG',
            #'propagate': False,
        #},
        'scriptnow': {
            'handlers': ['console', 'logfile',],
            'level': 'WARNING',
        },
    }
}