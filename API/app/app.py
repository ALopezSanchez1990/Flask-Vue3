from flask import Flask
from db.db import create_tables
from route.articulo import article_route
from route.categoria import categoria_route

app= Flask(__name__)
app.register_blueprint(article_route)
app.register_blueprint(categoria_route)

@app.route("/")
def hello_world():
    return "<p>Hello, World!</p>"

if __name__ == '__main__':
    create_tables()
    app.run('0.0.0.0', 5000, debug=True)
