# Script to train the multilingual LLM chatbot
from transformers import MarianMTModel, MarianTokenizer

# Load the tokenizer and model
tokenizer = MarianTokenizer.from_pretrained('Helsinki-NLP/opus-mt-en-hi')
model = MarianMTModel.from_pretrained('Helsinki-NLP/opus-mt-en-hi')

# Example training process (this is a simplified example)
# For actual training, you would need a more comprehensive setup and dataset
input_text = "What are the symptoms of colorectal cancer?"
inputs = tokenizer(input_text, return_tensors="pt")
outputs = model.generate(**inputs)
translated_text = tokenizer.decode(outputs[0], skip_special_tokens=True)

print(translated_text)
