# IoT-Based Smart Home Network Monitoring System

## Project Overview
This project monitors home network traffic and device activity using an IoT-based system. A Raspberry Pi or ESP8266/ESP32 acts as a network sensor, sending data to an MQTT broker. The data is stored in InfluxDB and visualized using Grafana.

## Features
- Monitor connected devices & network traffic
- Visualize network activity in real-time dashboards
- Send alerts for unusual activity

## Tech Stack
- Python (for data collection)
- MQTT (for IoT communication)
- InfluxDB & Grafana (for storage and visualization)

## Installation
1. Install dependencies: `pip install paho-mqtt influxdb-client`
2. Configure InfluxDB and MQTT settings in `mqtt_listener.py`
3. Run the script: `python mqtt_listener.py`

## Author
Created by ChatGPT
