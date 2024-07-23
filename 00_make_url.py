from dotenv import load_dotenv
import os
import requests

load_dotenv()

TOKEN = os.getenv('TELEGRAM_BOT_TOKEN')

URL = f'https://api.telegram.org/bot{TOKEN}'

method = 'getUpdates'

res = requests.get(f'{URL}/{method}')
res_dict = res.json()

user_input = res_dict['result'][-1]['message']['text']
user_id = res_dict['result'][-1]['message']['from']['id']

print(user_id, user_input)
print(f'{URL}/sendMessage?chat_id={user_id}&text={user_input}')

SEND_MSG_URL = f'{URL}/sendMessage?chat_id={user_id}&text={user_input}'

requests.get(SEND_MSG_URL)