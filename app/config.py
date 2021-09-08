
from logging import DEBUG


class Config:
    '''
    General configuration parent class
    '''
    MOVIE_API_BASE_URL ='https://api.themoviedb.org/3/movie/{}?api_key={}'

class ProdConfig(Config):
    '''
    Production configuration child
    Args:
    Config:the parent configuration class with general configuiration settings
    '''
    pass
class DevConfig(Config):
    '''
    Development configuration child class
    Args:
    Config:The parent configuration class with general configuilation settings
    '''
    DEBUG=True

