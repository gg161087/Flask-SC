class Config:
    SECRET_KEY = '37a60a0c42bc00e7415e93c031cd66ccfc37fb8dec839b070387fcad246bc87d'

class DevelopmentConfig(Config):
    DEBUG = True
    MYSQL_HOST = 'localhost'
    MYSQL_USER = 'root'
    MYSQL_PASSWORD = ''
    MYSQL_DB = 'flask-sc'

config = {
    'development': DevelopmentConfig
}