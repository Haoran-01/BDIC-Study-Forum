# 数据库的配置变量
HOSTNAME = '127.0.0.1'
PORT     = '3306'
DATABASE = 'cyanpine'
USERNAME = 'root'
PASSWORD='Wangji1208'
DB_URI='mysql+pymysql://{}:{}@{}:{}/{}?charset=utf8'.format(USERNAME,PASSWORD,HOSTNAME,PORT,DATABASE)
SQLALCHEMY_DATABASE_URI = DB_URI
SQLALCHEMY_TRACK_MODIFICATIONS = True

SECRET_KEY='dskjfwqienkehyr1'

# email config
# use 163 email
MAIL_SERVER =  "smtp.163.com"
MAIL_PORT =  465
MAIL_USE_TLS = False
MAIL_USE_SSL = True
MAIL_DEBUG = True
MAIL_USERNAME = "cyanpine12@163.com"
MAIL_PASSWORD = "AKNAKMOROSOSPAGB"
MAIL_DEFAULT_SENDER = "cyanpine12@163.com"