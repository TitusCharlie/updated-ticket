# from app import app as application
import os
import sys
import imp

sys.path.insert(0, os.paht.dirname(__file__))

wsgi = imp.load_source('wsgi', 'app.py')

application = wsgi.app
