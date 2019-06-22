import paho.mqtt.client as mqtt
import sys
import credentials

#MQTT Connection definitions: 
broker = credentials.MQTTBroker
PortaBroker = credentials.MQTTPort
KeepAliveBroker = 60
username = credentials.MQTTUsername
password = credentials.MQTTPassword

#MQTT Topics definitions:
MQTT_TOPIC = [("ledStatus",1),("temperature",1)]
topicSubscribe = "ledStatus"
topicSender = "confirmationLedStatus"

#MQTT Connect to broker function
def on_connect(client, userdata, flags, rc):
 print("[STATUS] Connecting to broker: " + str(rc))
 client.subscribe(MQTT_TOPIC)
 
#Reception callback function
def on_message(client, userdata, msg):
 MensagemRecebida = str(msg.payload)
 print("[MSG RECEIVED] Topic: " + msg.topic + " / Message: " + MensagemRecebida)
 sendMessage(topicSender,"OK")

#Send function
def sendMessage(topic, msg):
 client.publish(topic,msg)
 print("[MSG SENT] Topic: " + topic + " / Message: " + msg)
 
#Main:
try:
        print("[STATUS] Inicializando MQTT...")
        #inicializa MQTT:
        client = mqtt.Client()
        client.on_connect = on_connect
        client.on_message = on_message
        client.username_pw_set(username, password)
        client.connect(broker, PortaBroker, KeepAliveBroker)
        client.loop_forever()

except KeyboardInterrupt:
        print ("\nClosing application and exiting.")
        sys.exit(0)