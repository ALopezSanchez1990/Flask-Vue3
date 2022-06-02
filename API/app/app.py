from flask import Flask
from flask_cors import CORS
from db.db import create_tables
from route.articulo import article_route
from route.categoria import categoria_route

app= Flask(__name__)
app.register_blueprint(article_route)
app.register_blueprint(categoria_route)

# enable CORS
CORS(app, resources={r'/*': {'origins': '*'}})
app.config['CORS_HEADERS'] = 'Content-Type'

@app.route("/")
def hello_world():
    return "<p>Hello, World!</p>"

if __name__ == '__main__':
    create_tables()
    app.run('0.0.0.0', 5000, debug=True)
