# Script to collect data for training the multilingual LLM chatbot
import pandas as pd

# Example data collection process
data = {
    "questions": [
        "What are the symptoms of colorectal cancer?",
        "कोलोरेक्टल कैंसर के लक्षण क्या हैं?",
        "కోలొరెక్టల్ క్యాన్సర్ లక్షణాలు ఏమిటి?",
        "କୋଲୋରେକ୍ଟାଲ କ୍ୟାନ୍ସର ଲକ୍ଷଣଗୁଡିକ କ’ଣ?"
    ],
    "answers": [
        "The symptoms include changes in bowel habits, rectal bleeding, and abdominal pain.",
        "लक्षणों में मल त्याग की आदतों में बदलाव, मलाशय से खून आना और पेट में दर्द शामिल हैं।",
        "లక్షణాలలో బowel అలవాట్లలో మార్పులు, రెక్టల్ బ్లీడింగ్, మరియు కడుపు నొప్పి ఉన్నాయి.",
        "ଲକ୍ଷଣଗୁଡିକରେ ମଳ ଆଦତରେ ପରିବର୍ତ୍ତନ, ଆନୁଗଳୀ ରକ୍ତସ୍ରାବ, ଏବଂ ପେଟର ପିଳା ହୋଇଥାଏ।"
    ]
}

df = pd.DataFrame(data)
df.to_csv("chatbot_training_data.csv", index=False)
