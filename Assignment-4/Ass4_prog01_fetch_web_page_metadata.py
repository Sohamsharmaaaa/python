# Write a Python program using requests to fetch a web page (a local test page) and display the status code, response headers and the page size.

import requests

response = requests.get("http://127.0.0.1:8000/index.html")

print("Status code:", response.status_code)

print("\nResponse headers:")
for key, value in response.headers.items():
    print(f"  {key}: {value}")

print("\nPage size:", len(response.content), "bytes")

"""
Steps to run:
1. Start the default python server by giving command on terminal as
    $python3 -m http.server  
       OR 
    if we want to use different port no than default(8000)
    $python3 -m http.server 8080
    Note that donot close this terminal.
2. Create a html file in the same folder as index.html may be blank or
   add some html contents like 
     	<html>
	<body>
	<h1>Hello to all
	</body>
	</html>
3. Then open the firefox browser and type url as:
	http://localhost:8000
   We will see the output displayed on browser as:
   	Hello to all
4. Run the python program on another terminal as:
	$python program_name.py
5. At the end stop the server by pressing ctrl+c
"""
