from flask import Flask, render_template
from datetime import datetime
import pytz

app = Flask(__name__)

@app.route('/')
def home():
    time_zones = ['UTC', 'US/Pacific', 'Europe/London', 'Asia/Tokyo', 'Australia/Sydney']
    times = {tz: datetime.now(pytz.timezone(tz)).strftime('%Y-%m-%d %H:%M:%S') for tz in time_zones}
    return render_template('index.html', times=times)

if __name__ == '__main__':
    app.run(debug=True)
