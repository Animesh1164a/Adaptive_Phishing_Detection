import requests
from bs4 import BeautifulSoup


class WebsiteAnalyzer:

    def __init__(self, url):

        self.url = url

        self.html = ""

        self.soup = None

        self.fetch_page()

    # ----------------------------------------------------

    def fetch_page(self):

        try:

            headers = {
                "User-Agent":
                "Mozilla/5.0"
            }

            response = requests.get(

                self.url,

                timeout=10,

                headers=headers,

                allow_redirects=True

            )

            self.html = response.text

            self.soup = BeautifulSoup(

                self.html,

                "lxml"

            )

        except Exception:

            self.html = ""

            self.soup = None

    # ----------------------------------------------------

    def has_title(self):

        return 1 if self.soup and self.soup.title else 0

    # ----------------------------------------------------

    def page_title(self):

        if self.soup and self.soup.title:

            return self.soup.title.text.strip()

        return ""

    # ----------------------------------------------------

    def has_description(self):

        if not self.soup:

            return 0

        return 1 if self.soup.find(

            "meta",

            attrs={"name": "description"}

        ) else 0

    # ----------------------------------------------------

    def has_favicon(self):

        if not self.soup:

            return 0

        return 1 if self.soup.find(

            "link",

            rel=lambda x: x and "icon" in x.lower()

        ) else 0

    # ----------------------------------------------------

    def has_submit_button(self):

        if not self.soup:

            return 0

        return 1 if self.soup.find(

            "input",

            {"type": "submit"}

        ) else 0

    # ----------------------------------------------------

    def has_password_field(self):

        if not self.soup:

            return 0

        return 1 if self.soup.find(

            "input",

            {"type": "password"}

        ) else 0

    # ----------------------------------------------------

    def has_hidden_fields(self):

        if not self.soup:

            return 0

        return len(

            self.soup.find_all(

                "input",

                {"type": "hidden"}

            )

        )

    # ----------------------------------------------------

    def has_iframe(self):

        if not self.soup:

            return 0

        return len(

            self.soup.find_all("iframe")

        )

    # ----------------------------------------------------

    def image_count(self):

        if not self.soup:

            return 0

        return len(

            self.soup.find_all("img")

        )

    # ----------------------------------------------------

    def css_count(self):

        if not self.soup:

            return 0

        return len(

            self.soup.find_all(

                "link",

                rel="stylesheet"

            )

        )

    # ----------------------------------------------------

    def js_count(self):

        if not self.soup:

            return 0

        return len(

            self.soup.find_all("script")

        )

    # ----------------------------------------------------

    def robots(self):

        return 1 if "robots.txt" in self.html.lower() else 0

    # ----------------------------------------------------

    def responsive(self):

        if not self.soup:

            return 0

        return 1 if self.soup.find(

            "meta",

            attrs={"name": "viewport"}

        ) else 0

    # ----------------------------------------------------

    def popup_count(self):

        return self.html.lower().count("window.open")

    # ----------------------------------------------------

    def external_form_submit(self):

        if not self.soup:

            return 0

        forms = self.soup.find_all("form")

        for form in forms:

            action = form.get("action", "")

            if action.startswith("http"):

                return 1

        return 0

    # ----------------------------------------------------

    def keyword_bank(self):

        text = self.html.lower()

        return 1 if any(

            x in text

            for x in

            [

                "bank",

                "account"

            ]

        ) else 0

    # ----------------------------------------------------

    def keyword_pay(self):

        text = self.html.lower()

        return 1 if any(

            x in text

            for x in

            [

                "pay",

                "payment",

                "paypal"

            ]

        ) else 0

    # ----------------------------------------------------

    def keyword_crypto(self):

        text = self.html.lower()

        return 1 if any(

            x in text

            for x in

            [

                "bitcoin",

                "btc",

                "crypto",

                "ethereum"

            ]

        ) else 0

    # ----------------------------------------------------

    def extract(self):

        return {

            "HasTitle": self.has_title(),

            "Title": self.page_title(),

            "HasDescription": self.has_description(),

            "HasFavicon": self.has_favicon(),

            "Robots": self.robots(),

            "IsResponsive": self.responsive(),

            "NoOfURLRedirect": 0,

            "NoOfSelfRedirect": 0,

            "NoOfPopup": self.popup_count(),

            "NoOfiFrame": self.has_iframe(),

            "HasExternalFormSubmit": self.external_form_submit(),

            "HasSubmitButton": self.has_submit_button(),

            "HasHiddenFields": self.has_hidden_fields(),

            "HasPasswordField": self.has_password_field(),

            "Bank": self.keyword_bank(),

            "Pay": self.keyword_pay(),

            "Crypto": self.keyword_crypto(),

            "NoOfImage": self.image_count(),

            "NoOfCSS": self.css_count(),

            "NoOfJS": self.js_count()

        }


# ------------------------------------------------------------

if __name__ == "__main__":

    url = input("Enter URL : ")

    analyzer = WebsiteAnalyzer(url)

    result = analyzer.extract()

    print("\nWebsite Features\n")

    for k, v in result.items():

        print(f"{k:30} : {v}")