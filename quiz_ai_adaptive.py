import random

# Questions categorized by difficulty level
questions_easy = [
    {"question": "What is the capital of France?", "options": ["a) Berlin", "b) Paris", "c) Madrid"], "answer": "b"},
    {"question": "What is 5 * 6?", "options": ["a) 30", "b) 25", "c) 20"], "answer": "a"}
]

questions_medium = [
    {"question": "Which language is primarily used for AI?", "options": ["a) Python", "b) HTML", "c) JavaScript"], "answer": "a"},
    {"question": "What is 15 squared?", "options": ["a) 215", "b) 225", "c) 235"], "answer": "b"}
]

questions_hard = [
    {"question": "What is the output of 2 ** 3 ** 2 in Python?", "options": ["a) 64", "b) 512", "c) 256"], "answer": "b"},
    {"question": "Which algorithm is used in Decision Trees?", "options": ["a) Gini Index", "b) Naive Bayes", "c) K-Means"], "answer": "a"}
]

def run_quiz(questions):
    score = 0
    for q in questions:
        print("\n" + q["question"])
        for opt in q["options"]:
            print(opt)
        user_ans = input("Your answer: ").lower()
        if user_ans == q["answer"]:
            print("Correct!")
            score += 1
        else:
            print(f"Wrong! Correct answer is: {q['answer']}")
    return score

def adaptive_quiz():
    print("Welcome to the AI Quiz App!\n")
    print("Starting with Easy Level...")
    score_easy = run_quiz(questions_easy)
    
    if score_easy >= len(questions_easy) * 0.75:
        print("\nGood performance! Moving to Medium Level...")
        score_medium = run_quiz(questions_medium)

        if score_medium >= len(questions_medium) * 0.75:
            print("\nExcellent! Let's challenge you with Hard Level...")
            score_hard = run_quiz(questions_hard)
        else:
            print("\nTry again to unlock Hard Level!")
    else:
        print("\nYou need more practice to unlock higher levels!")

    print("\nThank you for playing the AI Quiz App!")

if __name__ == "__main__":
    adaptive_quiz()
