
__author__ = 'Benjamin Thomas Schwertfeger'
__email__ = 'development@b-schwertfeger.de'

__description__ = "Script to generarte dummy Messages, sent to the Websocketserver, which will then sent to the client to display\
 a log and if the right words are choosen, some dougnut charts."

import requests
import json
import time
import numpy as np

s = requests.Session()

url = "http://127.0.0.1:3000"#"http://192.168.8.140:3000"

do_request = lambda payload: s.post(f'{url}/api/data', data={'data': json.dumps(payload)})
smiles: [str] = ['bad','medium', 'good', 'unknown']
gender: [str] = ['male', 'female', 'wtf']
pleasures: [str] = ['happy', 'bored', 'funny', 'sweet', 'annoying']
emotions: [str] = ['happy', 'excited', 'bored', 'stressy']

sleeptime = lambda: np.random.choice(np.arange(0.1, 2,.001))

def main() -> None:
    while True:
        print(do_request({'topic': 'smile_state', 'state': np.random.choice(smiles)}).status_code)
        time.sleep(sleeptime())
        print(do_request({'topic': 'gender', 'gender': np.random.choice(gender)}).status_code)
        time.sleep(sleeptime())
        print(do_request({'topic': 'pleasure_state', 'state': np.random.choice(pleasures)}).status_code)
        time.sleep(sleeptime())
        print(do_request({'topic': 'emotion_state', 'state': np.random.choice(emotions)}).status_code)
        time.sleep(sleeptime())

if __name__ == '__main__':
    main()