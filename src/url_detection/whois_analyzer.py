import ssl
import socket
import whois
from urllib.parse import urlparse
from datetime import datetime


class WhoisAnalyzer:

    def __init__(self, url):

        self.url = url
        self.domain = urlparse(url).netloc.replace("www.", "")

    # ----------------------------------

    def domain_age(self):

        try:

            info = whois.whois(self.domain)

            creation = info.creation_date

            if isinstance(creation, list):
                creation = creation[0]

            if creation:

                return (datetime.now() - creation).days

            return -1

        except:
            return -1

    # ----------------------------------

    def expiry_days(self):

        try:

            info = whois.whois(self.domain)

            expiry = info.expiration_date

            if isinstance(expiry, list):
                expiry = expiry[0]

            if expiry:

                return (expiry - datetime.now()).days

            return -1

        except:
            return -1

    # ----------------------------------

    def registrar(self):

        try:

            info = whois.whois(self.domain)

            if info.registrar:

                return info.registrar

            return "Unknown"

        except:

            return "Unknown"

    # ----------------------------------

    def ssl_valid(self):

        try:

            context = ssl.create_default_context()

            with socket.create_connection((self.domain,443),timeout=5) as sock:

                with context.wrap_socket(
                    sock,
                    server_hostname=self.domain
                ) as ssock:

                    cert = ssock.getpeercert()

                    return 1 if cert else 0

        except:

            return 0

    # ----------------------------------

    def extract(self):

        return {

            "DomainAge":self.domain_age(),

            "ExpiryDays":self.expiry_days(),

            "Registrar":self.registrar(),

            "SSLValid":self.ssl_valid()

        }