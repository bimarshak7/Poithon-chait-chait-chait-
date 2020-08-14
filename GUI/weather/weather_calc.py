import requests
import json
from datetime import datetime
def winddir(degree):
	val=int((degree/22.5)+.5)
	arr=["N","NNE","NE","ENE","E","ESE", "SE", "SSE","S","SSW","SW","WSW","W","WNW","NW","NNW"]
	return arr[(val % 16)]
def tempconv(kelvin):
	return str("{:.2f}".format(kelvin-273))+u"\u00B0"+"C"
def timeconv(stamp):
	return str(datetime.fromtimestamp(stamp).time())
def search(city):
	try:
		url="http://api.openweathermap.org/data/2.5/weather?q="+city+"&appid=55a6b2683f3c85dcb1fe4e0d4039dc0a"
		api_req=requests.get(url)
		data=json.loads(api_req.content)
		country=data["sys"]["country"]
		city=data["name"]
		temp=tempconv(data["main"]["temp"])
		temp_feel=tempconv(data["main"]["feels_like"])
		temp_min=tempconv(data["main"]["temp_min"])
		temp_max=tempconv(data["main"]["temp_max"])
		weather=data["weather"][0]["main"]
		weather_desc=data["weather"][0]["description"]
		sunrise=timeconv(data["sys"]["sunrise"])
		sunset=timeconv(data["sys"]["sunset"])
		humidity=str(data["main"]["humidity"])+" %"
		pressure=str(data["main"]["pressure"])+" hPa"
		wind_dir=winddir(data["wind"]["deg"])
		url="http://openweathermap.org/img/wn/"+data["weather"][0]["icon"]+"@2x.png"
		dat=[country,city,weather,weather_desc,temp,temp_feel,temp_min,temp_max,sunrise,sunset,pressure,wind_speed,wind_dir,humidity,url]
		try:
			visibility=str(data["visibility"]//1000)+" KM"
		except:
			visibility="-"
		dat.append(visibility)
		return dat
	except Exception as error:
		return "0"
