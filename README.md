# 🧠 AI Adaptive Quiz App

A terminal-based Python quiz application that adapts to the user's performance. Designed to make learning fun and progressively challenging!

## 🚀 Features

- ✅ Three difficulty levels: **Easy**, **Medium**, and **Hard**
- 🎯 Adaptive logic: Unlocks the next level only if you score well in the current one
- 💬 Multiple-choice questions with instant feedback
- 🔁 Replayable and easy to customize with your own questions

## 🧩 How It Works

1. The quiz starts with **Easy** level questions.
2. If the user scores **75% or more**, it progresses to the **Medium** level.
3. If the Medium level is cleared with 75%+, it proceeds to the **Hard** level.
4. Otherwise, the quiz ends with motivational feedback.

## 🛠️ Setup & Run

### Requirements

- Python 3.x

### Run the App

```bash
python quiz_ai_adaptive.py
```

### Sample Output

```
Welcome to the AI Quiz App!

Starting with Easy Level...

What is the capital of France?
a) Berlin
b) Paris
c) Madrid
Your answer: b
Correct!

...

Thank you for playing the AI Quiz App!
```

## 📝 Customization

You can easily modify or add your own questions in the following sections of the `quiz_ai_adaptive.py`:

```python
questions_easy = [
    {"question": "Your question?", "options": ["a) Option1", "b) Option2"], "answer": "a"}
]
```

## 📁 File Structure

```
quiz_ai_adaptive.py    # Main script with logic and question bank
README.md              # Project documentation
```

## 👨‍💻 Author

Developed by Tanmay Pansare

## 📜 License

This project is open source and available under the MIT License.
