import time
import paho.mqtt.client as mqtt
import paho.mqtt.publish as publish

# Callback Function on Connection with MQTT Server
def on_connect( client, userdata, flags, rc):
    print ("Connected with Code :" +str(rc))
    # Subscribe Topic from here
    client.subscribe("Broker")

# Callback Function on Receiving the Subscribed Topic/Message
def on_message( client, userdata, msg):
    # print the message received from the subscribed topic
    print("inside")
    print(str(msg.payload))
    if msg.payload == "recheck":
        print("rechecking")
        client.publish("car1","getinfo1")
        client.publish("car","getinfo")

    if msg.payload == "object":
        client.publish("car","ir")

    if msg.payload == "accident":
        print("Yogesh")
        #publish.single("Yo1","Accident Case",hostname="broker.hivemq.com")
        client.publish("car","acc")
        print("published acc")
        

client = mqtt.Client()
client.on_connect = on_connect
client.on_message = on_message
client.connect("broker.hivemq.com", 1883, 60)
client.publish("car","getinfo")
#client.publish("car1","getinfo1")
# client.loop_forever()
client.loop_start()
#client.publish("car","getinfo")
while True:
    time.sleep(0.1)
    #client.publish("car1","getinfo1")
client.loop_stop()
client.disconnect()
