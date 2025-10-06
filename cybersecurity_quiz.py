#!/usr/bin/env python3
"""
Interactive Cybersecurity Quiz Script
Focuses on Practice Labs (2.10-2.14) and Multiple Choice Questions from Pre-Assessment
Created for studying cybersecurity concepts and Python security implementations
"""

import random
import time
import sys
from datetime import datetime

class CybersecurityQuiz:
    def __init__(self):
        self.score = 0
        self.total_questions = 0
        self.start_time = None
        self.questions_answered = []
        
    def display_header(self):
        """Display quiz header with current time and progress tracking"""
        current_time = datetime.now().strftime("%H:%M:%S")
        print("=" * 60)
        print("🔐 CYBERSECURITY INTERACTIVE QUIZ 🔐")
        print("=" * 60)
        print(f"📅 Started at: {current_time}")
        print("📚 Focus: Practice Labs & Multiple Choice Questions")
        print("🎯 Topics: Input Validation, Security Vulnerabilities, Python Security")
        print("=" * 60)
        
    def calculate_eta(self):
        """Calculate and display estimated time remaining"""
        if self.start_time and self.total_questions > 0:
            elapsed = time.time() - self.start_time
            avg_time_per_question = elapsed / max(1, len(self.questions_answered))
            remaining_questions = self.total_questions - len(self.questions_answered)
            eta_seconds = remaining_questions * avg_time_per_question
            
            hours = int(eta_seconds // 3600)
            minutes = int((eta_seconds % 3600) // 60)
            seconds = int(eta_seconds % 60)
            
            print(f"⏱️  ETA: {hours}h {minutes}m {seconds}s remaining")
    
    def show_progress(self):
        """Show current progress with detailed updates"""
        answered = len(self.questions_answered)
        percentage = (answered / self.total_questions * 100) if self.total_questions > 0 else 0
        
        print(f"\n📊 Progress: {answered}/{self.total_questions} ({percentage:.1f}%)")
        print(f"🎯 Current Score: {self.score}/{answered}" if answered > 0 else "🎯 Current Score: 0/0")
        
        if answered > 0:
            accuracy = (self.score / answered) * 100
            print(f"📈 Accuracy: {accuracy:.1f}%")
        
        self.calculate_eta()
        print("-" * 60)

    def get_practice_lab_questions(self):
        """Practice lab questions focusing on code implementation"""
        return [
            {
                "type": "code_completion",
                "topic": "Input Validation - Range Check",
                "question": "Complete this code to validate that a number is within range 1-10 (inclusive):",
                "code": "r = range(1, 11)\nnum = int(input())\n# Create conditional statement for range check here\nif ___:\n    print(\"The number input is in the range from 1 and 10.\")\nelse:\n    print(\"The number input is not in the range from 1 and 10.\")",
                "answer": "num in r",
                "explanation": "Use 'num in r' to check if the number is within the range 1-10 (inclusive). Note: range(1, 11) creates [1, 2, 3, 4, 5, 6, 7, 8, 9, 10]"
            },
            {
                "type": "code_completion", 
                "topic": "Input Validation - Length Check",
                "question": "Complete this code to validate password length (minimum 8 characters):",
                "code": "password = input()\n# Write an if/else statement to evaluate password length\nif ___: \n    print(\"Your password is long enough.\")\nelse:\n    print(\"Your password is too short.\")",
                "answer": "len(password) >= 8",
                "explanation": "Use 'len(password) >= 8' to check if the password has at least 8 characters"
            },
            {
                "type": "code_debug",
                "topic": "Least Privilege Implementation",
                "question": "What's wrong with this least privilege code? Identify the bug:",
                "code": "def grant_permission(name_list, filename):\n    if result:  # BUG: 'result' is not defined in this function\n        os.chmod(filename, stat.S_IRWXU)\n    else:\n        os.chmod(filename, stat.S_IRUSR | stat.S_IRGRP | stat.S_IROTH)",
                "answer": "result is not defined in function scope",
                "explanation": "The variable 'result' is used but not defined within the function scope. It should be passed as a parameter or defined within the function."
            },
            {
                "type": "code_analysis",
                "topic": "Assert Statements",
                "question": "What will this assert statement output when called with ['user']?",
                "code": "def authorizeAdmin(usr):\n    assert isinstance(usr, list) and usr != [], \"No user found\"\n    assert 'admin' in usr, \"No admin found.\"\n    print(\"You are granted full access to the application.\")\n\nauthorizeAdmin(['user'])",
                "answer": "AssertionError: No admin found",
                "explanation": "The first assert passes (['user'] is a non-empty list), but the second fails because 'admin' is not in ['user'], raising AssertionError with message 'No admin found.'"
            }
        ]

    def get_multiple_choice_questions(self):
        """Multiple choice questions from Pre-Assessment files"""
        return [
            {
                "type": "multiple_choice",
                "topic": "Input Validation",
                "question": "Which type of input validation does this code show?\n\nisValidNumber = False\nwhile not isValidNumber:\n    try:\n        pickedNumber = int(input('Pick a number from 1 to 10'))\n        if pickedNumber >= 1 and pickedNumber <= 10:\n            isValidNumber = True\n    except:\n        print('You must enter a valid number from 1 to 10')",
                "options": ["A. Type and range check", "B. Type and length check", "C. Length and range check", "D. Invalid number check"],
                "answer": "A",
                "explanation": "The code performs both type checking (int conversion) and range checking (1-10), making it a type and range check validation."
            },
            {
                "type": "multiple_choice",
                "topic": "SQL Injection",
                "question": "Which method is used for a SQL injection attack?",
                "options": ["A. Exploiting query parameters", "B. Passing safe query parameters", "C. Using SQL composition", "D. Utilizing literal parameters"],
                "answer": "A",
                "explanation": "SQL injection attacks exploit query parameters by injecting malicious SQL code into vulnerable queries when input is not properly sanitized."
            },
            {
                "type": "multiple_choice",
                "topic": "Cross-Site Scripting (XSS)",
                "question": "An attacker exploits a cross-site scripting vulnerability. What is the attacker able to do?",
                "options": ["A. Access the user's data", "B. Execute a shell command or script", "C. Discover other users' credentials", "D. Gain access to sensitive files on the server"],
                "answer": "A",
                "explanation": "XSS allows attackers to inject malicious scripts that execute in users' browsers, enabling them to access user data, cookies, and perform actions on behalf of the victim."
            },
            {
                "type": "multiple_choice",
                "topic": "Log Injection Defense",
                "question": "What is the primary defense against log injection attacks?",
                "options": ["A. Sanitize outbound log messages", "B. Do not use parameterized stored procedures in the database", "C. Allow all users to write to these logs", "D. Use API calls to log actions"],
                "answer": "A",
                "explanation": "Sanitizing outbound log messages prevents malicious content from being injected into logs, protecting against log injection attacks."
            },
            {
                "type": "multiple_choice",
                "topic": "Defensive Coding",
                "question": "What are two common defensive coding techniques?",
                "options": ["A. Check functional preconditions and postconditions", "B. Encrypt passwords and email submissions", "C. Adjust length and encoding of messages", "D. Develop code with exceptions to find errors"],
                "answer": "A",
                "explanation": "Checking preconditions (input validation) and postconditions (output verification) are fundamental defensive coding techniques that improve code reliability and security."
            },
            {
                "type": "multiple_choice",
                "topic": "Regression Testing",
                "question": "Which package is meant for internal use by Python for regression testing?",
                "options": ["A. test", "B. regress test", "C. doctest", "D. assert"],
                "answer": "A",
                "explanation": "The 'test' package is Python's internal testing suite used for regression testing of the Python interpreter and standard library."
            },
            {
                "type": "multiple_choice",
                "topic": "Penetration Testing",
                "question": "Consider this penetration test code checking for HSTS headers. Which security vulnerability is being tested?\n\nimport requests\nurls = open('websites.txt', 'r')\nfor url in urls:\n    url = url.strip()\n    req = requests.get(url)\n    try:\n        transport_security = req.headers['Strict-Transport-Security']\n    except:\n        print('HSTS header not set properly')",
                "options": ["A. Man-in-the-middle", "B. Cross-site scripting", "C. Denial of service", "D. Code injection"],
                "answer": "A",
                "explanation": "The code checks for HSTS (HTTP Strict Transport Security) headers, which protect against man-in-the-middle attacks by enforcing HTTPS connections."
            },
            {
                "type": "multiple_choice",
                "topic": "Access Control",
                "question": "A security analyst noticed a vulnerability where an attacker took over multiple users' accounts. Which vulnerability was encountered?",
                "options": ["A. Broken access control", "B. Broken function level authorization", "C. API mass assignment", "D. Privilege escalation"],
                "answer": "A",
                "explanation": "Broken access control occurs when access control mechanisms fail to prevent unauthorized access to user accounts or resources."
            },
            {
                "type": "multiple_choice",
                "topic": "Privilege Escalation Prevention",
                "question": "When creating a new user via API with fields (Name, Email, Password, IsAdmin), what's the best way to protect against privilege escalation?",
                "options": ["A. Implement resource and field-level access control", "B. Ensure incoming requests are rate limited", "C. Remove IsAdmin from the endpoint", "D. Encrypt the incoming request"],
                "answer": "A",
                "explanation": "Implementing resource and field-level access control ensures only authorized users can access the endpoint and modify the IsAdmin field, preventing privilege escalation."
            }
        ]

    def ask_question(self, question_data):
        """Ask a single question and handle the response"""
        print(f"\n🔍 Topic: {question_data['topic']}")
        print(f"❓ {question_data['question']}")
        print("-" * 60)
        
        if question_data['type'] == 'code_completion':
            print("💻 Complete the code:")
            print(question_data['code'])
            
        elif question_data['type'] == 'code_debug':
            print("🐛 Debug this code:")
            print(question_data['code'])
            
        elif question_data['type'] == 'code_analysis':
            print("🔍 Analyze this code:")
            print(question_data['code'])
            
        elif question_data['type'] == 'multiple_choice':
            for option in question_data['options']:
                print(f"   {option}")
        
        print("-" * 60)
        
        # Get user input
        if question_data['type'] == 'multiple_choice':
            user_answer = input("Enter your answer (A, B, C, or D): ").strip().upper()
        else:
            user_answer = input("Enter your answer: ").strip()
        
        # Check answer
        correct = False
        if question_data['type'] == 'multiple_choice':
            correct = user_answer == question_data['answer']
        else:
            correct = user_answer.lower() == question_data['answer'].lower()
        
        # Provide feedback
        if correct:
            print("✅ CORRECT!")
            self.score += 1
        else:
            print("❌ INCORRECT!")
            if question_data['type'] == 'multiple_choice':
                print(f"Correct answer: {question_data['answer']}")
            else:
                print(f"Correct answer: {question_data['answer']}")
        
        print(f"💡 Explanation: {question_data['explanation']}")
        
        self.questions_answered.append({
            'question': question_data['question'],
            'user_answer': user_answer,
            'correct': correct,
            'topic': question_data['topic']
        })
        
        return correct

    def run_quiz(self):
        """Main quiz execution"""
        self.display_header()
        
        # Get all questions
        practice_questions = self.get_practice_lab_questions()
        mc_questions = self.get_multiple_choice_questions()
        all_questions = practice_questions + mc_questions
        
        # Shuffle questions for variety
        random.shuffle(all_questions)
        
        # Ask user how many questions they want
        print(f"\n📋 Available Questions:")
        print(f"   💻 Practice Lab Questions: {len(practice_questions)}")
        print(f"   📝 Multiple Choice Questions: {len(mc_questions)}")
        print(f"   📊 Total Available: {len(all_questions)}")
        
        while True:
            try:
                num_questions = int(input(f"\n🎯 How many questions would you like? (1-{len(all_questions)}): "))
                if 1 <= num_questions <= len(all_questions):
                    break
                else:
                    print(f"❌ Please enter a number between 1 and {len(all_questions)}")
            except ValueError:
                print("❌ Please enter a valid number")
        
        self.total_questions = num_questions
        self.start_time = time.time()
        
        # Select questions
        selected_questions = all_questions[:num_questions]
        
        print(f"\n🚀 Starting quiz with {num_questions} questions...")
        print("=" * 60)
        
        # Ask questions
        for i, question in enumerate(selected_questions, 1):
            print(f"\n📝 Question {i} of {num_questions}")
            self.show_progress()
            self.ask_question(question)
            
            if i < num_questions:
                input("\n⏸️  Press Enter to continue to next question...")
        
        # Show final results
        self.show_final_results()

    def show_final_results(self):
        """Display final quiz results"""
        end_time = time.time()
        total_time = end_time - self.start_time if self.start_time else 0
        
        print("\n" + "=" * 60)
        print("🎉 QUIZ COMPLETED! 🎉")
        print("=" * 60)
        
        # Time calculations
        hours = int(total_time // 3600)
        minutes = int((total_time % 3600) // 60)
        seconds = int(total_time % 60)
        
        print(f"⏱️  Total Time: {hours}h {minutes}m {seconds}s")
        print(f"📊 Final Score: {self.score}/{self.total_questions}")
        
        # Calculate percentage
        percentage = (self.score / self.total_questions * 100) if self.total_questions > 0 else 0
        print(f"📈 Accuracy: {percentage:.1f}%")
        
        # Performance assessment
        if percentage >= 90:
            print("🌟 EXCELLENT! You have mastered these cybersecurity concepts!")
        elif percentage >= 80:
            print("👍 GOOD JOB! You have a solid understanding of cybersecurity principles!")
        elif percentage >= 70:
            print("📚 FAIR! Review the topics you missed and try again!")
        else:
            print("🔄 NEEDS IMPROVEMENT! Study the materials more thoroughly!")
        
        # Topic breakdown
        print("\n📋 Topic Performance:")
        topic_scores = {}
        for q in self.questions_answered:
            topic = q['topic']
            if topic not in topic_scores:
                topic_scores[topic] = {'correct': 0, 'total': 0}
            topic_scores[topic]['total'] += 1
            if q['correct']:
                topic_scores[topic]['correct'] += 1
        
        for topic, scores in topic_scores.items():
            accuracy = (scores['correct'] / scores['total'] * 100) if scores['total'] > 0 else 0
            print(f"   {topic}: {scores['correct']}/{scores['total']} ({accuracy:.1f}%)")
        
        # Show incorrect answers for review
        incorrect_answers = [q for q in self.questions_answered if not q['correct']]
        if incorrect_answers:
            print(f"\n❌ Questions to Review ({len(incorrect_answers)}):")
            for i, q in enumerate(incorrect_answers, 1):
                print(f"   {i}. {q['topic']}: {q['question'][:50]}...")
        
        print("\n" + "=" * 60)
        print("🎓 Keep studying and practicing cybersecurity concepts!")
        print("🔐 Security is an ongoing learning process!")
        print("=" * 60)

def main():
    """Main function to run the quiz"""
    try:
        quiz = CybersecurityQuiz()
        quiz.run_quiz()
    except KeyboardInterrupt:
        print("\n\n⏹️  Quiz interrupted by user. Goodbye!")
        sys.exit(0)
    except Exception as e:
        print(f"\n❌ An error occurred: {e}")
        sys.exit(1)

if __name__ == "__main__":
    main()
