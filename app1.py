import streamlit as st
import requests

st.title("Dictionary App")
st.write("Powered by FastAPI Backend")
st.caption("Brought to you by Arnab")

word = st.text_input("Enter a Word to Search")
# st.button("Search")

if(st.button("Search")):
    # Now I will call the FastAPI
    response = requests.get(f"http://127.0.0.1:8000/dictionary/{word}")
    data = response.json()
    if "error" in data:
        st.error(data["error"])
    else:
        word_data = data[0]
        # Basic info
        st.header(word_data["word"].capitalize())
        st.write(f"📢 {word_data.get('phonetic', 'No phonetic available')}")
        # All meanings in expanders
        st.subheader("Meanings")
        for meaning in word_data["meanings"]:
            with st.expander(meaning["partOfSpeech"].capitalize()):
                for defn in meaning["definitions"]:
                    st.write(f"• {defn['definition']}")
                    if "example" in defn:
                        st.caption(f'Example: "{defn["example"]}"')