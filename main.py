import os
import sys
from dotenv import load_dotenv
from google import genai


def main():
    load_dotenv()
    api_key = os.environ.get("GEMINI_API_KEY")
    client = genai.Client(api_key=api_key)
    args = sys.argv[1:]
    
    if not args:
        print('No prompt was provided.')
        print('\nUsage: python main.py "your prompt here:"')
        print('Example: python main.py "How do I build a calculator app?"')
        sys.exit(1)
    prompt = " ".join(args)

    response = client.models.generate_content(
        model = 'gemini-2.0-flash-001',
        contents = prompt
    )
    prompt_tokens = response.usage_metadata.prompt_token_count
    response_tokens = response.usage_metadata.candidates_token_count
    print(f'Response: {response.text}')
    print(f'Prompt tokens: {prompt_tokens}')
    print(f'Response tokens: {response_tokens}')


if __name__ == "__main__":
    main()
