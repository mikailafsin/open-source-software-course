from flask import Flask

myflaskapp = Flask(__name__)

@myflaskapp.route("/")
def hello():
    return """
    <!DOCTYPE html>
    <html lang="en">
    <head>
        <meta charset="UTF-8">
        <meta name="viewport" content="width=device-width, initial-scale=1.0">
        <title>Benim Flask Servisim</title>
    </head>
    <body style="display: flex; align-items: center; justify-content: center; min-height: 100vh">
        <p style="font-size: 2rem; font-family: 'Courier New', monospace">Projeme hizmet edecek olan Gunicorn ornegi</p>
    </body>
    </html>
    """

if __name__ == "__main__":
    myflaskapp.run(host='0.0.0.0')

