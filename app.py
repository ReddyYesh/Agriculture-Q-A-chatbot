import os
import streamlit as st
from openai import OpenAI

# Read the API key from the environment variable
OPENAI_API_KEY = os.getenv("OPENAI_API_KEY")

# Initialize the OpenAI client
client = OpenAI(api_key=OPENAI_API_KEY)

def agricultural_chatbot(user_input):
    # Define the prompt or question
    prompt = user_input

    # Make a request to the OpenAI API with an appropriate model
    response = client.completions.create(
        model="gpt-3.5-turbo-instruct",  # Use an alternative model like "text-davinci"
        prompt=prompt,
        max_tokens=500,  # Adjust as needed
        n=1,  # Number of completions
        stop=None,  # You can add custom stop words if needed
        temperature=0.3  # Adjust temperature for creativity vs. accuracy
    )
    
    # Extract and return the generated text
    return response.choices[0].text.strip()

# Streamlit UI
st.title("Agriculture Chatbot")

# Text input field for user to type messages
user_input = st.text_input("You:", "")

# Submit button to trigger the chatbot response
if st.button("Submit"):
    # Call the chatbot function with user input
    response = agricultural_chatbot(user_input)
    
    # Display the chatbot response
    st.text_area("Chatbot:", value=response, height=200)
