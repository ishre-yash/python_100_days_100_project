import requests
from twilio.rest import Client

# Latitude = 29.9934, Longitude = 78.1997
weather_params = {
    "lat": 29.9934,
    "lon": 78.1997,
    "exclude": "current,minutely,daily",
    "appid": api_key
}

OWM_Endpoint = "https://api.openweathermap.org/data/2.5/onecall"
api_key = ''

response = requests.get(OWM_Endpoint, params=weather_params)
response.raise_for_status()
data = response.json()
data_slice = data["hourly"][:12]

will_rain = False
for hour_data in data_slice:
    conditon_code = hour_data["weather"][0]['id']
    if int(conditon_code) < 700:
        will_rain = True


account_sid = ''
auth_token = ''
if will_rain:
    client = Client(account_sid, auth_token)
    message = client.messages \
                    .create(
                        body="ShreYash Boot Message : It's Going To rain today.Remember to bring an ☔",
                        from_='+19106346521',
                        to=''
                    )
    print(message.sid)
