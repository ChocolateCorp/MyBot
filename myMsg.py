import time
from slackclient import SlackClient

BOT_TOKEN = "xoxb-215245499840-8P8Y6EUekGjQyXOv6gdIPYIA"
CHANNEL_NAME = "general"

def main():
    # Create the slackclient instance
    sc = SlackClient(BOT_TOKEN)
    print "my sc " , sc

    # Connect to slack
    sc.api_call(
        "chat.postMessage", channel="#general", text="hello how r u ?",
        username='startbot', icon_emoji=':lion_face:')
    if sc.rtm_connect():
        # Send first message
        sc.rtm_send_message(CHANNEL_NAME, "I'm ALIVE!!!")

        while True:
            # Read latest messages
            for slack_message in sc.rtm_read():
                message = slack_message.get("text")
                print "my messages",message
                user = slack_message.get("user")
                print "my user" , user
                if not message or not user:
                    continue
                sc.rtm_send_message(CHANNEL_NAME, "<@{}> wrote something...".format(user))
            # Sleep for half a second
            time.sleep(0.5)

if __name__ == '__main__':
    main()