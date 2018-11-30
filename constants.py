from config import config

# common
DEBUG = config["COMMON"]["DEBUG"]

### Config related constants

DRIVER_NAME = config["DEVICE"]["DRIVER_NAME"]
DRIVER_ID = config["DEVICE"]["DRIVER_ID"]
VEHICLE_MODEL = config["DEVICE"]["VEHICLE_MODEL"]
VEHICLE_ID = config["DEVICE"]["VEHICLE_ID"]
SENSORS = config["DEVICE"]["SENSORS"]
DISTANCE_UNITS_LABEL= config["DEVICE"]["DISTANCE_UNITS_LABEL"]
# to avoid gps errors till implemented
DEFAULT_GPS = config["DEVICE"]["DEFAULT_GPS"]
LIVE = "True" == config["DEVICE"]["LIVE"]

SAMPLING_FREQUENCY = float(config["EDGE"]["SAMPLING_FREQUENCY"])

DATA_FILENAME = config["DEVICE"]["DEVICE_DATA_FILENAME"]

STREAM = "True" == config["EDGE"]["STREAM"]
EVENTS_FILENAME = config["EDGE"]["EVENTS_FILENAME"]
EVENTS_FILENAME_BACKUP = config["EDGE"]["EVENTS_FILENAME_BACKUP"]
HISTORY = int(config["EDGE"]["HISTORY"])
MAX_READINGS = int(config["EDGE"]["MAX_READINGS"])

DISTANCE_FILENAME = config["EDGE"]["DISTANCE_FILENAME"]
DISTANCE_FILENAME_BACKUP = config["EDGE"]["DISTANCE_FILENAME_BACKUP"]

INSURANCE_ENABLED = "True" == config["EDGE"]["INSURANCE_ENABLED"]
MY_DRIVING_ENABLED = "True" == config["EDGE"]["MY_DRIVING_ENABLED"]
SMART_CITY_ENABLED = "True" == config["EDGE"]["SMART_CITY_ENABLED"]
REPORT_RETRY_SEC = int(config["EDGE"]["REPORT_RETRY_SEC"])
SAVE_LOCAL_SEC = float(config["EDGE"]["SAVE_LOCAL_SEC"])

## auto domain related constants

HARDSTOP_THRESHOLD = 0.5
HARD_BREAK = "hard_break"
SPEEDING = "speeding"
NORMAL = "normal"
SLOW_DOWN = "slow_down"
MILES = "miles"
KMs = "kilometers"

INSURANCE_EVENTS = [HARD_BREAK, SPEEDING]
