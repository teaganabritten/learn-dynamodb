import boto3

dynamodb = boto3.resource('dynamodb')
table = dynamodb.Table('users')

users = [
    {"username": "jsmith",   "firstname": "Jamal",    "lastname": "Smith",    "email": "jsmith@example.com",   "dob": "1990-04-12", "status": "active"},
    {"username": "mjones",   "firstname": "Marietta", "lastname": "Jones",    "email": "mjones@example.com",   "dob": "1985-07-23", "status": "active"},
    {"username": "blee",     "firstname": "Bruce",    "lastname": "Lee",      "email": "blee@example.com",     "dob": "1940-11-27", "status": "inactive"},
    {"username": "pparker",  "firstname": "Philip",   "lastname": "Parker",   "email": "pparker@example.com",  "dob": "2001-08-10", "status": "active"},
    {"username": "dwilson",  "firstname": "Diana",    "lastname": "Wilson",   "email": "dwilson@example.com",  "dob": "1995-03-05", "status": "suspended"},
    {"username": "rrogers",  "firstname": "Robert",   "lastname": "Rogers",   "email": "rrogers@example.com",  "dob": "1988-12-15", "status": "active"},
    {"username": "cmonroe",  "firstname": "Charlie",  "lastname": "Monroe",   "email": "cmonroe@example.com",  "dob": "1992-06-20", "status": "inactive"},
    {"username": "srogers",  "firstname": "Sarah",    "lastname": "Rogers",   "email": "srogers@example.com",  "dob": "1987-09-18", "status": "suspended"}
]

for user in users:
    table.put_item(Item=user)
    print(f"Loaded: {user['username']}")

print("Done.")
