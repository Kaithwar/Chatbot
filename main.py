import streamlit as st
from openai import OpenAI
from streamlit_monaco import st_monaco
from func import debug_code
from func import run_code
from func import analyze_code

client = OpenAI(api_key="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")

# Function to interact with the chatbot using GPT-3
def ask_question(question):
    response = client.chat.completions.create(
            model="gpt-3.5-turbo",
            messages=[
                {
                "role": "user",
                "content": question
                }
            ],
            temperature=1,
            max_tokens=256,
            top_p=1,
            frequency_penalty=0,
            presence_penalty=0
            )
    return response.choices[0].message.content


with st.container():
    st.title("Chat with the AI")

    st.subheader("Ask any question:")
    question = st.text_input("")
    if st.button("Submit", key="button1"):
        if question:
            answer = ask_question(question)
            st.write("AI's response:")
            st.write(answer)
        else:
            st.write("Please enter a question.")
    
    st.markdown("<br><br>", unsafe_allow_html=True)
    

with st.container():
    st.subheader("Enter code:")
    language=st.selectbox("Select language", ["python", "java", "javascript","cpp", "html", "css", "markdown"]),
    content = st_monaco(
    value="// write your code",
    height="200px",
    language=language,
    lineNumbers=True,
    minimap=False,
    theme="vs-dark",
    )

    st.subheader("What do you want to do with the code?")
    options = ["Run the code", "Complete the code", "Debug the code"]
    selected_option = st.selectbox("", options)

    if st.button("Submit"):
        if content:
            if selected_option == "Run the code":
                output = run_code(content,language)
                st.write("Output:")
                st.write(output)
            elif selected_option == "Debug the code":
                fixes = debug_code(content,language)
                st.write("Suggested fixes:")
                st.write(fixes)
            elif selected_option == "Complete the code":
                analysis = analyze_code(content,language)
                st.write("Output:")
                st.write(analysis)
        else:
            st.write("Please ask a question or enter code.")