"""
Main module of the server file
"""

# 3rd party moudles
from flask import render_template, redirect

# local modules
import config  # personal config

# Get the application instance
app = config.connex_app

# Read the swagger.yml file to configure the endpoints
app.add_api('swagger.yml')

# Create a URL route in our application for "/"
@app.route("/")
def home():
    """
    This function just responds to the browser URL
    localhost:5000/

    @return@ auto redirect to swagger.ui
    """
    response = redirect("api/ui", code=302)
    headers = dict(response.headers)
    response.headers = headers
    return response


def startUp():
    print("Started App")


# If we're running in stand alone mode, run the application
if __name__ == '__main__':
    startUp()
    app.run(host='0.0.0.0', port=5000, debug=True)
