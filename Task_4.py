import requests

API_KEY = "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"

def health_chatbot(query):
    unsafe = ["diagnose", "dose", "dosage", "prescribe", "treat", "cure"]
    if any(w in query.lower() for w in unsafe):
        return "I cannot provide medical diagnosis or dosage information. Please consult a doctor."

    url = "https://api.groq.com/openai/v1/chat/completions"
    headers = {
        "Content-Type": "application/json",
        "Authorization": f"Bearer {API_KEY}"
    }
    data = {
        "model": "llama-3.1-8b-instant",
        "messages": [
            {"role": "system", "content": "You are a friendly health assistant. Provide only general health information."},
            {"role": "user", "content": query}
        ]
    }

    response = requests.post(url, headers=headers, json=data)

    result = response.json()
    if "choices" not in result:
        return "API Error: " + str(result)
    return result["choices"][0]["message"]["content"]

print("Health Chatbot (API version) - type 'exit' to stop")

while True:
    q = input("You: ")
    if q.lower() == "exit":
        break
    print("Bot:", health_chatbot(q))
