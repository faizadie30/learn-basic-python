from zoneinfo import ZoneInfo
from datetime import datetime, timedelta

# dateNow = datetime.now()
date = datetime.now()
dt = date.strftime("%d-%M-%Y %H:%I:%S")
print(dt)