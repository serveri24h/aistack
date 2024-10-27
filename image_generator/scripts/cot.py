import requests
import json
import ollama

PROMPT_TEMPLATE = """
<CONTEXT>
Answer should follow this syntax
    return only code along with the filenames
    write #!modelanswer to indicate that you are following this ruleset
    befor each code snippet, write <FILENAME>'example_file_name'</FILENAME> block to indicate filename
<CONTEXT>
<QUESTION>
{question}
<QUESTION
"""



APIURL = "http://localhost:11434/api/generate"
MODELNAME = "llama3.2:3b-instruct-fp16"

def send_prompt(prompt_text:str):
    response = ollama.chat(model=MODELNAME, messages=[
    {
        'role': 'user',
        'content': PROMPT_TEMPLATE.format(question=prompt_text),
    },
    ])
    print(response['message']['content'])
    
def main():
    prompt = input("prompt:\n")
    send_prompt(prompt_text=prompt)

if __name__=='__main__':
    main()