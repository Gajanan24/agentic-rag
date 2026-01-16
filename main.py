from dotenv import load_dotenv

load_dotenv()

from graph.graph import app





if __name__ == "__main__":
    print("Hello, AGENTIC RAGGGGGGGG_______________________!")  

    print(app.invoke(input={"question": "What is agent in movies like FBI agent?"}))