""" This file is representative of a middleware. Here, we create an instance of our app. For a small site one instance might be enough but for future scaling we'd like to be able to create multiple instances of our app.
"""
from app import init_app


app = init_app()

if __name__ == "__main__":
    app.run()