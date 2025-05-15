import openai
 

client = openai.OpenAI(api_key="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")


messages = [
    {"role": "system", "content": "You are a DevOps assistant. Always answer with 3 sentences."}
]

print("Ask your DevOps questions! Type 'exit' to quit.\n")

while True:
    user_input = input("You: ")
    
    if user_input.strip().lower() in {"exit", "quit"}:
        print("Goodbye!")
        break

    # Add the user's message
    messages.append({"role": "user", "content": user_input})

    # Send the chat request
    response = client.chat.completions.create(
        model="gpt-4.1",  # Use "gpt-4-turbo" or "gpt-3.5-turbo"
        messages=messages
    )

    # Extract and print the assistant's reply
    reply = response.choices[0].message.content
    print(f"\nAssistant: {reply}\n")

    # Add assistant's reply to conversation history
    messages.append({"role": "assistant", "content": reply})
