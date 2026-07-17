from flask import Flask

app = Flask( name)

@app.route("/")

def home ():

return "Hello from Render PaaS"

@app.route ("/about")

def about():

return "This is About Page"

if name == " main ":

import os

port = int (os.environ.get("PORT", 10000)) app.run (host="0.0.0.0", port=port)