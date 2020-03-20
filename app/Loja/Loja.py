from flask import Response, make_response, jsonify
from manager import db
from datetime import datetime

import json


class Loja():
    def __init__(self):