import streamlit as st
import cohere

# Initialize Cohere client
co = cohere.Client(st.secrets["COHERE_API_KEY"])  # Replace with your actual key in secrets.toml

def generate_email_response(email_text, tone):
    prompt = f"""
You are an AI assistant. Write a reply to the following email using a {tone.lower()} tone:

Email:
{email_text}

Reply:
"""
    response = co.generate(
        model="command-r",  # or "command", "command-light", etc.
        prompt=prompt,
        max_tokens=300,
        temperature=0.7
    )
    return response.generations[0].text.strip()
