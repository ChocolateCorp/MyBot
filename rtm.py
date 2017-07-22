import time
from slackclient import SlackClient

token = "YOUR_BOT_TOKEN"# found at https://api.slack.com/web#authentication
sc = SlackClient(token)
print sc.api_call("api.test")
print sc.api_call("channels.info", channel="1234567890")
print sc.api_call(
        "chat.postMessage", channel="#general", text="Hello from Chetna! :tada:",
        username='startbot', icon_emoji=':lion_face:'
)
if sc.rtm_connect():
        while True:
                print sc.rtm_read()
                time.sleep(1)
else:
    print "Connection Failed, invalid token?"
