from pydantic import BaseModel
# from model.url_check import UrlModel


class UrlSchema(BaseModel):
    """ Define como deve ser o url
    """
    url_str: str = "https://eusa-lombo.firebaseapp.com/"
    length_url: int = 35
    length_hostname: int = 26
    nb_dots: int = 2
    nb_hyphens: int = 1
    nb_underscore: int = 0
    nb_tilde: int = 0
    nb_percent: int = 0
    nb_slash: int = 3
    nb_colon: int = 1
    nb_comma: int = 0
    nb_semicolumn: int = 0
    nb_dollar: int = 0
    nb_www: int = 0
    http_in_path: int = 0 
    url_predic: int = 1
    

class UrlToCheckSchema(BaseModel):
    """ Define como deve ser o url
    """
    url_str: str = "https://eusa-lombo.firebaseapp.com/"
    length_url: int = 35
    length_hostname: int = 26
    nb_dots: int = 2
    nb_hyphens: int = 1
    nb_underscore: int = 0
    nb_tilde: int = 0
    nb_percent: int = 0
    nb_slash: int = 3
    nb_colon: int = 1
    nb_comma: int = 0
    nb_semicolumn: int = 0
    nb_dollar: int = 0
    nb_www: int = 0
    http_in_path: int = 0 

