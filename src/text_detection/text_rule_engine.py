import re


class TextRuleEngine:

    def __init__(self, text):

        self.text = text.lower()

        self.score = 0

        self.reasons = []

    # -----------------------------------------

    def add(self, score, reason):

        self.score += score

        if reason not in self.reasons:
            self.reasons.append(reason)

    # -----------------------------------------

    def keyword_rules(self):

        keywords = {

            "urgent":15,
            "immediately":15,
            "immediate":10,
            "action required":20,
            "verify":20,
            "verification":20,
            "login":20,
            "signin":20,
            "password":20,
            "account":15,
            "payment":20,
            "bank":20,
            "paypal":25,
            "amazon":20,
            "microsoft":20,
            "apple":20,
            "google":15,
            "security":15,
            "suspended":20,
            "blocked":20,
            "disabled":20,
            "confirm":20,
            "update":15,
            "reward":15,
            "gift":10,
            "bonus":10,
            "lottery":25,
            "winner":20,
            "won":20,
            "prize":20,
            "crypto":20,
            "bitcoin":20,
            "wallet":20,
            "otp":20,
            "invoice":15,
            "click":10,
            "click here":20,
            "limited time":15

        }

        for word, value in keywords.items():

            if word in self.text:

                self.add(value, word)

    # -----------------------------------------

    def url_rule(self):

        if re.search(r"http[s]?://", self.text):

            self.add(25, "URL detected")

    # -----------------------------------------

    def shortener_rule(self):

        shorteners = [

            "bit.ly",

            "tinyurl",

            "goo.gl",

            "t.co",

            "rb.gy",

            "cutt.ly"

        ]

        for s in shorteners:

            if s in self.text:

                self.add(30, "Shortened URL")

                break

    # -----------------------------------------

    def money_rule(self):

        if "$" in self.text:

            self.add(10, "Money Symbol")

    # -----------------------------------------

    def exclamation_rule(self):

        if self.text.count("!") >= 2:

            self.add(10, "Too many exclamation marks")

    # -----------------------------------------

    def calculate(self):

        self.keyword_rules()

        self.url_rule()

        self.shortener_rule()

        self.money_rule()

        self.exclamation_rule()

        if self.score > 100:

            self.score = 100

        return {

            "rule_score": self.score,

            "reasons": self.reasons

        }