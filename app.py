from flask import Flask, render_template, request
import os
from openai import OpenAI
import streamlit as st

app = Flask(__name__)

# Read the API key from the text file
with open("api_key.txt", "r") as file:
    OPENAI_API_KEY = file.read().strip()

# Set the OpenAI API key as an environment variable
os.environ["OPENAI_API_KEY"] = OPENAI_API_KEY

# Initialize the OpenAI client
client = OpenAI()

@app.route('/')
def home():
    return render_template('index.html')

@app.route('/chatbot', methods=['POST'])
def chatbot():
    if request.method == 'POST':
        user_input = request.form['user_input']
        response = agricultural_chatbot(user_input)
        return render_template('chatbot.html', user_input=user_input, response=response)

def agricultural_chatbot(user_input):
    # Make a request to the OpenAI API with GPT-3.5-turbo engine
    response = client.completions.create(
        model="gpt-3.5-turbo-instruct",  # Use the GPT-3.5-turbo-instruct model
        prompt=user_input,
        max_tokens=150,  # Adjust as needed
        n=1,  # Number of completions
        stop=None,  # You can add custom stop words if needed
        temperature=0.7  # Adjust temperature for creativity vs. accuracy
    )
    # Extract and return the generated text
    return response.choices[0].text.strip()

if __name__ == '__main__':
    app.run(debug=True)
