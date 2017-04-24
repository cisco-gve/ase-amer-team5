import json
import requests
import time

ACCESS_TOKEN_BOT = "NmRkOTVlNjUtMTUxNy00MDcyLTk5MzAtNTJjOWRjMWM2MDFiMDcwN2E2NWUtYjE5"
ACCESS_TOKEN = "Mzg1OGExNTctMGQ3ZS00ODdiLTkwZTItY2U0OGY5OTdiOGYyMmZhZTljNDAtNzNh" #put your access token here between the quotes.

roomID = 'Y2lzY29zcGFyazovL3VzL1JPT00vZGQxYmYzMTAtMDgwMy0xMWU3LWEwZTAtMDdiM2EwMmE2OTVj'

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

# adds a new member to the room.  Member e-mail is test@test.com
def addMembers(the_header,roomId):
	member = '{"roomId":"' + roomId + '","personEmail": "<YOUR_EMAIL>", "isModerator": false}'
	uri = 'https://api.ciscospark.com/v1/memberships'
	resp = requests.post(uri, data=member, headers=the_header)


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

    response = requests.post('https://<YOUR_CEM_IP>/api/3.0/login?username=<YOUR_USERNAME>&password=YOUR_PASSWORD', verify=False)

    parsed = json.loads(response.content)
    authCEM = parsed['result']['auth']

    url = "https://<YOUR_CEM_IP>/api/3.0/management/tenants"
    
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
    deviceTotCEM = reqParsedCEM['result']['uiLicense']['deviceCounts']['devices']
	
    if 'CEM Customer' in message:
    	return deviceCustCEM
    elif 'CEM Count' in message:
	return str(deviceCountCEM)
    elif 'CEM Devices' in message:
	temp = str(deviceSubTotCEM)
	temp = temp.replace("{","")
	temp = temp.replace("}","")
	temp = temp.replace("\':",":")
	temp = temp.replace("u\'","")
	temp = temp.replace(",","\\n")
	return temp
    elif 'CEM Total' in message:
	return str(deviceTotCEM)
    else:
	print "Nothing"

def CAM(message):

    response = requests.post('https://<YOUR_CAM_IP>/api/3.0/login?username=<YOUR_USERNAME>&password=<YOUR_PASSWORD>', verify=False)

    parsed = json.loads(response.content)
    authCAM = parsed['result']['auth']

    url = "https://<YOUR_CAM_IP>/api/3.0/management/tenants"

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
    deviceTotCAM = reqParsedCAM['result']['uiLicense']['deviceCounts']['devices']

    if 'CAM Customer' in message:
        return str(deviceCustCAM)
    elif 'CAM Count' in message:
        return str(deviceCountCAM)
    elif 'CAM Devices' in message:
    	temp = str(deviceSubTotCAM)
        temp = temp.replace("{","")
        temp = temp.replace("}","")
	temp = temp.replace("'':","nknown devices:")
        temp = temp.replace("\':",":")
        temp = temp.replace("u\'","")
        temp = temp.replace(",","\\n")
	return temp
    
    elif 'CAM Total' in message:
	return str(deviceTotCAM)
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
