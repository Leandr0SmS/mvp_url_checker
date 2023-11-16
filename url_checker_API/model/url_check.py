from sqlalchemy import Column, String, Integer
from model import Base


class UrlModel(Base):
    __tablename__ = 'url_predicted'

    id_url = Column(Integer, primary_key=True)
    url_str = Column("url_str", String(500), unique=True, nullable=False)
    length_url = Column("length_url", Integer, nullable=False)
    length_hostname = Column("length_hostname", Integer, nullable=False)
    nb_dots = Column("nb_dots", Integer, nullable=False)
    nb_hyphens = Column("nb_hyphens", Integer, nullable=False)
    nb_underscore = Column("nb_underscore", Integer, nullable=False)
    nb_tilde = Column("nb_tilde", Integer, nullable=False)
    nb_percent = Column("nb_percent ", Integer, nullable=False)
    nb_slash = Column("nb_slash", Integer, nullable=False)
    nb_colon = Column("nb_colon", Integer, nullable=False)
    nb_comma = Column("nb_comma", Integer, nullable=False)
    nb_semicolumn = Column("nb_semicolumn", Integer, nullable=False)
    nb_dollar = Column("nb_dollar", Integer, nullable=False)
    nb_www = Column("nb_www", Integer, nullable=False)
    http_in_path = Column("http_in_path", Integer, nullable=False)
    url_predic = Column(Integer, nullable=False)


    def __init__(self, url_str: str, length_url: int, length_hostname: int,
                nb_dots: int, nb_hyphens: int, nb_underscore: int, nb_tilde: int, nb_percent: int,
                nb_slash: int, nb_colon: int, nb_comma: int, nb_semicolumn: int,
                nb_dollar: int, nb_www: int, http_in_pat: int, url_predic: int):
        """
        Recebe uma url e cria um modelo"

        Args:
            url_str (str): String que
                representa um URL
            url_predic (int):
                0 - legitimo
                1 - phishing
            length_url (int):
                length of url_str
            length_hostname (int):
                length of url_str host name
            nb_dots (int):
                number of dots in ulr_str
            nb_hyphens (int):
                number od hypens in ulr_str
            nb_underscore (int):
                number of underscore in ulr_str
            nb_tilde (int):
                number of tilde in ulr_str
            nb_percent (int):
                number of percent in ulr_str
            nb_slash (int):
                number of slash in ulr_str
            nb_colon (int):
                number of colon in ulr_str
            nb_comma (int):
                number of comma in ulr_str
            nb_semicolumn (int):
                number of semicolumn in ulr_st
            nb_dollar (int):
                number of dollar in ulr_st
            nb_www (int):
                number of www in ulr_st
            http_in_path (int):
                number of http in the path of url_str
        """

        self.url_str = url_str
        self.length_url = length_url
        self.length_hostname = length_hostname
        self.nb_dots = nb_dots
        self.nb_hyphens = nb_hyphens
        self.nb_underscore = nb_underscore
        self.nb_tilde = nb_tilde
        self.nb_percent = nb_percent
        self.nb_slash = nb_slash
        self.nb_colon = nb_colon
        self.nb_comma = nb_comma
        self.nb_semicolumn = nb_semicolumn
        self.nb_dollar = nb_dollar
        self.nb_www = nb_www
        self.http_in_path = http_in_path
        self.url_predic = url_predic

    def __repr__(self):
        return f'Url("{self.url_str}")'
