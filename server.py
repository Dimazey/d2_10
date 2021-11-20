import os
from bottle import Bottle
import sentry_sdk
from sentry_sdk.integrations.bottle import BottleIntegration
from sentry_config import sentry_token

sentry_sdk.init(
    dsn=sentry_token,
    integrations=[BottleIntegration()]
    )

APP = Bottle()
@APP.route("/")
def index():
    html = """
<!DOCTYPE html>
<html lang="en">
<head>
    <meta charset="UTF-8">
    <link rel="icon" href="http://favicon.ico" type="image/ico">
    <title>main page</title>
    </head>
  <body>
  <div class="container">
      <a href="/success">маршрут https:/you-application.herokuapp.com/success вернет ответ - Status 200 OK</a>
    <br><br>
    <a href="/fail">маршрут https:/you-application.herokuapp.com/fail вызовет ошибку сервера</a>
    </div>
   
  </body>
</html>
"""
    return html

@APP.route("/success")
def success():
    html = """
   <!DOCTYPE html>
    <html lang="en">
    <link rel="icon" href="http://favicon.ico" type="image/ico">
    <head>
    <meta charset="UTF-8">
    <meta name="viewport" content="width=device-width, initial-scale=1.0">
    <title>Status 200</title>
    </head>
    <body>
    <div class="container">
    <h1>Status 200 OK</h1>
     </div>
    </body>
    </html>
    """
    return html

@APP.route("/fail")
def fail():
    raise RuntimeError('Error for Error')

if os.environ.get('APP_LOCATION') == 'heroku':
    APP.run(host="0.0.0.0",
        port=int(os.environ.get("PORT", 5000)))
else:
    APP.run(host='localhost', port=8080, debug=True)
