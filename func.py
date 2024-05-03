from openai import OpenAI
from dotenv import load_dotenv
import os

os.environ["OPENAI_API_KEY"] = "sk-proj-xXgnWUDwCqQ5dXt3kRP2T3BlbkFJiIKEBhR5hDQ9h91fFjMQ"
client = OpenAI(api_key=os.environ.get("OPENAI_API_KEY"))

def configure():
    load_dotenv()

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


# Function to run the code and get the output
def run_code(code,language):
    response = client.chat.completions.create(
        model="gpt-3.5-turbo",
        messages=[
            {"role": "user", "content": f"Please give the output of {language} code:\n\n{code}\nOutput:"}
        ],
        temperature=1,
        max_tokens=100
    )
    return response.choices[0].message.content

# Function to debug the code and suggest fixes
def debug_code(code,language):
    response = client.chat.completions.create(
        model="gpt-3.5-turbo",
        messages=[
            {"role": "user", "content": f"Debug the following {language} code:\n\n{code}\nSuggested fixes:"}
        ],
        temperature=1,
        max_tokens=100
    )
    return response.choices[0].message.content

# Function to analyze the code and provide insights
def analyze_code(code,language):
    response = client.chat.completions.create(
        model="gpt-3.5-turbo",
        messages=[
            {"role": "user", "content": f"Complete the uncompleted following {language} code and give the full completed code:\n\n{code}\n"}
        ],
        temperature=1,
        max_tokens=100
    )
    return response.choices[0].message.content