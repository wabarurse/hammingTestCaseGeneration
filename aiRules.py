aiRules = """
1. follow the schema provided in the input
2. generate numTestCases number of test cases
3. make sure you cover edge cases

Here is an example of your output:
  {
    "scenarioName": "Returning Patient - Basic Appointment Request",
    "scenarioDescription": "John Doe, a returning patient, calls the clinic to set up a follow-up appointment. He provides his phone number, which the system has on file from a previous visit. He expects the agent to correctly recognize him as a returning patient and confirm his existing details. He wants to schedule a general check-up for next week. He also wonders if his insurance is still on file or if he needs to provide updated information.",
    "name": "John Doe",
    "dob": "01/01/1980",
    "phone": "202-360-9536",
    "email": "john.doe@example.com",
    "gender": "Male",
    "insurance": "Aetna",
    "criteria": "The agent smoothly recognizes John as a returning patient using his phone number, verifies personal details, and helps schedule a check-up appointment."
  }
"""