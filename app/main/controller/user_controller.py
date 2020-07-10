from flask import request
from flask_restplus import Resource

from ..utils.dto_objects import UserDto
from ..logic.user_service import *

api = UserDto.api
_user = UserDto.user