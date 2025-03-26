from google import genai
from google.genai import types
from pydantic import BaseModel
from aiRules import aiRules
from testInput import testInput
import dotenv
import os

dotenv.load_dotenv()


class schema(BaseModel):
    scenarioName: str
    scenarioDescription: str
    name: str
    dob: str
    phone: str
    email: str
    gender: str
    insurance: str
    criteria: str

def generateTestCases(input, numTestCases) -> list[schema]: 
    try:
        input = "input: " + input + "\nNumber of test cases: " + str(numTestCases) + "\n" + "your rules: " + aiRules
        geminiClient = genai.Client(api_key=os.getenv("GEMINI_KEY"))
        response = geminiClient.models.generate_content(
            model="gemini-2.0-flash",
            contents=input,
            config=types.GenerateContentConfig(
                response_mime_type='application/json',
                response_schema=list[schema],
            )
        )
        return response.text
    except Exception as e:
        print(e)
        return []

print(generateTestCases(testInput, 10))
