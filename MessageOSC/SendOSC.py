from pythonosc import osc_message_builder
from pythonosc import udp_client

vrchat_ip = "127.0.0.1"
vrchat_port = 9000

def SendMessageBox(message):
    builder = osc_message_builder.OscMessageBuilder(address="/chatbox/input")
    builder.add_arg(message)  # Text argument (string)
    builder.add_arg(True)  # Immediate flag (boolean)
    builder.add_arg(False)  # Keyboard flag (boolean)
    builder.add_arg(False)  # Notification SFX flag (boolean)
    msg = builder.build()
    client = udp_client.SimpleUDPClient(vrchat_ip, vrchat_port)
    client.send(msg)