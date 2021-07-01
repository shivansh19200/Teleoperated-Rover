from paho.mqtt import client as mqtt_client
from tkinter import *
import tkinter.font as font

#Creating windows
root=Tk()
root.title("Rover Control App")

broker = 'mqtt.flespi.io'
port = 1883
client_id = 'ss-9082351597'
username = "KmjvpeomwKOcdbC0NLa1t5aiXMsYDWKb6RvmTJwgh9gkaI9Nh7CB2CJOeZAGL8FI"
password = ''


def reconnect(client, userdata, flags, rc):
    print("Connected with result code " + str(rc))
    # Subscribing in on_connect() means that if we lose the connection and reconnect then subscriptions will be renewed.
    client.subscribe("Rover/Connect")

def callback(client, userdata, msg):
    print(msg.topic + " " + str(msg.payload))


client = mqtt_client.Client(client_id)
client.on_connect = reconnect
client.on_message = callback
client.username_pw_set(username, password)
client.connect(broker, port)
print('Mqtt Connection Established')
#Function for publishing value of slider
def slider1(val):
    client.publish("roverSpeed", str(val))

button_font = font.Font(size= "10", weight='bold')

headerButton1 = Button(root, text="Speed Control", font=button_font, bg="black",fg="white")
headerButton1.pack()

slider = Scale(root, from_=0, to=255, orient=HORIZONTAL, length=400, tickinterval="50",command=slider1)
slider.pack()

#Function to publish message according
def controlDirection(dir):
    print("Moving in "+dir+" direction")
    client.publish("roverMovement", dir)

headerButton2 = Button(root, text="Direction Control", font=button_font, bg="black",fg="white")
headerButton2.pack(pady="15")
btn1=Button(root , text="🔺" ,bg="blue", fg="white",width="15", height="5",font=button_font ,command=lambda:controlDirection("Forward"))
btn2=Button(root , text="🔻" ,bg="blue", fg="white",width="15", height="5", font=button_font ,command=lambda:controlDirection("Backward"))
btn3=Button(root , text="RIGHT" , bg="blue", fg="white",width="15", height="5",font=button_font ,command=lambda:controlDirection("Right"))
btn4=Button(root , text="LEFT" , bg="blue", fg="white",width="15", height="5",font=button_font ,command=lambda:controlDirection("Left"))
btn5=Button(root , text="🛑" , bg="blue", fg="white",width="15", height="5",font=button_font ,command=lambda:controlDirection("STOP"))

btn1.pack(side="top",pady="10")
btn2.pack(side="bottom",pady="10")
btn3.pack(side="right",padx="10")
btn4.pack(side="left",padx="10")
btn5.pack()
mainloop()

while (1):
    client.loop()

client.disconnect()