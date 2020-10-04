import logging, sys
logging.basicConfig(stream=sys.stderr)
sys.path.insert(0, '/var/www/flask_api')
from run import app as application