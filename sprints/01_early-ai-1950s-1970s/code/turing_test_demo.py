# turing_test_demo.py
import random


def human_response():
    responses = ["I love AI!", "Let's talk about science.", "Why do you ask?"]
    return random.choice(responses)


def machine_response():
    prompts = [
        "Tell me more about that.",
        "How does that make you feel?",
        "Can you elaborate?",
    ]
    return random.choice(prompts)


def play():
    print("Welcome to the Turing Test Demo. (Type 'exit' to quit)")
    while True:
        user_input = input("You: ")
        if user_input.lower() == "exit":
            break
        # Machine randomly chooses behavior to mimic human or bot
        if random.random() < 0.5:
            print("Machine:", human_response())
        else:
            print("Machine:", machine_response())


if __name__ == "__main__":
    play()
