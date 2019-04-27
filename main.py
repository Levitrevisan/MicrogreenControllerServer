import paho.mqtt.client as mqtt
import sys

#definitions: 
Broker = "m16.cloudmqtt.com"
PortaBroker = 10746
KeepAliveBroker = 60
topicSubscribe = "ledStatus"
topicSender = "confirmationLedStatus"
username = "paiqlirh"
password = "V4ig-DwmZsCA"
#Relate mqtt topic reception to callback fuction
def on_connect(client, userdata, flags, rc):
    print("[STATUS] Connecting to broker: " + str(rc))
 
    #subscribe to led status topic
    client.subscribe(topicSubscribe)
 
#Callback function
def on_message(client, userdata, msg):
 MensagemRecebida = str(msg.payload)
 print("[MSG RECEIVED] Topic: " + msg.topic + " / Message: " + MensagemRecebida)
 sendMessage(topicSender,"OK")

#Send function
def sendMessage(topic, msg):
 client.publish(topic,msg)
 print("[MSG SENT] Topic: " + topic + " / Message: " + msg)
 
#programa principal:
try:
        print("[STATUS] Inicializando MQTT...")
        #inicializa MQTT:
        client = mqtt.Client()
        client.on_connect = on_connect
        client.on_message = on_message
        client.username_pw_set(username, password)
        client.connect(Broker, PortaBroker, KeepAliveBroker)
        client.loop_forever()
except KeyboardInterrupt:
        print ("\nCtrl+C pressionado, encerrando aplicacao e saindo...")
        sys.exit(0)