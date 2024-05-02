from openai import OpenAI

client = OpenAI(api_key="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")


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