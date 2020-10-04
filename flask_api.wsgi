import logging, sys
logging.basicConfig(stream=sys.stderr)
sys.path.insert(0, '/var/www/flask_api/app')
from run import app as application
