import requests

print("ChatGPT da Wish: Olá em que posso ajudar?")

while True:
    pergunta = input("\nVocê: ")
    r = requests.post("http://127.0.0.1:8000/perguntar", json={"pergunta": pergunta})
    print("\nChatGPT da Wish:", r.json()["resposta"])