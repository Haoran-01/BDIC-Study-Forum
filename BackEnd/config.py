from flask import Flask

app=Flask(__name__)

#数据库的配置变量
HOSTNAME='127.0.0.1'
PORT ='3306'
DATABASE='zl_flask'
USERNAME='root'
DB_URI='mysql+pymysql://{}:{}@{}:{}/{}?charset=utf8'.format(USERNAME,PASSWORD,HOSTNAME,PORT,DATABASE)
app.config['SQLaLCHEMY_DATABASE_URI']=DB_URI

MAIL_SERVER ="smtp.qq.com"
MAIL_PORT =465
MAIL_USE_TLS=False
MAIL_USE_SSL =True
MAIL_DEBUG =True
MAIL_USERNAME ="2769059069@qq.com"
MAIL_PASSWORD ="aiwxvcisknaodcef"
MAIL_DEFAULT_SENDER ="2769059069@qq.com"
MAIL_MAX_EMAILS =
MAIL_SUPPRESS_SEND =
MAIL_ASCII_ATTACHMENTS =