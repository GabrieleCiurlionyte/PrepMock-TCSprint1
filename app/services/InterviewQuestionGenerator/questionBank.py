from .interviewQuestion import InterviewQuestion

QUESTION_BANK = [
    InterviewQuestion(
        id="oop-1",
        question="What are the main principles of OOP?",
        answer="""
Encapsulation involves bundling data (properties) and methods into a single unit called a class. Encapsulation helps hide the internal implementation details of an object and provides a well-defined interface for interacting with the object.
Abstraction focuses on the essential features of an object, hiding the unnecessary details. It allows you to create abstract classes and interfaces that define a contract without specifying the implementation details.
Inheritance allows a derived class to inherit properties and methods from a base class. It promotes code reuse and helps create hierarchical relationships between classes.
Polymorphism enables objects of different classes to be treated as objects of a common superclass. It allows you to write more generic and flexible code that can work with objects of different types.""",
        difficulty=None,
        topic="oop",
    ),
]
