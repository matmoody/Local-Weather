from flask import render_template
from app import app
import forecastio
from keys import api_key


lat = 38.8242
lng = -97.6072



forecast = forecastio.load_forecast(api_key, lat, lng)

byHour = forecast.hourly()
byMinute = forecast.minutely()
now = forecast.currently()
day = forecast.daily()

@app.route('/')
@app.route('/index')
def index():
	return render_template("base.html",
		title = 'Home',
		now = forecast.currently(),
		byHour = forecast.hourly(),
		byMinute = forecast.minutely(),
		day = forecast.daily())
