import random
import time

# Function to ask a question with input validation and timer
def ask_question(question, options, correct_option, time_limit=10):
    print("\n" + question)  
    for idx, option in enumerate(options, 1):
        print(f"{idx}. {option}")  

    start_time = time.time()
    
    while True:
        answer = input(f"Choose the correct option (1/2/3/4) within {time_limit} seconds: ")
        
        # Check if time limit is exceeded
        if time.time() - start_time > time_limit:
            print("Time's up!\n")
            return False
        
        # Validate input
        if answer.isdigit() and 1 <= int(answer) <= len(options):
            break
        print("Invalid input. Please enter a number between 1 and 4.")

    if int(answer) == correct_option:
        print("Correct!\n")
        return True
    else:
        print(f"Wrong! The correct answer is {options[correct_option - 1]}\n")
        return False

# Function to select a quiz category
def select_category():
    categories = {
        "1": "General Knowledge",
        "2": "Science",
        "3": "History"
    }
    
    print("\nSelect a quiz category:")
    for key, value in categories.items():
        print(f"{key}. {value}")
    
    while True:
        choice = input("Enter the category number: ")
        if choice in categories:
            return choice
        print("Invalid choice, please select a valid category.")

# Function to save high scores
def save_score(name, score, total_questions):
    with open("high_scores.txt", "a") as file:
        file.write(f"{name}: {score}/{total_questions}\n")

# Main function
def main():
    name = input("Enter your name: ")
    category = select_category()
    print(f"\nYou selected: {category}")

    # Define quiz questions for each category
    quiz_data = {
        "1": [
            {"question": "What is the capital of France?", "options": ["Berlin", "Madrid", "Paris", "Rome"], "correct_option": 3},
            {"question": "Who wrote '1984'?", "options": ["George Orwell", "J.K. Rowling", "Mark Twain", "Ernest Hemingway"], "correct_option": 1},
            {"question": "What is 5 + 7?", "options": ["11", "12", "13", "14"], "correct_option": 2}
        ],
        "2": [
            {"question": "What planet is known as the Red Planet?", "options": ["Earth", "Mars", "Jupiter", "Venus"], "correct_option": 2},
            {"question": "What is the chemical symbol for water?", "options": ["O2", "CO2", "H2O", "N2"], "correct_option": 3},
            {"question": "How many bones are in the adult human body?", "options": ["206", "180", "250", "300"], "correct_option": 1}
        ],
        "3": [
            {"question": "Who was the first President of the United States?", "options": ["Abraham Lincoln", "Thomas Jefferson", "George Washington", "John Adams"], "correct_option": 3},
            {"question": "In what year did World War II end?", "options": ["1945", "1939", "1918", "1950"], "correct_option": 1},
            {"question": "What ancient civilization built the pyramids?", "options": ["Romans", "Greeks", "Egyptians", "Mayans"], "correct_option": 3}
        ]
    }

    # Get the selected category's questions
    questions = quiz_data[category]
    
    # Shuffle questions
    random.shuffle(questions)

    score = 0

    print("\nWelcome to the Python Quiz!\n")

    # Ask each question
    for q in questions:
        if ask_question(q["question"], q["options"], q["correct_option"]):
            score += 1

    # Print final score
    print(f"\n{name}, your final score is: {score}/{len(questions)}")

    # Save the score
    save_score(name, score, len(questions))
    print("Your score has been saved!")

if __name__ == "__main__":
    main()
