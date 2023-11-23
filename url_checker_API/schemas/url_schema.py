from pydantic import BaseModel, validator
from urllib.parse import urlparse
from models.url_model import UrlModel


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
    

class UrlSchema(BaseModel):
    """ Define como deve ser o url de input para o modelo de ML
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
    
class UrlStringToCheckSchema(BaseModel):
    """ Define input do front end
    """
    
    @validator('url_str')
    def validate_url_str(cls, v):
        parsed_url = urlparse(v)
        if all([parsed_url.scheme, parsed_url.netloc]):
            return v
        raise ValueError("URL inválido")
    
    url_str: str = "https://eusa-lombo.firebaseapp.com/"
    
# Apresenta apenas os dados de um url    
def apresenta_url(url: UrlModel):
    """ Retorna uma representação do url seguindo o schema definido em
        UrlSchema.
    """
    return {
        "url_str": url.url_str,
        "length_url": url.length_url,
        "length_hostname": url.length_hostname,
        "nb_dots": url.nb_dots,
        "nb_hyphens": url.nb_hyphens, 
        "nb_underscore": url.nb_underscore,
        "nb_tilde": url.nb_tilde,
        "nb_percent": url.nb_percent,
        "nb_slash": url.nb_slash,
        "nb_colon": url.nb_colon,
        "nb_comma": url.nb_comma,
        "nb_semicolumn": url.nb_semicolumn,
        "nb_dollar": url.nb_dollar,
        "nb_www": url.nb_www,
        "http_in_path": url.http_in_path,
        "url_predic": url.url_predic
    }

