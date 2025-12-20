from langchain_google_genai import ChatGoogleGenerativeAI
from dotenv import load_dotenv

load_dotenv()

model = ChatGoogleGenerativeAI(
  model = 'gemini-2.5-flash-lite',
  temperature= '0.8'
)

result = model.invoke("what is india")
print(result.content)