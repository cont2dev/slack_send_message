from slacker import Slacker

token = ''
slack = Slacker(token)

message = 'Hello, Slack'
slack.chat.post_message('#general', message, as_user=True)
