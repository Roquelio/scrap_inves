from flask import Flask, render_template

def crear_app():
    app = Flask(__name__)
    @app.route('/')
    def home():
        return render_template('html.html')
    return app

if __name__ == '__main__':
    app = crear_app()
    app.run()