"""
The flask application package.
"""

from flask import Flask
app = Flask(__name__)

import Entertainment_Hub.views
import Entertainment_Hub.viewcontroller2
