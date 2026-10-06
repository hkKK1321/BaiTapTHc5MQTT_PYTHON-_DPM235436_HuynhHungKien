import paho.mqtt.client as mqtt

# --- CẤU HÌNH MQTT BROKER HIVEMQ ---
BROKER = "broker.hivemq.com"
PORT = 1883
TOPIC = "agu/iot/nhietdo"

def on_connect(client, userdata, flags, rc, properties=None):
    if rc == 0:
        print("=" * 50)
        print("✅ Kết nối tới HiveMQ Broker thành công!")
        print(f"📡 Đã Subscribe kênh topic: {TOPIC}")
        print("=" * 50 + "\n")
        client.subscribe(TOPIC)
    else:
        print(f"❌ Kết nối thất bại, mã lỗi: {rc}")

def on_message(client, userdata, msg):
    payload = msg.payload.decode('utf-8')
    print(f"📩 [NHẬN TỪ ESP32] Topic: {msg.topic} | Nhiệt độ: {payload} °C")
    
    try:
        temp = float(payload)
        if temp > 30.0:
            print("   ⚠️ CẢNH BÁO: Nhiệt độ vượt ngưỡng 30°C!\n")
        else:
            print("   ✅ Trạng thái: Bình thường.\n")
    except ValueError:
        pass


try:
    client = mqtt.Client(mqtt.CallbackAPIVersion.VERSION1, client_id="Python_Subscriber_AGU")
except AttributeError:
    client = mqtt.Client(client_id="Python_Subscriber_AGU")

client.on_connect = on_connect
client.on_message = on_message

print("⏳ Đang kết nối tới broker.hivemq.com...")
client.connect(BROKER, PORT, 60)
client.loop_forever()
