import google.generativeai as genai

# Configure Gemini API with your key
genai.configure(api_key="GOOGLE_API_KEY")

# List available models
models = genai.list_models()

# Print model names
print("Available models:")
for model in models:
    print(model.name)
