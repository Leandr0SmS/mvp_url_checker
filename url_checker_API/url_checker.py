import urllib.parse
import re

class Url_checker():
    def __init__(self, url_input:str):
        self.url_str = url_input
        
    def hostname_length(self):
        parsed_url = urllib.parse.urlparse(self.url_str)
        hostname_len = len(parsed_url.netloc)
        return hostname_len

    def url_nbCount_char(self, char, escape=False):
        if escape:
            reg_exp = re.compile(re.escape(char))
        else:
            reg_exp = re.compile(char)

        found = reg_exp.findall(self.url_str)
        if found:
            return len(found)
        else:
            return 0
        
    def find_http_in_path(self):
        parsed_url = urllib.parse.urlparse(self.url_str)
        # Get the length of the origin part of the URL
        url_origin_len = len(parsed_url.scheme) + len(parsed_url.netloc)
        # Extract the path
        path = url[url_origin_len:]
        reg_exp = re.compile("http")
        print(path)
        print({"regexp": reg_exp})
        found = reg_exp.findall(path)
        print(path)
        if found:
            return len(found)
        else:
            return 0


    def url_infos(self):
        return {
            "url": self.url_str,
            "length_url": len(self.url_str),
            "length_hostname": self.hostname_length(),
            "nb_dots": self.url_nbCount_char(".", True),
            "nb_hyphens": self.url_nbCount_char("-"),
            "nb_underscore": self.url_nbCount_char("_", True),
            "nb_tilde": self.url_nbCount_char("~"),
            "nb_percent": self.url_nbCount_char("%"),
            "nb_slash": self.url_nbCount_char("/", True),
            "nb_colon": self.url_nbCount_char(":"),
            "nb_comma": self.url_nbCount_char(","),
            "nb_semicolumn": self.url_nbCount_char(";"),
            "nb_dollar": self.url_nbCount_char("$", True),
            "nb_space": self.url_nbCount_char("\s", True),
            "nb_www": self.url_nbCount_char("www"),
            "hhtp_in_path": self.find_http_in_path()
        }
