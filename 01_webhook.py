import os
from dotenv import load_dotenv

load_dotenv()

TOKEN = os.getenv('TELEGRAM_BOT_TOKEN')
URL = f'https://api.telegram.org/bot{TOKEN}'
method = 'setWebhook'
NGROK_URL = os.getenv('NGROK_URL')

print(f'{URL}/{method}?url={NGROK_URL}')