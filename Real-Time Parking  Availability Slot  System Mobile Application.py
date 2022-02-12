import paho.mqtt.client as mqtt
import time
def on_connect(client, userdata, flags, rc):
    if rc == 0:
        print("Connected to broker")
    else:
        print("Connection failed")
def on_message(client, userdata, msg):
    global distance1 ,distance2
    if msg.topic == "distance_1":
        distance1 = int(msg.payload)
    if msg.topic == "distance_2":
        distance2 = int(msg.payload)

client = mqtt.Client("Python")
client.username_pw_set(username="mymqtt",password="jc1997")
print("Connecting...")
client.connect("israngkul.ddns.net", 1883,10)


client.on_connect= on_connect
client.on_message= on_message
distance1 = client.subscribe("distance_1")
distance2 = client.subscribe("distance_2")
client.loop_start()

try:
    while True:
        if distance1 == 1:
            parkslot_1 = 0
        elif distance1 == 2:
            parkslot_1 = 0
        elif distance1 == 3:
            parkslot_1 = 0
        elif distance1 == 4:
            parkslot_1 = 0
        elif distance1 == 5:
            parkslot_1 = 0
        elif distance1 == 6:
            parkslot_1 = 0
        elif distance1 == 7:
            parkslot_1 = 0
        elif distance1 == 8:
            parkslot_1 = 0
        elif distance1 == 9:
            parkslot_1 = 0
        elif distance1 == 10:
            parkslot_1 = 0
        else:
            parkslot_1 = 1
        client.publish("parkstatus_1", parkslot_1)
        if distance2 == 1:
            parkslot_2 = 0
        elif distance2 == 2:
            parkslot_2 = 0
        elif distance2 == 3:
            parkslot_2 = 0
        elif distance2 == 4:
            parkslot_2 = 0
        elif distance2 == 5:
            parkslot_2 = 0
        elif distance2 == 6:
            parkslot_2 = 0
        elif distance2 == 7:
            parkslot_2 = 0
        elif distance2 == 8:
            parkslot_2 = 0
        elif distance2 == 9:
            parkslot_2 = 0
        elif distance2 == 10:
            parkslot_2 = 0
        else:
            parkslot_2 = 1
        client.publish("parkstatus_2", parkslot_2)
        time.sleep(1)
except KeyboardInterrupt:
    print("exiting")
client.disconnect()
client.loop_stop()