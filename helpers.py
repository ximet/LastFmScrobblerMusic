import time
import datetime

def get_current_timestamp():
    timestamp = int(time.mktime(datetime.datetime.now().timetuple()))
    print("Timestamp:\t" + str(timestamp)) #for logging
    return timestamp
