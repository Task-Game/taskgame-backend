from flask import Blueprint, request, Response
from .Loja import Loja
import json
shop_bp = Blueprint('shop_bp', __name__)


@shop_bp.route('/api/v1.0/shop', methods=['GET'])
def index():
    response = Loja.index()

    return response, Response(status=200)



@shop_bp.route('/api/v1.0/shop', methods=['POST'])
def create():
    """
    Recebe um json como data e cria um novo shop no banco
    """

    return shop, Response(status=201)



@shop_bp.route('/api/v1.0/shop/<idShop>', methods=['GET'])
def show(idShop):
    request_json = request.get_json()

    idShop = request_json['data']['idShop']

    shop = Loja.show(idShop)

    return shop, Response(status=200)



@shop_bp.route('/api/v1.0/shop/<idShop>', methods=['PUT'])
def upgrade(idShop):
    request_json = request.get_json()

    idShop = request_json['data']['idShop']
    # get another request body data here

    shop = Loja.upgrade(idShop)

    return shop, Response(status=200)



@shop_bp.route('/api/v1.0/shop/<idShop>', methods=['DELETE'])
def destroy(idShop):
    request_json = request.get_json()

    idShop = request_json['data']['idShop']

    shop = Loja.destroy(idShop)

    return shop, Response(status=200)