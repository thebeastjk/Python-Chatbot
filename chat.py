import llama_cpp

model = Model(model_path='/path/to/ggml/model')
while True:
    try:
        prompt = input("You: ", flush=True)
        if prompt == '':
            continue
        print(f"AI:", end='')
        for token in model.generate(prompt):
            print(f"{token}", end='', flush=True)
        print()
    except KeyboardInterrupt:
        break