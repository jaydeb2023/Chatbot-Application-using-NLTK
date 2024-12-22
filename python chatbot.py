#!/usr/bin/env python
# coding: utf-8

# In[1]:


pip install nltk


# In[3]:


import nltk
from nltk.chat.util import Chat, reflections


# In[4]:


# Pairs of patterns and responses
pairs = [
    [
        r"(hi|hello|hey)",
        ["Hello! How can I assist you today?", "Hi there! How can I help?", "Hey! What can I do for you?"]
    ],
    [
        r"what is your name?", 
        ["I am a chatbot created to assist you. You can call me ChatBot!"]
    ],
    [
        r"how are you?",
        ["I am just a bunch of code, but I am functioning as expected! How can I assist you?"]
    ],
    [
        r"(what can you do|your features)",
        ["I can answer your questions, chat with you, and provide helpful information. Just ask me anything!"]
    ],
    [
        r"(bye|goodbye|exit)",
        ["Goodbye! Have a great day!", "Bye! Take care!", "See you later!"]
    ],
    [
        r"(.*) (location|city)",
        ["I am based in the digital world and accessible from anywhere!"]
    ],
    [
        r"(.*) weather (.*)",
        ["I don't have real-time weather data, but you can check online for accurate information."]
    ],
    [
        r"(.*)",
        ["I'm not sure how to respond to that. Could you rephrase or ask something else?", "Interesting! Can you elaborate?", "Let me think about that. Can you ask differently?"]
    ]
]


# In[5]:


# Create a chatbot instance
chatbot = Chat(pairs, reflections)


# In[ ]:


# Start the chatbot
print("Welcome to the ChatBot! Type 'bye' to exit.")
while True:
    user_input = input("You: ")
    if user_input.lower() in ['bye', 'exit', 'quit']:
        print("ChatBot: Goodbye! Have a great day!")
        break
    response = chatbot.respond(user_input)
    print("ChatBot:", response)


# In[ ]:




