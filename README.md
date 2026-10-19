# CCCS 104 · Data Structures and Algorithms

Three menu-driven console programs in Python, each implementing a linear data structure: a **list**, a **stack** and a **queue**. They were written as graded learning tasks for CCCS 104 (College of Computer Studies, Camarines Sur Polytechnic Colleges). Each task also has a written report with a rationale and a user guide.

![Python](https://img.shields.io/badge/Python-3-3776AB?logo=python&logoColor=white)
![Dependencies](https://img.shields.io/badge/dependencies-none-brightgreen)

## Projects

| # | Structure | What the program does | Submitted |
|---|---|---|---|
| 1 | [Array list](1-list/) | Manages a list of integers through ten operations: insert, delete, search and display | Aug 30, 2024 |
| 2 | [Stack on a linked list](2-stack/) | Takes three stacks and finds the height at which all three are equal | Sep 8, 2024 |
| 3 | [Queue](3-queue/) | Distributes incoming workloads across three queues | Sep 15, 2024 |

Submission dates are the dates of each task's final report.

## 1. Array List

A list abstract data type backed by a Python list. The program loops on a menu until the user confirms exit.

```
[1] Insert At Start      [6] Delete At Position
[2] Insert At End        [7] Delete Number
[3] Insert At Position   [8] Search Number
[4] Delete At Start      [9] Display Number At Position
[5] Delete At End        [10] Display List       [0] Exit
```

- Each operation is a plain function that takes the list as a parameter.
- Non-numeric input, an empty list and out-of-range positions are handled with a message, not a crash.
- Search reports the position of the first match, and delete-by-value removes the first occurrence.

## 2. Stack on a Linked List

A `Stack` built on a `LinkedList` of `Node` objects. The program reads three space-separated stacks of integers and computes each stack's height, which is the sum of its elements.

To equalize the stacks, it removes the top element of whichever stack is currently tallest until all three heights match. If they only match at zero, it reports that they will never be equal. Afterwards it asks whether to run again.

Example run:

```
Enter elements of Stack 1: 3 2 1 1 1
Enter elements of Stack 2: 4 3 2
Enter elements of Stack 3: 1 1 4 1 1
----------------------------------------------
Stack 1 total height: 8
Stack 2 total height: 9
Stack 3 total height: 8
----------------------------------------------
All stacks are equal at Height: 7
Stack 1: 1 1 2 3
Stack 2: 3 4
Stack 3: 1 4 1 1
----------------------------------------------
Continue? Y or N:
```

Each remaining stack is printed top first.

## 3. Queue

A `Queue` class (`enqueue`, `dequeue`, `display`, `size`, `sum`, `front`) that powers a workload system with three queues. After every action the program prints the state of all three.

- **Enqueue:** if any queue is empty, the new workload goes to the queue with the fewest items. Once every queue has items, it goes to the queue with the lowest total.
- **Dequeue:** removes from the non-empty queue whose front value is lowest.

Example run, enqueuing 5, 3, 4, 2 and then dequeuing once:

```
Queue 1: 5
Queue 2: 3 2
Queue 3: 4
----------------------------------------------
Queue 1: 5
Queue 2: 2
Queue 3: 4
```

## Running the programs

Python 3 is the only requirement. Run the submitted version of each task from its `learning-task/` folder:

```bash
python3 1-list/learning-task/OriasMJ_BSCS2A.py
python3 2-stack/learning-task/OriasMJ_BSCS2A.py
python3 3-queue/learning-task/BSCS2A_Orias.py
```

## Repository layout

Each task folder holds the submitted program and its written report (`.docx` and `.pdf`).

```
├── 1-list/learning-task/
├── 2-stack/learning-task/
└── 3-queue/learning-task/
```

## Author

Mark Joseph C. Orias · BSCS 2A · August to September 2024
