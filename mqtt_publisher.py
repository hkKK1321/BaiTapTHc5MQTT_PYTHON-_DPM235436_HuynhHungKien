import paho.mqtt.client as mqtt


BROKER = "broker.hivemq.com"
PORT = 1883
TOPIC = "agu/iot/nhietdo"

try:
    client = mqtt.Client(mqtt.CallbackAPIVersion.VERSION1, client_id="Python_Publisher_AGU")
except AttributeError:
    client = mqtt.Client(client_id="Python_Publisher_AGU")

print("⏳ Đang kết nối tới broker.hivemq.com...")
client.connect(BROKER, PORT, 60)
client.loop_start()

print("\n🚀 KẾT NỐI THÀNH CÔNG!")
print("Nhập giá trị nhiệt độ (°C) từ bàn phím để truyền sang Board LCD & Board LED trên Wokwi.")
print("Gõ 'exit' để dừng chương trình.\n")

while True:
    val = input("Nhập nhiệt độ (°C): ")
    if val.lower() == 'exit':
        break
    try:
        temp = float(val)
        client.publish(TOPIC, str(temp))
        print(f"📤 [PUBLISH SUCCESS] Đã gửi {temp} °C lên topic '{TOPIC}'\n")
    except ValueError:
        print("❌ Vui lòng nhập số hợp lệ!")

client.loop_stop()
client.disconnect()
