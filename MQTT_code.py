import paho.mqtt.client as mqtt
import paho.mqtt.publish as publish
import time
import RPi.GPIO as IO
import Adafruit_ADXL345


def detect():
    while True:
        i=ir()
        j=acc()
        if(i==1):
            return 1
        if(j==2):
            return 2
        print(IO.input(21))
        if(IO.input(21)==1):
            a=input("Reached Parking Zone ?\n 1.Yes 2.No\nEnter Option 1/2")
            if(a==1):
                return 3
            if a==2:
                client.publish("Broker","recheck")
                return 0;
        
                    
        
def acc():
    #while True:
    x, y, z = accel.read()
    print('X={0}, Y={1}, Z={2}'.format(x, y, z))
    time.sleep(0.5)
    if(x>200):
        return 2
    if(x<-200):
        return 2
    if(y>200):
        return 2
    if(y<-200):
        return 2
    
    
    
def ir():
    #while 1:
    if(IO.input(18)==False):
        #print("Object detetced")
        return 1

def on_connect(client, userdata , flags , rc):
    print("Connected with the code "+str(rc))
    client.subscribe("car")
    print("\nsubcribed to car")



def on_message(client, userdata, msg):
    #print(msg.topic +  " " + str(msg.payload))
    global cnt;
    print("Inside on_message")
    print(str(msg.payload))
    time.sleep(2)

    if msg.payload =="1":
        print("Slot 1 is empty")
        return
    else:
        if msg.payload =="2":
            print("Slot 2 is empty")
            return
    
    if msg.payload == "getinfo":
        i=detect()
        if(i==1):
            client.publish("Broker","object")
            i=0

        if(i==2):
            client.publish("Broker","accident")
            print("Published accident")
            i=0
        if(i==3):
            client.publish("Park","getslot")
            print("published")
            time.sleep(2)
            
            

    if msg.payload == "ir":
        print("Object ahead, Go slow")
        time.sleep(1)
        client.publish("car1","ir")
        client.publish("Broker","recheck")
        

    if msg.payload == "acc":
        print("Ambulance Urgency")
        time.sleep(1)
        client.publish("Broker","recheck")
        

i=0
cnt=0
IO.setwarnings(False)
IO.setmode(IO.BCM)
IO.setup(18,IO.IN)
IO.setup(21,IO.IN)
accel = Adafruit_ADXL345.ADXL345()

client = mqtt.Client()
client.on_connect = on_connect
client.on_message = on_message
client.connect("broker.hivemq.com", 1883)

# client.loop_forever()
client.loop_start()
time.sleep(1)
print("getting")
while True:
    cnt=cnt+1
    #print("cnt=",cnt)
    #print(IO.input(21))
    time.sleep(0.1)

client.loop_stop()
client.disconnect()
