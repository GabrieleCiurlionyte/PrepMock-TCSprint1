FEW_SHOT_EXAMPLES = [
    # Example 1: Mostly correct but incomplete
    {
    "role": "user",
    "content": """
Interview question and reference answer:
QUESTION: What are the main principles of OOP?
ANSWER:
Encapsulation, Abstraction, Inheritance, Polymorphism

Interviewee answer:
Encapsulation, inheritance, and polymorphism are key OOP principles.
"""
},
{
    "role": "assistant",
    "content": """
{
  "off_topic": false,
  "message": null,
  "correct_answer": [
    "Correctly identified encapsulation.",
    "Correctly identified inheritance.",
    "Correctly identified polymorphism."
  ],
  "incorrect_answer": [
    "Did not mention abstraction."
  ],
  "overall_score": 7,
  "explanation": "The answer is mostly correct but incomplete because it omits abstraction, one of the core principles."
}
"""
},
# Example 2: Partially wrong
{
    "role": "user",
    "content": """
Interview question and reference answer:
QUESTION: What are the main principles of OOP?
ANSWER:
Encapsulation, Abstraction, Inheritance, Polymorphism

Interviewee answer:
OOP is based on encapsulation, inheritance, and recursion.
"""
},
{
    "role": "assistant",
    "content": """
{
  "off_topic": false,
  "message": null,
  "correct_answer": [
    "Correctly identified encapsulation.",
    "Correctly identified inheritance."
  ],
  "incorrect_answer": [
    "Incorrectly listed recursion as a core OOP principle.",
    "Did not mention abstraction or polymorphism."
  ],
  "overall_score": 4,
  "explanation": "The answer includes some correct principles but also contains incorrect information and misses key concepts."
}
"""
},
# Example 3: Off-topic
{
    "role": "user",
    "content": """
Interview question and reference answer:
QUESTION: What are the main principles of OOP?
ANSWER:
Encapsulation, Abstraction, Inheritance, Polymorphism

Interviewee answer:
OOP is useful because it makes programs faster and easier to debug.
"""
},
{
    "role": "assistant",
    "content": """
{
  "off_topic": true,
  "message": "The answer is not related to the interview question.",
  "correct_answer": null,
  "incorrect_answer": null,
  "overall_score": null,
  "explanation": null
}
"""
},
# Example 4: Very short, but correct
{
    "role": "user",
    "content": """
Interview question and reference answer:
QUESTION: What are the main principles of OOP?
ANSWER:
Encapsulation, Abstraction, Inheritance, Polymorphism

Interviewee answer:
Encapsulation, abstraction, inheritance, polymorphism.
"""
},
{
    "role": "assistant",
    "content": """
{
  "off_topic": false,
  "message": null,
  "correct_answer": [
    "Correctly identified encapsulation.",
    "Correctly identified abstraction.",
    "Correctly identified inheritance.",
    "Correctly identified polymorphism."
  ],
  "incorrect_answer": [],
  "overall_score": 9,
  "explanation": "The answer correctly lists all main principles, though it lacks explanation or detail."
}
"""
},
# Example 5: Uses synonyms
{
    "role": "user",
    "content": """
Interview question and reference answer:
QUESTION: What are the main principles of OOP?
ANSWER:
Encapsulation, Abstraction, Inheritance, Polymorphism

Interviewee answer:
Object-oriented programming relies on hiding internal details, defining general interfaces, reusing behavior through class hierarchies, and allowing different implementations to be used interchangeably.
"""
},
{
    "role": "assistant",
    "content": """
{
  "off_topic": false,
  "message": null,
  "correct_answer": [
    "Described encapsulation as hiding internal details.",
    "Described abstraction as defining general interfaces.",
    "Described inheritance as reusing behavior through class hierarchies.",
    "Described polymorphism as allowing interchangeable implementations."
  ],
  "incorrect_answer": [],
  "overall_score": 9,
  "explanation": "The answer correctly describes all OOP principles using paraphrased language, demonstrating strong understanding."
}
"""
}
]