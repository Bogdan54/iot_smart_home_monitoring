import paho.mqtt.client as mqtt
import influxdb_client
from influxdb_client.client.write_api import SYNCHRONOUS
import json
import time

# MQTT Configuration
MQTT_BROKER = "broker.hivemq.com"
MQTT_PORT = 1883
MQTT_TOPIC = "home/network/monitor"

# InfluxDB Configuration
INFLUXDB_URL = "http://localhost:8086"
INFLUXDB_TOKEN = "your-token-here"
INFLUXDB_ORG = "your-org"
INFLUXDB_BUCKET = "network-monitoring"

client = influxdb_client.InfluxDBClient(url=INFLUXDB_URL, token=INFLUXDB_TOKEN, org=INFLUXDB_ORG)
write_api = client.write_api(write_options=SYNCHRONOUS)

def on_connect(client, userdata, flags, rc):
    if rc == 0:
        print("Connected to MQTT Broker!")
        client.subscribe(MQTT_TOPIC)
    else:
        print("Failed to connect, return code", rc)

def on_message(client, userdata, msg):
    try:
        data = json.loads(msg.payload.decode("utf-8"))
        print(f"Received message: {data}")
        
        point = influxdb_client.Point("network_activity").tag("device", data.get("device", "unknown"))\
                .field("traffic", float(data.get("traffic", 0)))\
                .field("latency", float(data.get("latency", 0)))
                
        write_api.write(bucket=INFLUXDB_BUCKET, org=INFLUXDB_ORG, record=point)
        print("Data written to InfluxDB")
    except Exception as e:
        print("Error processing message:", e)

def start_mqtt_listener():
    mqtt_client = mqtt.Client()
    mqtt_client.on_connect = on_connect
    mqtt_client.on_message = on_message
    mqtt_client.connect(MQTT_BROKER, MQTT_PORT, 60)
    mqtt_client.loop_start()

if __name__ == "__main__":
    print("Starting IoT-Based Smart Home Network Monitoring System...")
    start_mqtt_listener()
    while True:
        time.sleep(1)
