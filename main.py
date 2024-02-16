import network, socket
import urequests as requests
import ujson
from time import sleep

# WiFi network
ssid='' # Network SSID
password=''  # Network password
sta_if = network.WLAN(network.STA_IF)
if not sta_if.isconnected():
    sta_if.active(True)
    print('connecting to network...')
    # TODO remove hard coded BSSID and figure out how to connect to the "strongest" signal
    sta_if.connect(ssid,password)
    while not sta_if.isconnected():
        print('.', end = '')
        sleep(0.25)
try:
    host = sta_if.config('hostname')
except ValueError:
    # "hostname" is available in master, but not yet in June 2022 1.19.1 release
    host = sta_if.config('dhcp_hostname')
print('Wifi connected as {}/{}, net={}, gw={}, dns={}'.format(host, *sta_if.ifconfig()))


# POST request
# Change the "api_key" to your own
# Change the "question" to what you want to ask
api_key = ""
url = "https://generativelanguage.googleapis.com/v1beta/models/gemini-pro:generateContent?key=" + api_key
question = "Who are you?"



payload = ujson.dumps({
  "contents": [
    {
      "parts": [{
        "text":question}]}]})

headers = {
  'Content-Type': 'application/json'
}



# Print the question (msg)
print(question)

# Post Data
response = requests.post(url, headers=headers, data=payload)
response_data = response.json()


# Access JSON object
message = response_data["candidates"][0]["content"]["parts"][0]["text"]
# Close the connection
response.close()

# Print the response (message)
print(message)




