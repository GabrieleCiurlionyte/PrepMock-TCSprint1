FEW_SHOT_EXAMPLES = [
    {
        "role": "user",
        "content": """
Interview question and reference answer:
QUESTION: What is recursion?
ANSWER:
Recursion is a programming technique where a function calls itself to solve a problem. It involves breaking down a problem into smaller, similar subproblems until a base case is reached. Recursive functions are often used to solve problems that can be defined in terms of smaller instances of the same problem, such as traversing tree-like data structures, calculating factorials, or generating Fibonacci sequences.

Interviewee answer:
Recursion is when a function calls itself until it reaches a base case. It is useful for problems like tree traversal and factorial calculations.
"""
    },
    {
        "role": "assistant",
        "content": """
{
  "off_topic": false,
  "message": null,
  "correct_answer": [
    "Correctly stated that recursion is when a function calls itself.",
    "Correctly mentioned the base case.",
    "Correctly mentioned common recursive uses such as tree traversal and factorials."
  ],
  "incorrect_answer": [
    "Did not explain that recursion usually solves a problem by reducing it into smaller subproblems."
  ],
  "overall_score": 9,
  "explanation": "Your answer is strong and technically correct. It would be even better if you also explained that each recursive call usually reduces the problem toward the base case.",
  "code_examples": [
    {
      "title": "Recursive factorial example",
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
QUESTION: What is recursion?
ANSWER:
Recursion is a programming technique where a function calls itself to solve a problem. It involves breaking down a problem into smaller, similar subproblems until a base case is reached. Recursive functions are often used to solve problems that can be defined in terms of smaller instances of the same problem, such as traversing tree-like data structures, calculating factorials, or generating Fibonacci sequences.

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
    "Did not explain that recursion usually solves a problem by reducing it into smaller subproblems.",
    "Did not mention any examples of recursion like traversing tree-like data structures, calculating factorials, or generating Fibonacci sequences"
  ],
  "overall_score": 3,
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
QUESTION: What is the fundamental difference between unit tests and integration tests?
ANSWER:
The fundamental difference between unit tests and integration tests is the scope and focus of the tests:

Unit tests focus on testing individual system components in isolation, verifying that each unit works as expected. They target the smallest testable parts of an application, such as individual methods or classes, and aim to ensure the correctness of the implementation.

Integration tests verify that different components of a system work together correctly. They test the interactions between multiple units or modules, ensuring the overall system functions as expected. Integration tests are typically performed after unit tests. They help identify issues that may arise from integrating different application parts.

The main difference is that unit tests target individual code units, while integration tests focus on the interactions and data flow between those units. Unit tests are typically easier to write, maintain, and run, while integration tests provide a more comprehensive understanding of the system's behavior.

Interviewee answer:
Unit tests check if the whole application works together, while integration tests check one method at a time.
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
    "Incorrectly reversed the meanings of unit tests and integration tests.",
    "Did not explain that unit tests focus on isolated components, while integration tests focus on interactions between components."
  ],
  "overall_score": 2,
  "explanation": "Your answer is incorrect because it swaps the definitions. Unit tests check small pieces of code in isolation, while integration tests check whether multiple parts of the system work correctly together.
  Unit tests target the smallest testable parts of an application, such as individual methods or classes, and aim to ensure the correctness of the implementation while integration tests are typically performed after unit tests. They help identify issues that may arise from integrating different application parts.",
  "code_examples": [
    {
      "title": "Unit test in isolation",
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
      "title": "Integration test across components",
      "code_lines": [
        "[Test]",
        "public async Task CreateOrder_ReturnsCreated()",
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
QUESTION: What is parallel programming (multithreading), and its purpose? Which classes are used?
ANSWER:
Parallel programming, or multithreading, is the ability of a system to support multiple threads of execution simultaneously. It improves performance by utilizing multiple processors or cores, allowing the application to perform multiple tasks concurrently. In .NET, classes like Task, Thread, and the Task Parallel Library (TPL) are commonly used for parallel programming.

Interviewee answer:
This is about object-oriented programming because threads are objects.
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
    "Did not mention that its purpose is to improve responsiveness or performance.",
    "Did not mention common .NET tools such as Task, Thread, or the Task Parallel Library (TPL)."
  ],
  "overall_score": null,
  "explanation": "You did not attempt to answer the question and instead asked to be taught. Parallel programming means a program can run multiple tasks or threads at the same time. Its purpose is to improve throughput or keep the application responsive. In .NET, common tools for this include Task, Thread, and the Task Parallel Library, which helps coordinate parallel work.",
  "code_examples": [
    {
      "title": "Running work with Task",
      "code_lines": [
        "using System.Threading.Tasks;",
        "",
        "Task first = Task.Run(() => DownloadData());",
        "Task second = Task.Run(() => ProcessData());",
        "await Task.WhenAll(first, second);"
      ]
    },
    {
      "title": "Using TPL with Parallel.ForEach",
      "code_lines": [
        "using System.Threading.Tasks;",
        "",
        "Parallel.ForEach(items, item =>",
        "{",
        "    Process(item);",
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
    "Correctly stated that parallel programming involves parallel execution using multiple threads to improve performance.",
    "Correctly mentioned Thread and Task as .NET tools used for parallel programming."
  ],
  "incorrect_answer": [
    "Incorrectly referred to 'thread class library'; the correct term is the Task Parallel Library (TPL).",
    "Did not clearly explain that parallel programming also allows concurrent work and can improve responsiveness."
  ],
  "overall_score": 7,
  "explanation": "Your answer is mostly correct because you described parallel execution and named Thread and Task. However, 'thread class library' is not the correct .NET term; the correct name is the Task Parallel Library (TPL). A stronger answer would also mention concurrent work and responsiveness more clearly.",
  "code_examples": [
    {
      "title": "Using Task for concurrent work",
      "code_lines": [
        "using System.Threading.Tasks;",
        "",
        "Task task = Task.Run(() => DoWork());",
        "await task;"
      ]
    },
    {
      "title": "Using TPL correctly",
      "code_lines": [
        "using System.Threading.Tasks;",
        "",
        "Parallel.ForEach(items, item =>",
        "{",
        "    Process(item);",
        "});"
      ]
    }
  ]
}
"""
    }
]
