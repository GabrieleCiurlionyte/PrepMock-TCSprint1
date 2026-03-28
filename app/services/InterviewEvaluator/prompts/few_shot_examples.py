FEW_SHOT_EXAMPLES = [
    {
        "role": "user",
        "content": """
Interview question and reference answer:
QUESTION: What are the 4 main principles of OOP?
ANSWER:
Encapsulation involves bundling data (properties) and methods into a single unit called a class. Encapsulation helps hide the internal implementation details of an object and provides a well-defined interface for interacting with the object.
Abstraction focuses on the essential features of an object, hiding the unnecessary details. It allows you to create abstract classes and interfaces that define a contract without specifying the implementation details.
Inheritance allows a derived class to inherit properties and methods from a base class. It promotes code reuse and helps create hierarchical relationships between classes.
Polymorphism enables objects of different classes to be treated as objects of a common superclass. It allows you to write more generic and flexible code that can work with objects of different types.

Interviewee answer:
Encapsulation, inheritance, and polymorphism are key OOP principles. Encapsulation bundles properties and methods to classes. Inheritance allowss classes to inherit functionality from base class. Polymorphism allows to write more generic code.
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
  "overall_score": 8,
  "explanation": "The answer is mostly correct but incomplete because it omits abstraction, one of the core principles.",
  "code_examples": null
}
"""
    },
    {
        "role": "user",
        "content": """
Interview question and reference answer:
QUESTION: What are the main principles of OOP?
ANSWER:
Encapsulation involves bundling data (properties) and methods into a single unit called a class. Encapsulation helps hide the internal implementation details of an object and provides a well-defined interface for interacting with the object.
Abstraction focuses on the essential features of an object, hiding the unnecessary details. It allows you to create abstract classes and interfaces that define a contract without specifying the implementation details.
Inheritance allows a derived class to inherit properties and methods from a base class. It promotes code reuse and helps create hierarchical relationships between classes.
Polymorphism enables objects of different classes to be treated as objects of a common superclass. It allows you to write more generic and flexible code that can work with objects of different types.

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
  "overall_score": 3,
  "explanation": "Your answer is partially correct because you identified encapsulation and inheritance, but recursion is not an OOP principle. Recursion is a programming technique where a function calls itself, while the missing OOP principles here are abstraction and polymorphism.",
  "code_examples": [
    {
      "title": "Recursion Example",
      "code_lines": [
        "int Factorial(int n)",
        "{",
        "    if (n <= 1)",
        "    {",
        "        return 1;",
        "    }",
        "",
        "    return n * Factorial(n - 1);",
        "}"
      ]
    }
  ]
}
"""
    },
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
  "explanation": null,
  "code_examples": null
}
"""
    },
    {
        "role": "user",
        "content": """
Interview question and reference answer:
QUESTION: What is parallel programming (multithreading), and its purpose? Which classes are used?
ANSWER:
Parallel programming, or multithreading, is the ability of a system to support multiple threads of execution simultaneously. It improves performance by utilizing multiple processors or cores, allowing the application to perform multiple tasks concurrently. In .NET, classes like Task, Thread, and the Task Parallel Library (TPL) are commonly used for parallel programming.

Interviewee answer:
I don't know what parallel programming is, can you teach me?
"""
    },
    {
        "role": "assistant",
        "content": """
{
  "off_topic": false,
  "message": null,
  "correct_answer": [],
  "incorrect_answer": [
    "Did not explain that parallel programming allows multiple tasks or threads to run concurrently.",
    "Did not mention that its purpose is to improve responsiveness or performance by using multiple cores.",
    "Did not mention common .NET classes such as Task, Thread, or the Task Parallel Library."
  ],
  "overall_score": null,
  "explanation": "You did not attempt to answer the question and instead asked to be taught. Parallel programming, or multithreading, means your program can run multiple tasks or threads at the same time instead of waiting for one task to finish before starting another. You would usually use it to improve performance or responsiveness, especially when work can be split across multiple CPU cores or when the program needs to keep responding while other work is happening. In .NET, common tools for this are Task, Thread, and the Task Parallel Library (TPL).",
  "code_examples": [
    {
      "title": "Running Tasks Concurrently",
      "code_lines": [
        "using System;",
        "using System.Threading.Tasks;",
        "",
        "var downloadTask = Task.Run(() =>",
        "{",
        "    Console.WriteLine(\"Downloading data...\");",
        "});",
        "",
        "var processTask = Task.Run(() =>",
        "{",
        "    Console.WriteLine(\"Processing file...\");",
        "});",
        "",
        "await Task.WhenAll(downloadTask, processTask);"
      ]
    },
    {
      "title": "Creating a Thread",
      "code_lines": [
        "using System;",
        "using System.Threading;",
        "",
        "var thread = new Thread(() =>",
        "{",
        "    Console.WriteLine(\"Running work on a separate thread\");",
        "});",
        "",
        "thread.Start();",
        "thread.Join();"
      ]
    }
  ]
}
"""
    },
    {
        "role": "user",
        "content": """
Interview question and reference answer:
QUESTION: What is the fundamental difference between unit tests and integration tests?
ANSWER:
The fundamental difference between unit tests and integration tests is the scope and focus of the tests:

Unit tests focus on testing individual system components in isolation, verifying that each unit works as expected. They target the smallest testable parts of an application, such as individual methods or classes, and aim to ensure the correctness of the implementation.

Integration tests verify that different components of a system work together correctly. They test the interactions between multiple units or modules, ensuring the overall system functions as expected. Integration tests are typically performed after unit tests. They help identify issues that may arise from integrating different application parts.

The main difference is that unit tests target individual code units, while integration tests focus on the interactions and data flow between those units. Unit tests are typically easier to write, maintain, and run, while integration tests provide a more comprehensive understanding of the system's behavior.

Interviewee answer:
I don't know. Can you explain the difference?
"""
    },
    {
        "role": "assistant",
        "content": """
{
  "off_topic": false,
  "message": null,
  "correct_answer": [],
  "incorrect_answer": [
    "Did not explain that unit tests verify individual components in isolation.",
    "Did not explain that integration tests verify how multiple components work together.",
    "Did not mention the difference in scope, purpose, or typical order of use."
  ],
  "overall_score": null,
  "explanation": "You did not attempt to answer the question and instead asked to be taught. Unit tests check a small piece of code, such as one function or class, in isolation so you can verify that individual parts behave correctly on their own. Integration tests check whether multiple parts of the system work correctly together, such as a service, database, and API. You usually write unit tests first because they are faster and more focused, and then use integration tests to confirm the full workflow between components.",
  "code_examples": [
    {
      "title": "Unit Test Example",
      "code_lines": [
        "[Test]",
        "public void CalculateTotal_AddsTaxCorrectly()",
        "{",
        "    var calculator = new Calculator();",
        "",
        "    var result = calculator.CalculateTotal(100m, 0.20m);",
        "",
        "    Assert.AreEqual(120m, result);",
        "}"
      ]
    },
    {
      "title": "Integration Test Example",
      "code_lines": [
        "[Test]",
        "public async Task Checkout_CreatesOrderInDatabase()",
        "{",
        "    var client = _factory.CreateClient();",
        "",
        "    var response = await client.PostAsJsonAsync(\"/checkout\", new",
        "    {",
        "        ProductId = 1,",
        "        Quantity = 2",
        "    });",
        "",
        "    response.EnsureSuccessStatusCode();",
        "",
        "    var order = await _dbContext.Orders.FirstOrDefaultAsync();",
        "    Assert.IsNotNull(order);",
        "}"
      ]
    }
  ]
}
"""
    },
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
  "incorrect_answer": [
    "Did not explain what encapsulation, abstraction, inheritance, and polymorphism mean."
  ],
  "overall_score": 9,
  "explanation": "The answer correctly lists all main principles, but it would be stronger if it briefly explained each one.",
  "code_examples": null
}
"""
    },
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
  "explanation": "The answer correctly describes all OOP principles using paraphrased language, demonstrating strong understanding.",
  "code_examples": null
}
"""
    }
]
