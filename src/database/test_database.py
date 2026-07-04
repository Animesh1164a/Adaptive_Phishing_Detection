from database import *

create_database()

insert_record(

    "URL",

    "http://paypal-login-security.xyz",

    "PHISHING",

    "HIGH",

    94.2

)

data = get_history()

print()

for row in data:

    print(row)