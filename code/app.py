import os
from bottle import route, run, get, request
import uuid
import json


userdict = {}


# HomeSite ############################################################################################################
@route('/')
def index():

    html = '<!DOCTYPE html>' \
           '<html>' \
           '<head>' \
           '<title>PasteTube</title>' \
           '</head>' \
           '<body>' \
           '<p>No public Website - PasteTube Team</p>' \
           '</body>'

    return html

# CreateUser ##########################################################################################################
@route('/CreateUser/')
def index():
    # Create UserId
    userid = uuid.uuid4().hex

    # Add User
    userdict[userid] = "Created"


    response = {
        "status": 0x01,
        "user-id": userid
    }

    return response

# Connect #############################################################################################################
@get("/Connect/")
def index():
    # Get MAC
    var = request.params.get("test")

    print(request.remote_addr)

    print(var)

    return var


if __name__ == '__main__':
    # Get required port, default to 5000.
    port = os.environ.get('PORT', 8080)

    # Run the app.
    run(host='localhost', port=port)