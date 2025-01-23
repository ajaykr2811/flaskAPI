from openai import OpenAI


client = OpenAI(api_key='put_your_key_here')

# Replace with your actual API key

# Make a simple request to the OpenAI API
try:
    response = client.completions.create(model="text-davinci-003",  # You can change the model if needed
    prompt="Say hello to the world!",max_tokens=10)

    print("Response from OpenAI API:")
    print(response.choices[0].text.strip())

except Exception as e:
    print(f"An error occurred: {e}")
