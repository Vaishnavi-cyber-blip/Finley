import streamlit as st
import requests
import json


def make_post_request(api_key, query):
    # URL with the channel token placeholder
    url = 'https://payload.vextapp.com/hook/WSQJQZP1BG/catch/$(vaish18)'

    # Payload data
    payload = {
        "payload": query
    }

    # Headers
    headers = {
        'Content-Type': 'application/json',
        'Apikey': 'Api-Key ' + api_key
    }

    # Make the POST request
    response = requests.post(url, headers=headers, data=json.dumps(payload))

    # Return response
    return response


# Streamlit UI
st.title("POST Request Application")

# Input fields for API Key and Query
api_key = "zwIqDEt8.ZW5RfaXmjr2eKI7MZUIT2vl9tH5UEkhC"
query = st.text_input("Enter your query:")

# Button to trigger the request
if st.button("Send Request"):
    if api_key and query:
        # Making the request
        response = make_post_request(api_key, query)

        # Displaying response
        st.subheader("Response:")
        st.json(response.json())
    else:
        st.write("Please enter API Key and Query.")
