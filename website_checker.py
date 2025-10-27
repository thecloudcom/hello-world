#This is my first website status checker
import requests

#webste to check 
website: str = "https://google.com"

try:
  response = requests.get(website)
  if response.status_code == 200:
    print(f"Success: {website} is online")
  else:
      print(f"Warning: {website} returned status code {response.status_code}")
except requests.exceptions.RequestException:
  print(f"Error: {website} is Down or cannot be reached")
