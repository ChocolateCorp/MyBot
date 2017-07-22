
import os
from slackclient import SlackClient

slack_client = SlackClient(os.environ.get('SLACK_BOT_TOKEN'))


if __name__ == "__main__":
    api_call = slack_client.api_call("users.list")
    if api_call.get('ok'):
        # retrieve all users
        users = api_call.get('members')
        print users
        for user in users:
        	if 'name' in user and user.get('name'):
        		print user['name']
    else:

        print("could not find  user with the name ")
