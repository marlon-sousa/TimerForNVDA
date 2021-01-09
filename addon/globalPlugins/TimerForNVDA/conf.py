import config

ADDON_CONFIG = "timerForNVDA"


def initConfiguration():
    confspec = {
        "reportWithSound": "boolean( default=True)",
        "reportWithSpeech": "boolean( default=False)",
        "operationMode": "string( default=TIMER)",
        "timeUnit": "string( default=SECONDS)",
    }

    config.conf.spec[ADDON_CONFIG] = confspec


def getConfig(key):
    value = config.conf[ADDON_CONFIG][key]
    return value


def setConfig(key, value):
    config.conf[ADDON_CONFIG][key] = value


initConfiguration()
