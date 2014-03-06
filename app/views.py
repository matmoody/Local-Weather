from flask import render_template
from app import app
import forecastio

api_key = "59053df436eaca0f50ee87db0b80dbff"
lat = 38.8242
lng = -97.6072

forecast = forecastio.load_forecast(api_key, lat, lng)

byHour = forecast.hourly()
now = forecast.currently()

@app.route('/')
@app.route('/index')
def index():
	return render_template("index.html",
		title = 'Home',
		now = forecast.currently(),
		byHour = forecast.hourly())