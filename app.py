from flask import Flask
import os
app = Flask(__name__)

name=os.environ.get("NAME","NOT SET")
port=os.environ.get("PORT",3000)

def set_capitalize(name):
    return name.capitalize()

@app.route("/")
def capitalize():
    return f'''<html><h2>Name should be capitalized: {set_capitalize(name)}</h2>
                <h2>App should be running on port: {port}</h2></html>'''


if __name__ == "__main__":
   app.run(host="0.0.0.0",debug=True,port=port)
