import streamlit as st

def echo_bot(user_input):
    # Simple EchoBot that repeats user input
    return f"Bot: You said: {user_input}"

# Streamlit app
def main():
    st.title("Conversational AI on Structured Data")

    # Text input for user
    user_input = st.text_input("User:", "")

    if st.button("Send"):
        # Process user input and get bot response
        bot_response = echo_bot(user_input)

        # Display bot response
        st.text_area("Bot:", bot_response, height=100)

if __name__ == "__main__":
    main()

