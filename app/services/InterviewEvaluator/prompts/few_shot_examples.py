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
  "explanation": "You did not attempt to answer the question and instead asked to be taught. Parallel programming, or multithreading, means a program can run multiple tasks or threads at the same time. Its purpose is to improve throughput or keep the application responsive, especially when work can be split across CPU cores or when background work should not block the main flow. In .NET, common classes and tools include Task for task-based asynchronous and parallel work, Thread for lower-level thread control, and the Task Parallel Library for coordinating parallel operations.",
  "code_examples": [
    {
      "title": "Running work concurrently with Task",
      "code_lines": [
        "using System.Threading.Tasks;",
        "",
        "Task first = Task.Run(() => DownloadData());",
        "Task second = Task.Run(() => ProcessData());",
        "",
        "await Task.WhenAll(first, second);"
      ]
    },
    {
      "title": "Creating a dedicated Thread",
      "code_lines": [
        "using System.Threading;",
        "",
        "Thread worker = new Thread(() => DoWork());",
        "worker.Start();",
        "worker.Join();"
      ]
    },
    {
      "title": "Using TPL to process items in parallel",
      "code_lines": [
        "using System.Threading.Tasks;",
        "",
        "int[] numbers = { 1, 2, 3, 4 };",
        "Parallel.ForEach(numbers, number =>",
        "{",
        "    Process(number);",
        "});"
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
        "    var result = new Calculator().CalculateTotal(100m, 0.20m);",
        "    Assert.AreEqual(120m, result);",
        "}"
      ]
    },
    {
      "title": "Integration Test Example",
      "code_lines": [
        "[Test]",
        "public async Task CreateOrder_SavesOrderAndReturns201()",
        "{",
        "    var response = await _client.PostAsJsonAsync(\"/orders\", new { productId = 1, quantity = 2 });",
        "    Assert.AreEqual(HttpStatusCode.Created, response.StatusCode);",
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
    },
    {
        "role": "user",
        "content": """
Interview question and reference answer:
QUESTION: What is parallel programming (multithreading), and its purpose? Which classes are used?
ANSWER:
Parallel programming, or multithreading, is the ability of a system to support multiple threads of execution simultaneously. It improves performance by utilizing multiple processors or cores, allowing the application to perform multiple tasks concurrently. In .NET, classes like Task, Thread, and the Task Parallel Library (TPL) are commonly used for parallel programming.

Interviewee answer:
Parallel programming is when you run code in multiple threads to make execution faster. We use classes like Task and Thread.
"""
    },
    {
        "role": "assistant",
        "content": """
{
  "off_topic": false,
  "message": null,
  "correct_answer": [
    "Correctly stated that parallel programming involves running work on multiple threads.",
    "Correctly mentioned Task and Thread as common .NET tools used for this."
  ],
  "incorrect_answer": [
    "Did not clearly explain that the purpose can also include improving responsiveness, not only making execution faster.",
    "Did not mention that work may run concurrently across multiple tasks or cores.",
    "Did not mention the Task Parallel Library (TPL)."
  ],
  "overall_score": 7,
  "explanation": "Your answer is mostly correct, but it is more general than the reference answer. Saying it makes execution faster is a reasonable partial explanation of the purpose, but you did not specifically mention responsiveness, concurrent task execution, or the Task Parallel Library.",
  "code_examples": null
}
"""
    },
    {
        "role": "user",
        "content": """
Interview question and reference answer:
QUESTION: What is recursion?
ANSWER:
Recursion is a programming technique where a function calls itself to solve a problem by breaking it into smaller subproblems. A recursive solution usually has a base case to stop the repeated calls and a recursive case that reduces the problem toward that base case.

Interviewee answer:
Recursion is when a function calls itself.
"""
    },
    {
        "role": "assistant",
        "content": """
{
  "off_topic": false,
  "message": null,
  "correct_answer": [
    "Correctly stated that recursion is when a function calls itself."
  ],
  "incorrect_answer": [
    "Did not mention the base case that stops the recursion.",
    "Did not explain that recursive solutions usually reduce a problem into smaller subproblems."
  ],
  "overall_score": 4,
  "explanation": "Your answer includes the core idea of recursion, but it is too brief to be complete. A stronger answer should also mention the base case and explain that recursion solves a problem by reducing it into smaller repeated subproblems.",
  "code_examples": [
    {
      "title": "Recursion with a base case",
      "code_lines": [
        "int Factorial(int n)",
        "{",
        "    if (n <= 1) return 1;",
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
QUESTION: What is parallel programming (multithreading), and its purpose? Which classes are used?
ANSWER:
Parallel programming, or multithreading, is the ability of a system to support multiple threads of execution simultaneously. It improves performance by utilizing multiple processors or cores, allowing the application to perform multiple tasks concurrently. In .NET, classes like Task, Thread, and the Task Parallel Library (TPL) are commonly used for parallel programming.

Interviewee answer:
Parallel programming is when you execute code in parallel to increase the perfgormance of code using several threads. The classes you can use in .NET are thread, task, thread class library.
"""
    },
    {
        "role": "assistant",
        "content": """
{
  "off_topic": false,
  "message": null,
  "correct_answer": [
    "Correctly stated that parallel programming involves using multiple threads or parallel execution to improve performance.",
    "Correctly mentioned Thread and Task as .NET tools used for parallel programming."
  ],
  "incorrect_answer": [
    "Incorrectly referred to 'thread class library'; the correct term is the Task Parallel Library (TPL).",
    "Did not clearly explain that parallel programming can also improve responsiveness and run work concurrently."
  ],
  "overall_score": 7,
  "explanation": "Your answer is mostly correct because you described parallel execution and named Thread and Task. However, 'thread class library' is not the correct .NET term; the correct name is the Task Parallel Library (TPL). A stronger answer would also mention concurrent work and responsiveness more clearly.",
  "code_examples": null
}
"""
    }
]
