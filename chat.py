import requests

# Set your Infobip API credentials and the API URL
infobip_url = 'https://api.infobip.com/sms/2/text/single'
infobip_username = 'Xfrost'
infobip_password = 'Morgan.123'
sender_id = 'ServiceSMS'  # Your custom sender ID

# Get the destination number and message from the user
dest_number = input("Enter the destination number (e.g. 15555555555): ")
message = input("Enter the message: ")

# Define the payload for the POST request
payload = {
    'from': sender_id,
    'to': dest_number,
    'text': message
}

# Make the POST request to send the SMS using the Infobip API
response = requests.post(infobip_url, auth=(infobip_username, infobip_password), json=payload)

# Check if the request was successful
if response.status_code == 200:
    print("Message sent successfully!")
else:
    print("Failed to send message. Error:", response.text)

