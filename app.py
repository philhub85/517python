from flask import Flask
def create_app():
    app = Flask(__name__)
    @app.route('/')
    def hello_world():
        return 'Hello, this is the app for 5/17/22!'
    return app
app = create_app()
