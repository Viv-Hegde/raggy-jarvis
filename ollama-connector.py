import ollama

client = ollama.Client()

model = "llama3.2"

print(f"Using model: {model}")

while True:
    prompt = input("Ask Llama: ")
    if prompt == "//":
        print("Exiting...")
        break
    # Assuming the client.generate() supports streaming via stream=True, iterate over chunks.
    for chunk in client.generate(model=model, prompt=prompt, stream=True):
        print(chunk.response, end="", flush=True)

    print("\n\n")