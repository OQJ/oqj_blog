from flask import Flask
import config

app = Flask(__name__)

app.secret_key = config.secret_key

from routes.index import main as index_routes
app.register_blueprint(index_routes)

if __name__ == '__main__':
    config = dict(
        debug=True,
        host='127.0.0.1',
        port=5000,
    )
    app.run(**config)