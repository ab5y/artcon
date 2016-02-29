import sys
import os.path
# There may be a better way to do this...
# sys.path.insert(0, 'artcon_z')

from pyramid.paster import get_app, setup_logging
from artcon_z import main

ini_path = os.path.join(os.path.dirname(__file__), 'development.ini')
setup_logging(ini_path)
# application = main({})
application = get_app(ini_path, 'main')