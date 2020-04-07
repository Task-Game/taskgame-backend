from flask import Response, make_response, jsonify
from manager import db
from datetime import datetime

import json


class Metas():
    def __init__(self):