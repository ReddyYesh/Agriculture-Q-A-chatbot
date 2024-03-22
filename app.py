import streamlit as st
import os
from openai import OpenAI

# Set your OpenAI API key using an environment variable
os.environ["OPENAI_API_KEY"] = "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"

# Initialize the OpenAI client
client = OpenAI()

def agricultural_chatbot(user_input):
    # Define the prompt or question
    prompt = user_input

    # Make a request to the OpenAI API with GPT-3.5-turbo engine
    response = client.completions.create(
        model="gpt-3.5-turbo-instruct",  # Use the GPT-3.5-turbo-instruct model
        prompt=prompt,
        max_tokens=150,  # Adjust as needed
        n=1,  # Number of completions
        stop=None,  # You can add custom stop words if needed
        temperature=0.7  # Adjust temperature for creativity vs. accuracy
    )
    
    # Extract and return the generated text
    return response.choices[0].text.strip()

# Streamlit UI
st.title("Agriculture Chatbot")

user_input = st.text_input("You:", "Type here...")

if st.button("Submit"):
    response = agricultural_chatbot(user_input)
    st.text_area("Chatbot:", value=response, height=200)

