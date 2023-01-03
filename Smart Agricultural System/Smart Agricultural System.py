import sys
import time
import ibmiotf.application # to install pip install ibmiotf
import ibmiotf.device

#Provide your IBM Watson Device Credentials
organization = "9wbx5m" 
deviceType = "iotdevice1"
deviceId = "qwerty123"
authMethod = "token"
authToken = "apple" 

def myCommandCallback(cmd): 
        print("Command received: %s" % cmd.data)
        if cmd.data['command']=='ON':
                print("MOTOR ON IS RECEIVED")
                time.sleep(1)
                print("MOTOR STARTED")
                          
        elif cmd.data['command']=='OFF':
                print("MOTOR OFF IS RECEIVED")
                time.sleep(1)
                print("MOTOR STOPPED")
                
        
        elif cmd.data['command']=='runfor30minutes':
                print("MOTOR RUNS FOR 30 MINUTES")
                print("MOTOR STARTED")
                for i in range(1,31):
                    print("%d minutes to stop"%(30-i)) 
                print("MOTOR STOPPED")
        
        
        if cmd.command == "setInterval":
                
                if 'interval' not in cmd.data:
                        print("Error - command is missing required information: 'interval'")
                else:
                        interval = cmd.data['interval']
        elif cmd.command == "print":
                if 'message' not in cmd.data:
                        print("Error - command is missing required information: 'message'")
                else:
                        output=cmd.data['message']
                        print(output)

try:
	deviceOptions = {"org": organization, "type": deviceType, "id": deviceId, "auth-method": authMethod, "auth-token": authToken}
	deviceCli = ibmiotf.device.Client(deviceOptions)
	
except Exception as e:
	print("Caught exception connecting device: %s" % str(e))
	sys.exit()

deviceCli.connect()

while True:
        deviceCli.commandCallback = myCommandCallback

deviceCli.disconnect()