import json
import os

# Function to load knowledge base from JSON file
def load_knowledge_base(file_path):
    if os.path.exists(file_path):
        with open(file_path, 'r') as file:
            return json.load(file)
    return {}

# Function to save knowledge base to JSON file
def save_knowledge_base(knowledge_base, file_path):
    with open(file_path, 'w') as file:
        json.dump(knowledge_base, file, indent=4)

# Simple response function to handle basic questions
def respond_to_question(question, knowledge_base):
    # Normalize the question to lowercase for consistent lookup
    question_key = question.lower()
    if question_key in knowledge_base:
        return knowledge_base[question_key]
    else:
        return "I don't know the answer to that question."

# Main learning function
def main():
    knowledge_base_file = 'knowledgebase.json'
    knowledge_base = load_knowledge_base(knowledge_base_file)

    print("Welcome to the Q&A bot! Type 'exit' to quit.")

    while True:
        question = input("What do you want to ask? ").strip()
        if question.lower() == 'exit':
            break

        # Get response
        response = respond_to_question(question, knowledge_base)
        print(f"Response: {response}")

        # If the bot doesn't know the answer, learn from the user
        if response == "I don't know the answer to that question.":
            answer = input("Please provide the answer so I can learn: ").strip()
            knowledge_base[question.lower()] = answer  # Save question in lowercase
            save_knowledge_base(knowledge_base, knowledge_base_file)
            print("Thank you! I've learned something new.")

if __name__ == "__main__":
    main()
