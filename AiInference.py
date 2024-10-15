from dotenv import load_dotenv
import os
# Declaring LLM
from langchain_groq import ChatGroq
load_dotenv()

GROQ_KEY = os.environ['GROQ_KEY']

llm = ChatGroq(
    model="llama-3.1-70b-versatile",
    temperature=0,
    max_tokens=None,
    timeout=None,
    max_retries=2,
    api_key=GROQ_KEY
    # other params...
)

def chat(user_input: str, system_prompt: str) -> str:
    
    messages = [
    (
        "system",
        system_prompt
    ),
    ("human", user_input),
    ]
    ai_msg = llm.invoke(messages)
    print("======== AI Message ========")
    print("\n")
    print(ai_msg.content)
    print("\n")
    return ai_msg.content
