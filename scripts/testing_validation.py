# Script to test and validate the chatbot
import requests

def test_chatbot():
    url = "http://localhost:5000/chat"
    messages = [
        {"message": "What are the symptoms of colorectal cancer?"},
        {"message": "कोलोरेक्टल कैंसर के लक्षण क्या हैं?"},
        {"message": "కోలొరెక్టల్ క్యాన్సర్ లక్షణాలు ఏమిటి?"},
        {"message": "କୋଲୋରେକ୍ଟାଲ କ୍ୟାନ୍ସର ଲକ୍ଷଣଗୁଡିକ କ’ଣ?"}
    ]
    for msg in messages:
        response = requests.post(url, json=msg)
        print(f"Input: {msg['message']}\nResponse: {response.json()['response']}\n")

if __name__ == "__main__":
    test_chatbot()
