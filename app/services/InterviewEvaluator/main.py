from dotenv import load_dotenv
from openai import OpenAI, conversations
from prompts.few_shot_examples import FEW_SHOT_EXAMPLES
from prompts.instructions import DEVELOPER_INSTRUCTIONS
from schemas import QuestionEvaluation

load_dotenv()

conversation = conversations.create()

client = OpenAI()

### We maybe add it as a question bank 


### Do we need to give question and answer and how do we read it from a question bank


## Where do we put the system prompt in?

### We need to provide a format for the question and answer itself.

# How to implement the safety identifier?





interview_question = """

QUESTION: What are the main principles of OOP (Object-Oriented Programming)?

ANSWER: 

Encapsulation involves bundling data (properties) and methods into a single unit called a class. Encapsulation helps hide the internal implementation details of an object and provides a well-defined interface for interacting with the object.

Abstraction focuses on the essential features of an object, hiding the unnecessary details. It allows you to create abstract classes and interfaces that define a contract without specifying the implementation details.

Inheritance allows a derived class to inherit properties and methods from a base class. It promotes code reuse and helps create hierarchical relationships between classes.

Polymorphism enables objects of different classes to be treated as objects of a common superclass. It allows you to write more generic and flexible code that can work with objects of different types.

"""

interviewee_answer = """

Object orientated programming is a type of programming where you encapsulate the logic into classes and can have polymorphism.
"""

### TODO: add few-shot promping examples
### TODO: let model have time to think, but how?
### TRIDIL defune audience
### Have limitation of the answer lenght?

### It should have personal tone it should say what did you do wrong -> not what the interviewee did wrong 

### How should we mesasure the quality of the answer

#Hot to implement scoring consistency


# Since we do not use reasoning model we need to provide insturctions

## Since 
response = client.responses.parse(
    model="gpt-4.1-nano",
    conversation=conversation.id,
    instructions=DEVELOPER_INSTRUCTIONS,
    input=[
        *FEW_SHOT_EXAMPLES,
        {
            "role": "user",
            "content": f"""
                "Interview question and reference answer:\n\n"
                f"{interview_question}"
            """
        },
        {
            "role": "user",
            "content": (
                "Interviewee answer:\n\n"
                f"{interviewee_answer}"
            )
        },
    ],
    text_format=QuestionEvaluation,
    store=False,
    temperature=0
)

### What is the compaction API?

print(response.output_text)
