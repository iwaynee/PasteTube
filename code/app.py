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
@route('/CreateUser')
def index():
    # Create UserId
    userid = uuid.uuid4().hex

    # Add User
    userdict[userid] = {
        "devices" : [],
        "data" : None
    }

    response = {
        "status": 0x01,
        "user-id": userid
    }

    return response

# Connect #############################################################################################################
@get("/Connect")
def index():
    # Get MAC
    mac_adress = request.params.get("mac")
    if mac_adress == None:
        response = { "status" : 0x02,
                     "error" : "No Mac-Adress"}

        return response

    # Get UserId
    userid = request.params.get("userid")
    if userid == None:
        response = { "status" : 0x03,
                     "error" : "No UserId"}

        return response

    # Check if Userid is in Database
    if userid not in userdict.keys():
        response = { "status" : 0x04,
                     "error" : "UserId is not in Database"}

        return response

    # Check if this Device is already connected
    devices = userdict[userid]["devices"]
    for device in devices:
        if device["ip"] == request.remote_addr and device["mac"] == mac_adress:
            response = {"status": 0x05,
                        "error": "Device already in Database"}

            return response

    userdict[userid]["devices"].append({
        "ip": request.remote_addr,
        "mac": mac_adress
    })

    response = {
        "status": 0x01
    }

    return response

# GetConnectedDevices #################################################################################################
@get("/GetConnectedDevices")
def index():
    # Get UserId
    userid = request.params.get("userid")
    if userid == None:
        response = { "status" : 0x03,
                     "error" : "No UserId"}

        return response

    # Check if Userid is in Database
    if userid not in userdict.keys():
        response = { "status" : 0x04,
                     "error" : "UserId is not in Database"}

        return response

    response = { "status" : 0x01,
                 "devices" : userdict[userid]["devices"]}

    return response

# Copy ################################################################################################################
@get("/Copy")
def index():
    # Get UserId
    userid = request.params.get("userid")
    if userid == None:
        response = { "status" : 0x03,
                     "error" : "No UserId"}

        return response

    # Get Data
    data = request.params.get("data")
    if data == None:
        response = { "status" : 0x05,
                     "error" : "No Data in request"}

    userdict[userid]["data"] = data

    response = { "status" : 0x01}

    return response


# Paste ################################################################################################################
@get("/Paste")
def index():
    # Get UserId
    userid = request.params.get("userid")
    if userid == None:
        response = {"status": 0x03,
                    "error": "No UserId"}

        return response

    response = {"status": 0x01,
                "data" : userdict[userid]["data"]}

    return response

if __name__ == '__main__':
    # Get required port, default to 5000.
    port = os.environ.get('PORT', 8080)

    # Run the app.
    run(host='0.0.0.0', port=port)