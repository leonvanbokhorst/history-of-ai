# Early AI: Code + Explanation

This document combines Python code examples alongside explanations to illustrate each milestone in Early AI.

## 1. Turing Test (1950)

### Explanation

The Turing Test evaluates a machine's ability to exhibit human-like intelligence through an imitation game.

### Code Demo

```python
# turing_test_demo.py
import random

def human_response():
    responses = ["I love AI!", "Let's talk about science.", "Why do you ask?"]
    return random.choice(responses)

def machine_response():
    # A simple rule-based bot that asks follow-up questions
    prompts = [
        "Tell me more about that.",
        "How does that make you feel?",
        "Can you elaborate?"
    ]
    return random.choice(prompts)

def play():
    print("Welcome to the Turing Test Demo. (Type 'exit' to quit)")
    while True:
        user_input = input("You: ")
        if user_input.lower() == 'exit':
            break
        # Machine randomly chooses behavior to mimic human or bot
        if random.random() < 0.5:
            print("Machine:", human_response())
        else:
            print("Machine:", machine_response())

if __name__ == '__main__':
    play()
```

### Usage

```bash
python code/turing_test_demo.py
```

---

## 2. Logic Theorist (1956)

### Explanation

The Logic Theorist was the first AI program to prove mathematical theorems using symbolic reasoning.

### Code Demo

```python
# logic_theorist_demo.py
from sympy import symbols, Implies, satisfiable

# Define propositions p and q
p, q = symbols('p q')

# Given (p -> q) and p, infer q
theorem = Implies(p, q) & p
model = satisfiable(theorem)
print("Satisfiable model:", model)
# If q is True in the model, the inference is valid.
```

### Usage

```bash
pip install sympy
python code/logic_theorist_demo.py
```

---

## 3. Perceptron (1958)

For a complete implementation and demonstration, refer to:

```bash
code/perceptron_demo.py
```

---

## 4. Shakey the Robot (1966)

### Explanation

Shakey was the first mobile robot to plan and execute actions in a real environment using the STRIPS planning language.

### Code Demo (Stub)

```python
# shakey_planning_demo.py
# Stub for a simple grid-world planner

def plan(start, goal, grid):
    # TODO: Implement BFS or A* path planning
    pass

if __name__ == '__main__':
    print("Shakey planning demo placeholder")
```

### Next Steps

- Implement the `plan` function using a search algorithm (BFS or A\*).
- Visualize the resulting path on a grid.

---

Feel free to run each demo in the `code/` directory and expand upon these examples!
