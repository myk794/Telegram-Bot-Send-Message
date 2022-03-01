import requests

token = 'YOUR_TOKEN'
chatID = 'YOUR_CHAT_ID'

def send_message(bot_message):
    
    send_text = 'https://api.telegram.org/bot' + token + '/sendMessage?chat_id=' + chatID + '&parse_mode=Markdown&text=' + bot_message
    response = requests.get(send_text)
    return response.json()

def send_photo(image_path):
    try:
        files={'photo':open(image_path,'rb')}
        response = requests.post('https://api.telegram.org/bot'+token+'/sendPhoto?chat_id='+chatID, files=files)
    except Exception as e:
        print(e)

def send_document(document_path):
    try:
        files={'document':open(document_path,'rb')}
        response = requests.post('https://api.telegram.org/bot'+token+'/sendDocument?chat_id='+chatID, files=files)
    except Exception as e:
        print(e)

send_message("This is a testing message!!")

send_photo('IMAGE_PATH')

send_document('DOCUMENT_PATH')
