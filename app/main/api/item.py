from flask import Blueprint, request, make_response
from ..service.item import retrieve_item, create_item, remove_item

item_bp = Blueprint('item_bp', __name__)

@item_bp.route('/', methods=['GET'])
def get_item():
    print(request.headers)
    if len(request.headers['authorization'].split()[1]) != 20:
        return 'Unauthorized', 401
    args = request.args
    if 'name' not in args:
        return 'Missing name parameter', 400
    try:
        return retrieve_item(args.get('name')), 200
    except NameError as e:
        return {}, 204


@item_bp.route('/', methods=['POST'])
def post_item():
    if len(request.headers['authorization'].split()[1]) != 20:
        return 'Unauthorized', 401
    args = request.args
    if 'name' not in args:
        return 'Missing name parameter', 400
    if 'price' not in args:
        return 'Missing price parameter', 400
    try:
        create_item(args.get('name'), args.get('price'))
        return "Success, item added", 201
    except NameError as e:
        # do nothing, if we wanted to update the item we should be using a PUT request
        return "Item already exists", 409
     

@item_bp.route('/', methods=['DELETE'])
def delete_item():
    if len(request.headers['authorization'].split()[1]) != 20:
        return 'Unauthorized', 401
    args = request.args
    if 'name' not in args:
        return 'Missing name parameter', 400
    try:
        remove_item(args.get('name'))
        return "Success, item deleted", 204
    except NameError as e:
        return "Item was not found and cannot be deleted", 404