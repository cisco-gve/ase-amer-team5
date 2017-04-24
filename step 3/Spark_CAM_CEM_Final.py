import json
import requests
import time

ACCESS_TOKEN_BOT = "<YOUR_BOT_TOKEN>"
ACCESS_TOKEN = "YOUR_TOKEN" # This token is most probably not needed.

roomID = '<YOUR_ROOM_ID>'

#sets the header to be used for authentication and data format to be sent.
def setHeaders():
	accessToken_hdr = 'Bearer ' + ACCESS_TOKEN
	spark_header = {'Authorization': accessToken_hdr, 'Content-Type': 'application/json; charset=utf-8'}
	return (spark_header)

def setHeaders_bot():
	accessToken_hdr = 'Bearer ' + ACCESS_TOKEN_BOT
	spark_header = {'Authorization': accessToken_hdr, 'Content-Type': 'application/json; charset=utf-8'}
	return (spark_header)

# creates a new room and returns the room id.
# Mission:  Add code to parse and return the room id
def createRoom(the_header,room_name):
	roomInfo = '{"title" :"' + room_name + '"}'
	uri = 'https://api.ciscospark.com/v1/rooms'
	resp = requests.post(uri, data=roomInfo, headers=the_header)
	var = resp.json()
	room_id =  var['id']
	print room_id
	return room_id
	#print("createRoom JSON: ", var)
	#MISSION: ADD CODE HERE TO PARSE AND RETURN THE ROOM ID.


# adds a new member to the room.  Member e-mail is test@test.com
def addMembers(the_header,roomId):
	member = '{"roomId":"' + roomId + '","personEmail": "<YOUR_EMAIL>", "isModerator": false}'
	uri = 'https://api.ciscospark.com/v1/memberships'
	resp = requests.post(uri, data=member, headers=the_header)
	#print("addMembers JSON: ", resp.json())

# #posts a message to the room
def postMsg(the_header,roomId,message):
	message = '{"roomId":"' + roomId + '","text":"'+message+'"}'
	uri = 'https://api.ciscospark.com/v1/messages'
	resp = requests.post(uri, data=message, headers=the_header)
	print("postMsg JSON: ", resp.json())

#MISSION: WRITE CODE TO RETRIEVE AND DISPLAY DETAILS ABOUT THE ROOM.
def getRoomInfo(the_header,roomId):
	print("In function getRoomInfo")

def getRoomMessages(theHeader):
	uri = 'https://api.ciscospark.com/v1/messages?roomId=' + roomID
	resp = requests.get(uri, headers=theHeader)
	var =  resp.json()
	message = var['items'][0]['text']
	return message

def CEM(message):
    url = "https://<YOUR_IP_ADDRESS>/api/3.0/login"

    response = requests.post('https://<YOUR_IP_ADDRESS>/api/3.0/login?username=<YOUR_USERNAME>&password=<YOUR_PASSWORD>', verify=False)

    parsed = json.loads(response.content)
    authCEM = parsed['result']['auth']

    url = "https://<YOUR_IP_ADDRESS_CEM>/api/3.0/management/tenants"

    headers = {
    'x-jem-auth': authCEM,
    'content-type': "application/json",
    'cache-control': "no-cache",
    'postman-token': "6a7c135c-8ccb-f1a2-0d51-c7b927a9eaa8"
    }

    requestCEM = requests.request("GET", url, headers=headers, verify=False)

    reqParsedCEM = json.loads(requestCEM.content)
    reqDumpsCEM = json.dumps(reqParsedCEM, indent=2)

    deviceCustCEM = reqParsedCEM['result']['uiLicense']['customer']
    deviceCountCEM = reqParsedCEM['result']['uiLicense']['deviceCount']
    deviceSubTotCEM = reqParsedCEM['result']['uiLicense']['deviceCounts']['types']

    if 'CEM Customer' in message:
    	return deviceCustCEM
    elif 'CEM Count' in message:
	return str(deviceCountCEM)
    elif 'CEM Devices' in message:
		str(deviceSubTotCEM).replace("{","")
		str(deviceSubTotCEM).replace("}","")
		str(deviceSubTotCEM).replace("\':",":")
		str(deviceSubTotCEM).replace("u\'","")
		str(deviceSubTotCEM).replace(",","\n")
	return str(deviceSubTotCEM)
    else:
	print "Nothing"

def CAM(message):
    url = "https://<YOUR_IP_ADDRESS_CAM>/api/3.0/login"

    response = requests.post('https://<YOUR_IP_ADDRESS_CAM>/api/3.0/login?username=<YOUR_USERNAME>&password=<YOUR_USERNAME>', verify=False)

    parsed = json.loads(response.content)
    authCAM = parsed['result']['auth']

    url = "https://<YOUR_IP_ADDRESS_CAM>/api/3.0/management/tenants"

    headers = {
    'x-jem-auth': authCAM,
    'content-type': "application/json",
    'cache-control': "no-cache",
    'postman-token': "6a7c135c-8ccb-f1a2-0d51-c7b927a9eaa8"
    }

    requestCAM = requests.request("GET", url, headers=headers, verify=False)

    reqParsedCAM = json.loads(requestCAM.content)
    reqDumpsCAM = json.dumps(reqParsedCAM, indent=2)

    deviceCustCAM = reqParsedCAM['result']['uiLicense']['customer']
    deviceCountCAM = reqParsedCAM['result']['uiLicense']['deviceCount']
    deviceSubTotCAM = reqParsedCAM['result']['uiLicense']['deviceCounts']['types']

    if 'CAM Customer' in message:
        return str(deviceCustCAM)
    elif 'CAM Count' in message:
        return str(deviceCountCAM)
    elif 'CAM Devices' in message:
    	return str(deviceSubTotCAM)
    else:
        print "Nothing"



if __name__ == '__main__':

    while True:
	print "3 sec"
    	header = setHeaders()
    	message = getRoomMessages(header)

   	if 'CEM' in message:
    	    postMsg(setHeaders_bot(), roomID, CEM(message))
    	elif 'CAM' in message:
	    postMsg(setHeaders_bot(), roomID, CAM(message))
    	else:
	    print "Nothing"
	time.sleep(3)
