import re
import socket
from urllib.parse import urlparse


class RuleEngine:

    def __init__(self, url):

        self.original_url = url.strip()

        if not self.original_url.startswith(("http://", "https://")):
            self.original_url = "https://" + self.original_url

        self.url = self.original_url.lower()
        self.parsed = urlparse(self.original_url)
        self.domain = self.parsed.netloc.lower()

        self.score = 0
        self.reasons = []

    # -------------------------------------------------------

    def add_score(self, score, reason):

        self.score += score

        if reason not in self.reasons:
            self.reasons.append(reason)

    # -------------------------------------------------------

    def check_https(self):

        if self.parsed.scheme != "https":
            self.add_score(30, "HTTPS is missing")

    # -------------------------------------------------------

    def check_ip(self):

        pattern = r"^(?:\d{1,3}\.){3}\d{1,3}$"

        if re.match(pattern, self.domain):
            self.add_score(60, "IP Address used instead of domain")

    # -------------------------------------------------------

    def check_dns(self):

        try:
            socket.gethostbyname(self.domain)
        except:
            self.add_score(20, "Domain cannot be resolved")

    # -------------------------------------------------------

    def check_url_length(self):

        length = len(self.url)

        if length > 120:
            self.add_score(25, "Extremely long URL")

        elif length > 80:
            self.add_score(15, "Long URL")

    # -------------------------------------------------------

    def check_special_characters(self):

        count = len(re.findall(r"[@?&=%_\-]", self.url))

        if count >= 10:
            self.add_score(20, "Too many special characters")

        elif count >= 6:
            self.add_score(10, "Many special characters")

    # -------------------------------------------------------

    def check_subdomains(self):

        if self.domain.count(".") >= 3:
            self.add_score(20, "Too many subdomains")

    # -------------------------------------------------------

    def check_at_symbol(self):

        if "@" in self.url:
            self.add_score(30, "@ symbol detected")

    # -------------------------------------------------------

    def check_obfuscation(self):

        if "%" in self.url:
            self.add_score(25, "URL Obfuscation detected")

    # -------------------------------------------------------

    def check_shortener(self):

        shorteners = [

            "bit.ly",
            "tinyurl.com",
            "goo.gl",
            "t.co",
            "ow.ly",
            "is.gd",
            "buff.ly",
            "cutt.ly",
            "rb.gy",
            "rebrand.ly",
            "shorturl.at"

        ]

        for s in shorteners:

            if s in self.domain:

                self.add_score(40, f"URL Shortener ({s})")

                break

    # -------------------------------------------------------

    def check_keywords(self):

        keywords = {

            "login":25,
            "signin":25,
            "verify":25,
            "verification":25,
            "secure":20,
            "security":20,
            "update":20,
            "confirm":20,
            "account":20,
            "password":25,
            "payment":25,
            "invoice":15,
            "wallet":20,
            "bank":30,
            "crypto":25,
            "bitcoin":25,
            "btc":20,
            "reward":15,
            "gift":15,
            "bonus":15,
            "free":10,
            "otp":20,
            "prize":20

        }

        for word, score in keywords.items():

            if word in self.url:

                self.add_score(score, f"Keyword detected : {word}")

    # -------------------------------------------------------

    def check_brand_impersonation(self):

        brands = [

            "google",
            "paypal",
            "amazon",
            "microsoft",
            "apple",
            "facebook",
            "instagram",
            "netflix",
            "hdfc",
            "sbi",
            "icici"

        ]

        phishing_words = [

            "login",
            "signin",
            "verify",
            "secure",
            "update",
            "account",
            "password"

        ]

        if any(b in self.url for b in brands):

            if any(k in self.url for k in phishing_words):

                self.add_score(

                    35,

                    "Brand impersonation detected"

                )

    # -------------------------------------------------------

    def check_tld(self):

        suspicious = [

            ".xyz",
            ".top",
            ".tk",
            ".gq",
            ".cf",
            ".ga",
            ".ml",
            ".click",
            ".buzz",
            ".work",
            ".cam",
            ".monster"

        ]

        for tld in suspicious:

            if self.domain.endswith(tld):

                self.add_score(30, f"Suspicious TLD ({tld})")

                break

    # -------------------------------------------------------

    def check_hyphen(self):

        if self.domain.count("-") >= 2:

            self.add_score(25, "Multiple hyphens")

    # -------------------------------------------------------

    def check_numbers(self):

        digits = sum(c.isdigit() for c in self.domain)

        if digits >= 6:

            self.add_score(15, "Too many digits in domain")

    # -------------------------------------------------------

    def check_double_slash(self):

        path = self.url.replace("https://", "").replace("http://", "")

        if "//" in path:

            self.add_score(20, "Double slash redirection")

    # -------------------------------------------------------

    def calculate(self):

        self.check_https()

        self.check_ip()

        self.check_dns()

        self.check_url_length()

        self.check_special_characters()

        self.check_subdomains()

        self.check_at_symbol()

        self.check_obfuscation()

        self.check_shortener()

        self.check_keywords()

        self.check_brand_impersonation()

        self.check_tld()

        self.check_hyphen()

        self.check_numbers()

        self.check_double_slash()

        if self.score > 100:
            self.score = 100

        return {

            "risk_score": self.score,

            "reasons": self.reasons

        }


# -------------------------------------------------------

if __name__ == "__main__":

    url = input("Enter URL : ")

    result = RuleEngine(url).calculate()

    print("\nRisk Score :", result["risk_score"])

    print("\nReasons:")

    for r in result["reasons"]:

        print("-", r)