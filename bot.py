import requests
from telegram.ext import Updater, CommandHandler

def start(update, context):
    context.bot.send_message(chat_id=update.effective_chat.id, text="Halo! Kirimkan tautan yang ingin kamu pendekkan.")

def create_short_link(update, context):
    url = update.message.text.split(' ')[1]  # Ambil URL dari pesan yang dikirimkan
    api_key = 'YOUR_PAID4LINK_API_KEY'  # Ganti dengan API Key Paid4Link Anda

    # Kirim permintaan ke API Paid4Link untuk membuat short link
    response = requests.get(f'https://paid4link.com/api?api={api_key}&url={url}')
    data = response.json()

    if data['status'] == 'success':
        short_link = data['shortenedUrl']
        context.bot.send_message(chat_id=update.effective_chat.id, text=short_link)
    else:
        context.bot.send_message(chat_id=update.effective_chat.id, text='Gagal membuat short link.')

def main():
    updater = Updater(token='YOUR_TELEGRAM_BOT_TOKEN', use_context=True)  # Ganti dengan token bot Telegram Anda
    dispatcher = updater.dispatcher
    start_handler = CommandHandler('start', start)
    create_short_link_handler = CommandHandler('shortlink', create_short_link)

    dispatcher.add_handler(start_handler)
    dispatcher.add_handler(create_short_link_handler)

    updater.start_polling()
    updater.idle()

if __name__ == '__main__':
    main()
