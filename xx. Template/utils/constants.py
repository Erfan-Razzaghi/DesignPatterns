
LOG_COLORS={
        'DEBUG':    'cyan',
        'INFO':     'green',
        'WARNING':  'yellow',
        'ERROR':    'red',
        'CRITICAL': 'bold_red',
}
LOG_FORMAT = "[%(asctime)s] [%(log_color)s%(levelname)-s%(reset)s] [%(cyan)s%(module)s%(reset)s] %(message)s"
DATE_FORMAT = "%H:%M:%S %z"
LOG_LEVEL = "INFO"