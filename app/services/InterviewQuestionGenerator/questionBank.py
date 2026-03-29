from .interviewQuestion import InterviewQuestion, Difficulty

QUESTION_BANK = [
    InterviewQuestion(
        id=1,
        question="What is recursion?",
        answer="""
Recursion is a programming technique where a function calls itself to solve a problem. It involves breaking down a problem into smaller, similar subproblems until a base case is reached. Recursive functions are often used to solve problems that can be defined in terms of smaller instances of the same problem, such as traversing tree-like data structures, calculating factorials, or generating Fibonacci sequences.""",
        difficulty=Difficulty.EASY,
    ),
    InterviewQuestion(
        id=2,
        question="What is parallel programming (multithreading), and its purpose? Which classes are used?",
        answer="""
Parallel programming, or multithreading, is the ability of a system to support multiple threads of execution simultaneously. It improves performance by utilizing multiple processors or cores, allowing the application to perform multiple tasks concurrently. In .NET, classes like Task, Thread, and the Task Parallel Library (TPL) are commonly used for parallel programming.""",
        difficulty=Difficulty.EASY,
    ),
    InterviewQuestion(
        id=3,
        question="What is the fundamental difference between unit tests and integration tests?",
        answer="""
The fundamental difference between unit tests and integration tests is the scope and focus of the tests:

Unit tests focus on testing individual system components in isolation, verifying that each unit works as expected. They target the smallest testable parts of an application, such as individual methods or classes, and aim to ensure the correctness of the implementation.

Integration tests verify that different components of a system work together correctly. They test the interactions between multiple units or modules, ensuring the overall system functions as expected. Integration tests are typically performed after unit tests. They help identify issues that may arise from integrating different application parts.

The main difference is that unit tests target individual code units, while integration tests focus on the interactions and data flow between those units. Unit tests are typically easier to write, maintain, and run, while integration tests provide a more comprehensive understanding of the system's behavior.""",
        difficulty=Difficulty.EASY,
    ),
    InterviewQuestion(
        id=4,
        question="What is Garbage Collector at a basic level?",
        answer="""
Garbage Collector is a mechanism in .NET that automatically reclaims memory occupied by objects no longer used by the application. This mechanism scans the memory (managed heap) to find unused objects and reclaim their space for future use.""",
        difficulty=Difficulty.MEDIUM,
        topic="oop",
    ),
    InterviewQuestion(
        id=5,
        question="Is there a difference between Delegate and Action?",
        answer="""
Delegate is a general-purpose type representing any method with a matching signature.

Action is a specific type of delegate that represents a method with a void return type and no parameters.""",
        difficulty=Difficulty.MEDIUM,
    ),
    InterviewQuestion(
        id=6,
        question="What is boxing/unboxing?",
        answer="""
Boxing is the process of converting a value type to a reference type instance.
Unboxing is the opposite, converting a reference type back to a value type.
Boxing and unboxing can incur a performance penalty as they involve additional memory allocations and type conversions.""",
        difficulty=Difficulty.MEDIUM,
    ),
    InterviewQuestion(
        id=7,
        question="What is a hash function, and why are hash tables needed?",
        answer="""
A hash function is a mathematical function that takes an input (e.g., a string, an object, or data collection) and produces a fixed-size output, typically an integer value, known as a hash code or hash value. Hash functions are designed to distribute their outputs in a uniform and pseudo-random manner across the entire range of possible hash values.

Hash tables are data structures that use hash functions to store and retrieve data efficiently. Hash tables are needed because they provide fast average-case time complexity for common operations like insertion, deletion, and lookup, which are typically O(1) on average.

Hash tables are widely used in various applications, such as caching systems, databases, compilers, and data processing pipelines, due to their efficiency in storing and retrieving data based on keys.""",
        difficulty=Difficulty.HARD,
    ),
    InterviewQuestion(
        id=8,
        question="What are collisions, and how do you deal with them?",
        answer="""
Collisions in hash tables occur when different keys are mapped to the same index by the hash function. Common techniques to handle collisions include separate chaining, open addressing, and rehashing.""",
        difficulty=Difficulty.HARD,
    ),
]
