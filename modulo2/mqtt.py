import paho.mqtt.client as mqtt
import time

servidor = "broker.mqtt.cool"
cliente = mqtt.Client(protocol=mqtt.MQTTv5)

cliente.connect(servidor, 1883)

# --------------------------------------------------------------
while True:
    cliente.publish("DesafioI40","Mensaje desde Python")
    time.sleep(1)