from senha import API_KEY
import requests
import json


headers = {"Authorization": f"Bearer {API_KEY}", "Content-Type": "application/json"}
link = "https://api.openai.com/v1/chat/completions"
id_modelo = "gpt-3.5-turbo"
print("Olá, digite sua dúvida, ou digite 'sair' para sair!")  
while True: 
    user_input = input("\nUsuario: ")
    if user_input.lower() == 'sair':
        break
        
    
    body_mensagem = {
    "model": id_modelo,
    "messages": [{"role": "user", "content": user_input}]
    }
    body_mensagem = json.dumps(body_mensagem)
    requisicao = requests.post(link, headers=headers, data=body_mensagem)
    resposta_bot = requisicao.json()["choices"][0]["message"]["content"]
    print(f"\nBot: {resposta_bot}")
