from flask import Flask, render_template
import os

def crear_app():
    app = Flask(__name__)

    @app.route('/')
    def home():
        return render_template('html.html')

    return app

app = crear_app()

if __name__ == '__main__':
    port = int(os.environ.get("PORT", 5000))
    app.run(host='0.0.0.0', port=port)
