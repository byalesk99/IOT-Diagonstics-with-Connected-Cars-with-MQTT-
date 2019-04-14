import paho.mqtt.client as mqtt
import paho.mqtt.publish as publish
import time

def on_connect(client, userdata , flags , rc):
    print("Connected with the code "+str(rc))
    client.subscribe("car1")
    print("\nsubcribed to car1")



def on_message(client, userdata, msg):
    #print(msg.topic +  " " + str(msg.payload))
    global cnt;
    print("Inside on_message")
    if msg.payload=="ir":
        print("Crash Alert, Keep safe distance")
    if msg.payload == "getinfo1":
        i= IO.input(21)
        if(i==1):
            a=input("Reached Parking Zone ?\n 1.Yes 2.No\nEnter Option 1/2")
            if(a==1):
                client.publish("Park","getslot1")
    if msg.payload =="1":
        print("Slot 1 is empty")
        return
    else:
        if msg.payload =="2":
            print("Slot 2 is empty")
            return

i=0
cnt=0
client = mqtt.Client()
client.on_connect = on_connect
client.on_message = on_message
client.connect("broker.hivemq.com", 1883, 60)

# client.loop_forever()
client.loop_start()
time.sleep(1)
print("getting")
while True:
    
    time.sleep(1)

client.loop_stop()
#client.disconnect()
