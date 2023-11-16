from sqlalchemy import Column, String, Integer
from model import Base


class UrlModel(Base):
    __tablename__ = 'url_predicted'

    id_url = Column(Integer, primary_key=True)
    url_str = Column(String(500), unique=True, nullable=False)
    url_predic = Column(Integer, nullable=False)

    def __init__(self, url_str: str, url_predic: int):
        """"Recebe uma url e cria um modelo"

        Args:
            url (str): String que
                representa um URL
            url_predic (int):
                0 - legitimo
                1 - phishing
        """

        self.url_str = url_str
        self.url_predic = url_predic

    def __repr__(self):
        return f'Url("{self.url_str}")'
