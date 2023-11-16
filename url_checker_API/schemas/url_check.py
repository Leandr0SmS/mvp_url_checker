from pydantic import BaseModel
# from model.url_check import UrlModel


class UrlChecked(BaseModel):
    """ Define como deve ser o url
    """
    url_str: str = "https://www.dropbox.com/l/AABsArKdOw0Xm20ePPEw4Fd2__f1tVEhlv0"
    url_predic: int = 1


class UrlTest(BaseModel):
    """ Define como deve ser a estrutura que representa a inserção
    do url ao sistema.
    """
    url_str: str = "https://agendagotsch.com/en/"


# def apresenta_url(url: UrlModel):
#     """ Retorna uma representação do url seguindo o schema definido em
#         UrlSchema.
#     """
#     return {
#         "url_str": url.url,
#         "url_predic": url.url_predic
#     }
