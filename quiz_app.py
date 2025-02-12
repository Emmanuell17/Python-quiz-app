# quiz_app.py

def ask_question(question, options, correct_option):
    print("\n" + question)  # Print the question
    for idx, option in enumerate(options, 1):
        print(f"{idx}. {option}")  # Print the options
    
    answer = input("Choose the correct option (1/2/3/4): ")

    if int(answer) == correct_option:
        print("Correct!\n")
        return True
    else:
        print(f"Wrong! The correct answer is {options[correct_option - 1]}\n")
        return False

def main():
    score = 0
    questions = [
        {
            "question": "What is the capital of France?",
            "options": ["Berlin", "Madrid", "Paris", "Rome"],
            "correct_option": 3
        },
        {
            "question": "Who wrote '1984'?",
            "options": ["George Orwell", "J.K. Rowling", "Mark Twain", "Ernest Hemingway"],
            "correct_option": 1
        },
        {
            "question": "What is 5 + 7?",
            "options": ["11", "12", "13", "14"],
            "correct_option": 2
        }
    ]
    
    print("Welcome to the Python Quiz!\n")
    
    # Ask each question
    for q in questions:
        correct = ask_question(q["question"], q["options"], q["correct_option"])
        if correct:
            score += 1
    
    # Print final score
    print(f"\nYour final score is: {score}/{len(questions)}")

if __name__ == "__main__":
    main()
