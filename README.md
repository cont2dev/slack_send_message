# slack_send_message
## Sending a simple message using [slacker](https://github.com/os/slacker) in Python

### Requirements
* git
* python3
* python3-venv

1. Install the requirements
```bash
sudo apt install git python3 python3-venv
```

2. Get your tokken
https://api.slack.com/custom-integrations/legacy-tokens

3. Add your token to the "token" in send_message.py
```python
from slacker import Slacker

token = 'xoxp-...'
slack = Slacker(token)

...
...
```

4. Run
```bash
python3 send_message.py
```
