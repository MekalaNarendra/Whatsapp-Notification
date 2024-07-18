import pywhatkit as kit
import time

# Define the phone number and message
phone_number = "+917732070952"  # Replace with the recipient's phone number in international format
message = "nuvvo bokka ra"

# Specify the time at which the message should be sent (24-hour format)
hour = 12  # Replace with the desired hour
minute = 30  # Replace with the desired minute

# Send the WhatsApp message
# kit.sendwhatmsg(phone_number, message, hour, minute)
while True:
    # Send the WhatsApp message immediately
    kit.sendwhatmsg_instantly(phone_number, message)

    # Wait for a specified amount of time before sending the next message
    time.sleep(2)  # Send a message every 60 seconds
