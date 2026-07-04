import re
import socket
from urllib.parse import urlparse


class URLFeatureExtractor:

    def __init__(self, url):

        self.url = url.strip()

        # Automatically add https:// if missing
        if not self.url.startswith(("http://", "https://")):
            self.url = "https://" + self.url

        self.parsed = urlparse(self.url)

        self.domain = self.parsed.netloc

    # ==========================================================
    # BASIC FEATURES
    # ==========================================================

    def url_length(self):
        return len(self.url)

    def domain_length(self):
        return len(self.domain)

    def is_https(self):
        return 1 if self.parsed.scheme == "https" else 0

    def is_ip(self):

        pattern = r"^(?:[0-9]{1,3}\.){3}[0-9]{1,3}$"

        return 1 if re.match(pattern, self.domain) else 0

    def number_of_digits(self):
        return sum(c.isdigit() for c in self.url)

    def digit_ratio(self):

        if len(self.url) == 0:
            return 0

        return self.number_of_digits() / len(self.url)

    def number_of_letters(self):
        return sum(c.isalpha() for c in self.url)

    def letter_ratio(self):

        if len(self.url) == 0:
            return 0

        return self.number_of_letters() / len(self.url)

    def special_characters(self):

        return len(re.findall(r"[?&=%@#_\-.]", self.url))

    def special_char_ratio(self):

        if len(self.url) == 0:
            return 0

        return self.special_characters() / len(self.url)

    def number_subdomains(self):

        return self.domain.count(".")

    def has_at_symbol(self):

        return 1 if "@" in self.url else 0

    def has_hyphen(self):

        return 1 if "-" in self.domain else 0

    def has_obfuscation(self):

        return 1 if "%" in self.url else 0

    def has_equal(self):

        return self.url.count("=")

    def has_questionmark(self):

        return self.url.count("?")

    def has_ampersand(self):

        return self.url.count("&")

    def resolve_domain(self):

        try:

            socket.gethostbyname(self.domain)

            return 1

        except:

            return 0

    # ==========================================================
    # ADVANCED URL FEATURES
    # ==========================================================

    def tld_length(self):

        parts = self.domain.split(".")

        if len(parts) > 1:
            return len(parts[-1])

        return 0

    def no_obfuscated_char(self):

        return self.url.count("%")

    def obfuscation_ratio(self):

        if len(self.url) == 0:
            return 0

        return self.no_obfuscated_char() / len(self.url)

    def url_char_probability(self):

        total = len(self.url)

        if total == 0:
            return 0

        valid = sum(c.isalnum() for c in self.url)

        return round(valid / total, 4)

    def char_continuation_rate(self):

        if len(self.url) == 0:
            return 0

        longest = 1
        current = 1

        for i in range(1, len(self.url)):

            if self.url[i] == self.url[i - 1]:

                current += 1

                longest = max(longest, current)

            else:

                current = 1

        return round(longest / len(self.url), 4)

    def url_similarity_index(self):

        domain = self.domain.replace(".", "").lower()

        url = self.url.lower()

        common = sum(ch in domain for ch in url)

        return round(common / max(len(url), 1), 4)

    def tld_legitimate_probability(self):

        tld_scores = {

            "com":0.99,
            "org":0.98,
            "edu":0.99,
            "gov":1.00,
            "net":0.95,
            "io":0.92,
            "co":0.90,
            "in":0.90,
            "br":0.88,
            "uk":0.90,

            "xyz":0.10,
            "tk":0.05,
            "top":0.20,
            "gq":0.10,
            "cf":0.10,
            "ml":0.10,
            "ga":0.10

        }

        parts = self.domain.split(".")

        if len(parts) > 1:

            tld = parts[-1].lower()

            return tld_scores.get(tld,0.50)

        return 0.50

    # ==========================================================
    # FINAL FEATURE EXTRACTION
    # ==========================================================

    def extract(self):

        return {

            "URLLength": self.url_length(),

            "DomainLength": self.domain_length(),

            "IsDomainIP": self.is_ip(),

            "URLSimilarityIndex": self.url_similarity_index(),

            "CharContinuationRate": self.char_continuation_rate(),

            "TLDLegitimateProb": self.tld_legitimate_probability(),

            "URLCharProb": self.url_char_probability(),

            "TLDLength": self.tld_length(),

            "NoOfSubDomain": self.number_subdomains(),

            "HasObfuscation": self.has_obfuscation(),

            "NoOfObfuscatedChar": self.no_obfuscated_char(),

            "ObfuscationRatio": self.obfuscation_ratio(),

            "NoOfLettersInURL": self.number_of_letters(),

            "LetterRatioInURL": self.letter_ratio(),

            "NoOfDegitsInURL": self.number_of_digits(),

            "DegitRatioInURL": self.digit_ratio(),

            "NoOfEqualsInURL": self.has_equal(),

            "NoOfQMarkInURL": self.has_questionmark(),

            "NoOfAmpersandInURL": self.has_ampersand(),

            "NoOfOtherSpecialCharsInURL": self.special_characters(),

            "SpacialCharRatioInURL": self.special_char_ratio(),

            "IsHTTPS": self.is_https(),

            "DNS_Available": self.resolve_domain(),

            "HasAtSymbol": self.has_at_symbol(),

            "HasHyphen": self.has_hyphen()

        }


# ==========================================================

if __name__ == "__main__":

    url = input("Enter URL: ")

    extractor = URLFeatureExtractor(url)

    features = extractor.extract()

    print("\nExtracted Features\n")

    for k, v in features.items():

        print(f"{k:30} : {v}")