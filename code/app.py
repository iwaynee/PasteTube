import os
from bottle import route, run, get, request
import uuid


userdict = {}


errors = {
    0x01: "Success",
    0x02: "No Mac-Adress",
    0x03: "No UserId in request",
    0x04: "UserId is not in Database",
    0x05: "Device already in Database",
    0x06: "No Data in request",
    0x07: "Device is not connectd yet"
}


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
        "state": 0x01,
        "userid": userid
    }

    return response

# Connect #############################################################################################################
@get("/Connect")
def index():
    # Get MAC
    mac_adress = request.params.get("mac")
    if mac_adress == None:
        response = { "state" : 0x02,
                     "error" : errors[0x02]}

        return response

    # Get UserId
    userid = request.params.get("userid")
    if userid == None:
        response = { "state" : 0x03,
                     "error" : errors[0x03]}

        return response

    # Check if Userid is in Database
    if userid not in userdict.keys():
        response = { "state" : 0x04,
                     "error" : errors[0x04]}

        return response

    # Check if this Device is already connected
    devices = userdict[userid]["devices"]
    for device in devices:
        if device["ip"] == request.remote_addr and device["mac"] == mac_adress:
            response = {"state": 0x05,
                        "error": errors[0x05]}

            return response

    userdict[userid]["devices"].append({
        "ip": request.remote_addr,
        "mac": mac_adress
    })

    response = {
        "state": 0x01
    }

    return response

# GetConnectedDevices #################################################################################################
@get("/GetConnectedDevices")
def index():
    # Get UserId
    userid = request.params.get("userid")
    if userid == None:
        response = { "state" : 0x03,
                     "error" : errors[0x03] }

        return response

    # Check if Userid is in Database
    if userid not in userdict.keys():
        response = { "state" : 0x04,
                     "error" : errors[0x04]}

        return response

    response = { "state" : 0x01,
                 "devices" : userdict[userid]["devices"]}

    return response

# Copy ################################################################################################################
@get("/Copy")
def index():
    # Get UserId
    userid = request.params.get("userid")
    if userid == None:
        response = { "state" : 0x03,
                     "error" : errors[0x03]}

        return response

    # Check if connected
    connected = False
    devices = userdict[userid]["devices"]
    for device in devices:
        if device["ip"] == request.remote_addr:
            connected = True

    if connected == False:
        response = {"state": 0x07,
                    "error": errors[0x07]}

        return response

    # Get Data
    data = request.params.get("data")
    if data == None:
        response = { "state" : 0x06,
                     "error" : errors[0x06]}

        return response

    userdict[userid]["data"] = data

    response = { "state" : 0x01}

    return response


# Paste ################################################################################################################
@get("/Paste")
def index():
    # Get UserId
    userid = request.params.get("userid")
    if userid == None:
        response = {"state": 0x03,
                    "error": 0x03}

        return response

    response = {"state": 0x01,
                "data" : userdict[userid]["data"]}

    return response



# DEBUG ONLY!!! ########################################################################################################
@get("/Debug")
def index():
    response = ""

    for i in userdict.keys():
        response += "User ID : " + i + "<br>" \
                    "_____________________ <br>" + str(userdict[i]["data"]) + "<br><br>"



    return response


if __name__ == '__main__':
    # Get required port, default to 5000.
    port = os.environ.get('PORT', 8080)

    # Run the app.
    run(host='0.0.0.0', port=port)