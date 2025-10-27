#This is my first website status checker
import requests

#webste to check 
website = "https://google.com"

try:
  response = request.get(website)
  if response.status_code == 200:
    print(f"Success: {website} is online"}
  else: 
    print(f"Warning: {website} return status code {response.status_code}")
except:
  print(f"Error: {Website} is Down or cannot be reached)
