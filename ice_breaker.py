from dotenv import load_dotenv
import os

if __name__ == '__main__':
    load_dotenv()
    print("hello LangChain!")
    print(os.environ.get("OPENAI_API_KEY"))