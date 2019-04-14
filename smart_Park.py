import time
import paho.mqtt.client as mqtt
import paho.mqtt.publish as publish

def check():
    global slot1;global slot2;
    print("checking")
    if(slot1==1):
        slot1=0
        return 1
    else:
        if(slot2==1):
            slot2=0
            return 2
        else:
            return 0
    
def on_connect( client, userdata, flags, rc):
    print ("Connected with Code :" +str(rc))
    client.subscribe("Park")

def on_message( client, userdata, msg):
    
    print("inside")
    print(str(msg.payload))
    if msg.payload == "getslot":
        print("searching")
        j = check()
        print(j)
        if(j==1):
            client.publish("car","1")
            print("published")
        else:
            if(j==2):
                client.publish("car","2")
            

    if msg.payload == "getslot1":
        print("searching")
        i = check()
        print(i)
        if(i==1):
            client.publish("car1","1")
        else:
            if(i==2):
                client.publish("car1","2")

        

slot1=1;
slot2=1;
client = mqtt.Client()
client.on_connect = on_connect
client.on_message = on_message
client.connect("broker.hivemq.com", 1883, 60)

# client.loop_forever()
client.loop_start()
time.sleep(1)
while True:
    #print(".")
    time.sleep(2)

client.loop_stop()
client.disconnect()
