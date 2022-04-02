""" For convenience; redirects the root page to /item. Can easily be changed later
"""
from flask import Blueprint, redirect

root_bp = Blueprint('root_bp', __name__)

@root_bp.route('/')
def redirect_to_item():
    return redirect('/item')