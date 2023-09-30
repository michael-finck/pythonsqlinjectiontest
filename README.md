+# Web Application Penetration Testing - SQL Injection

This Python script demonstrates a basic SQL injection attack on a web application.
It exploits a SQL injection vulnerability in a targeted web page to demonstrate a potential security risk.

## Table of Contents

- [Overview](#overview)
- [Usage](#usage)
- [SQL Injection](#sql-injection)

## Overview

The script sends a malicious payload as a username parameter to a targeted URL using a POST request.
The payload is designed to attempt to drop the 'Users' table in the database through SQL injection.
The script then analyzes the response to determine if the SQL injection was successful based on the presence of an "Error" message.

## Usage

1. Install Python (if not already installed) from [Python Official Website](https://www.python.org/).

2. Clone the repository or download the `webapp_sql_injection.py` file.

3. Open the script and modify the `target_url` variable to match the URL of the vulnerable web page:
   ```python
   target_url = "http://www.myexample.com/vulnerable-page.php"

Run the script:
python pythonsqlinjectiontest.py

SQL Injection

The exploit_sql_injection() function sends a malicious SQL injection payload to the targeted URL.
The payload attempts to execute SQL commands to drop the 'Users' table in the database.
The script checks the response for the presence of an "Error" message to determine the success of the SQL injection.


In this README:

1. **Title and Description**: Provides an overview of the script's purpose and functionality.

2. **Table of Contents**: Lists the sections covered in the README.

3. **Overview**: Explains the general purpose and operation of the script.

4. **Usage**: Guides users on how to use the script, including installation, modifying the script for their specific use, and running the script.

5. **SQL Injection**: Explains the SQL injection technique used in the script.

Feel free to modify and tailor this README to suit the specific needs and details of your project.
