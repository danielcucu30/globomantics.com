#!/user/bin/env python
"""
A simple Flaz web app that demonstartaes MODEL VIEW CONTROLLER

"""

from flask import Flask, render_template , request
from database import Database


app = Flask(__name__)

#path = "data/db.json"
#path = "data/db.yml"
path = "data/db.xml"
db = Database(path) # send the path to  database.py


@app.route("/", methods=["GET", "POST"])
def index():
    """
    This is a view function which responds to request for the top-level URL
    It serves as the "controler" in MVC as it accesses both the model and the view
    """
    if request.method == "POST":
        # This collects the user input from the view. The controler will process the info
        # that will include methods from the model to get that info (account balance) 
        acct_id = request.form ["acctid"]
        acct_balance = db.balance (acct_id.upper())
        app.logger.debug(f"bakance for the{acct_id}: {acct_balance}")
    else:
        #during a normal Get request no need to do calculations
        acct_balance = "N/A"
        # this is the view which is a HTML template data that is presented to the user.
        # the user interacts with this webpage  and provides info to the controler then process. The 
        #controller passes the info back to the view so  it can be displayed to the user
   
    return render_template("index.html", acct_balance=acct_balance)
if __name__ == "__main__":
    app.run(host="0.0.0.0", debug=True)
