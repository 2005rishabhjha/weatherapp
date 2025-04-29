import requests
import json
import win32com.client as wincom


city = input("Enter the name of the city\n")

url = f"https://api.weatherapi.com/v1/current.json?key=15580c49c35a43e18dc63859252704&q={city}"

r = requests.get(url)
print(r.text)
wdic = json.loads(r.text)
print(wdic["current"]["temp_c"])

speak = wincom.Dispatch("SAPI.SpVoice")

text = f"say 'The current weather in {city} is degrees'"
speak.Speak(text)