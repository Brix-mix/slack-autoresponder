#!/usr/bin/env python
import os
import time
from random import randint
from pprint import pprint

from slackclient import SlackClient

def run_bot():
    token = os.environ.get('SLACKBOT_TOKEN')
    
    slack_client = SlackClient(token)
    
    hits = [
        "guyz"
        "hey guys",
        "hi guys",
        "my guys",
        "thanks guys",
        "the guys",
        "these guys",
        "these guys",
        "those guys",
        "you guys",
    ]
    
    responses = [
        'Some people in the community find "guys" alienating, next time would you consider folks? :slightly_smiling_face: (<http://bit.ly/2uJCn3y|Learn more>)',
        'Some people in the community find "guys" alienating, next time would you consider all? :slightly_smiling_face: (<http://bit.ly/2uJCn3y|Learn more>)',
        'Some people in the community find "guys" alienating, next time would you consider y\'all? :slightly_smiling_face: (<http://bit.ly/2uJCn3y|Learn more>)',
        'Some people in the community find "guys" alienating, next time would you consider everyone? :slightly_smiling_face: (<http://bit.ly/2uJCn3y|Learn more>)'
    ]
    
    if slack_client.rtm_connect():
        while True:
            events = slack_client.rtm_read()
            for event in events:
                if event.get('type') == 'message':
                    channel = event['channel']
                    text = event['text']
                    user = event['user']
                    if any(hit in text.lower() for hit in hits):
                        slack_client.api_call(
                            'chat.postEphemeral',
                            channel=channel,
                            text=responses[randint(0,
                                                   len(responses) - 1)],
                            user=user,
                            as_user='true',
                        )
            time.sleep(1)
    else:
        print('Connection failed, invalid token?')

if __name__ == '__main__':
    run_bot()
