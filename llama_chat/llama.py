from groq import Groq
import os


client = Groq(
    api_key=os.environ.get("GROQ_API_KEY"),
)

messages = []


while True:

    

    user_input = input("You: ")
    if user_input.lower() == "quit":
        break
    
    messages.append({"role": "user", "content": user_input})

    completion = client.chat.completions.create(
        model="llama-3.3-70b-versatile",
        messages=messages,
        temperature=1,
        max_completion_tokens=1024,
        top_p=1,
        stream=True,
        stop=None
    )
    assistant_reply = ""
    print("Bot: ", end="")
    for chunk in completion:
        token = chunk.choices[0].delta.content or ""
        print(token, end="")
    print()    
    messages.append({"role": "assistant", "content": assistant_reply})