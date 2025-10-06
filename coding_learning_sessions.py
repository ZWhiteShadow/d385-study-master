#!/usr/bin/env python3
"""
Interactive Coding Learning Sessions
Socratic Method Learning for Cybersecurity Python Examples
Focuses on understanding code through guided questions and analysis
"""

import time
import sys
from datetime import datetime

class CodingLearningSessions:
    def __init__(self):
        self.session_start_time = None
        self.topics_completed = []
        
    def display_header(self):
        """Display learning session header"""
        current_time = datetime.now().strftime("%H:%M:%S")
        print("=" * 70)
        print("🎓 INTERACTIVE CODING LEARNING SESSIONS 🎓")
        print("=" * 70)
        print(f"📅 Started at: {current_time}")
        print("🧠 Method: Socratic Learning (Questions & Discovery)")
        print("🔐 Focus: Understanding Cybersecurity Python Code")
        print("=" * 70)
        
    def ask_guided_question(self, question, hints=None):
        """Ask a guided question with optional hints"""
        print(f"\n🤔 {question}")
        if hints:
            print("💡 Hints:")
            for i, hint in enumerate(hints, 1):
                print(f"   {i}. {hint}")
        
        response = input("\n💭 Your thoughts: ").strip()
        return response
        
    def explain_concept(self, concept, explanation):
        """Provide detailed explanation of a concept"""
        print(f"\n📚 {concept}")
        print("=" * 50)
        print(explanation)
        print("=" * 50)
        
    def analyze_code_line_by_line(self, code, topic):
        """Analyze code line by line with guided questions"""
        print(f"\n🔍 CODE ANALYSIS: {topic}")
        print("=" * 60)
        
        lines = code.strip().split('\n')
        for i, line in enumerate(lines, 1):
            if line.strip():  # Skip empty lines
                print(f"\n📝 Line {i}: {line}")
                
                # Ask guiding questions based on the line
                if "import" in line:
                    response = self.ask_guided_question(
                        f"What does this import statement do? Why might we need it for {topic}?",
                        ["What module is being imported?", "What functionality does it provide?"]
                    )
                    
                elif "def " in line:
                    response = self.ask_guided_question(
                        "What is this function supposed to do? What parameters does it take?",
                        ["Look at the function name", "Check the parameters in parentheses"]
                    )
                    
                elif "if " in line or "elif " in line:
                    response = self.ask_guided_question(
                        "What condition is being checked here? Why is this check important?",
                        ["What happens if the condition is True?", "What happens if it's False?"]
                    )
                    
                elif "return" in line:
                    response = self.ask_guided_question(
                        "What is this function returning? Why is this the correct return value?",
                        ["What should the function output?", "How does this help the overall program?"]
                    )
                    
                else:
                    response = self.ask_guided_question(
                        "What does this line accomplish? How does it contribute to the overall goal?",
                        ["Look at the variable names", "Consider the data being manipulated"]
                    )
                
                input("\n⏸️  Press Enter when you've thought about this line...")
        
        print("\n✅ Code analysis complete!")
        
    def run_hashing_session(self):
        """Interactive session for understanding hashing concepts"""
        print("\n🔐 HASHING CONCEPTS SESSION")
        print("=" * 50)
        
        # Explain what hashing is
        self.explain_concept(
            "What is Hashing?",
            """Hashing is a one-way cryptographic function that converts input data into a fixed-size string.
            
Key Concepts:
• One-way: You can't reverse a hash to get the original data
• Fixed-size: Same length output regardless of input size  
• Deterministic: Same input always produces same hash
• Used for: Password storage, data integrity, digital signatures

Security Benefits:
• Passwords stored as hashes can't be "decrypted"
• Even if database is compromised, original passwords are safe
• Can verify data hasn't been tampered with"""
        )
        
        # Analyze the hashing code
        hashing_code = '''import hashlib

def hash_password(pwd):
    # encode password string to bytes
    enc_pwd = pwd.encode()
    
    # call the sha3_256() function returns a hash object
    d = hashlib.sha3_256()
    d.update(enc_pwd)
    
    # generate binary hash of password string in hexidecimal
    hash = d.hexdigest()
    
    return hash'''
        
        self.analyze_code_line_by_line(hashing_code, "Password Hashing")
        
        # Guided questions about the implementation
        self.ask_guided_question(
            "Why do we use SHA-3-256 instead of MD5 or SHA-1 for password hashing?",
            ["Research the security vulnerabilities of older hash functions", "What makes SHA-3 more secure?"]
        )
        
        self.ask_guided_question(
            "Why do we convert the password to bytes before hashing?",
            ["Hash functions work on binary data", "What happens if we pass a string directly?"]
        )
        
        self.explain_concept(
            "SHA-3-256 Security",
            """SHA-3-256 is considered cryptographically secure because:
• Produces 256-bit (32-byte) hash values
• Resistant to collision attacks
• Resistant to preimage attacks  
• Part of the SHA-3 family (Keccak algorithm)
• Recommended by NIST for security applications

This is why it's used instead of:
• MD5: Vulnerable to collision attacks
• SHA-1: Vulnerable to collision attacks
• SHA-2: Still secure, but SHA-3 is newer and more robust"""
        )
        
        self.topics_completed.append("Hashing Concepts")
        
    def run_logging_session(self):
        """Interactive session for understanding logging concepts"""
        print("\n📝 LOGGING CONCEPTS SESSION")
        print("=" * 50)
        
        self.explain_concept(
            "What is Logging?",
            """Logging is the process of recording events and messages during program execution.

Logging Levels (in order of severity):
• DEBUG (10): Detailed information for diagnosing problems
• INFO (20): General information about program execution  
• WARNING (30): Something unexpected happened, but program continues
• ERROR (40): A serious problem occurred, some function failed
• CRITICAL (50): A very serious error occurred, program may stop

Security Benefits:
• Track suspicious activities and security events
• Monitor system behavior for anomalies
• Audit trail for compliance and forensic analysis
• Debug security vulnerabilities"""
        )
        
        logging_code = '''import logging

logging.basicConfig(level=logging.DEBUG, format='%(levelname)s:%(message)s')

def logMessage(numIn):
    if numIn == "10":
        logging.debug("10: Debug test…")
        return "Debug test…"
    
    if numIn == "20":
        logging.info("20: Program successful!")
        return "Program successful!"
    
    if numIn == "30":
        logging.warning("30: Warning, there could be errors…")
        return "Warning, there could be errors…"
    
    if numIn == "40":
        logging.error("40: Program encountered an error!")
        return "Program encountered an error!"
    
    if numIn == "50":
        logging.critical("50: The program has stopped working!")
        return "The program has stopped working!"'''
        
        self.analyze_code_line_by_line(logging_code, "Logging Implementation")
        
        self.ask_guided_question(
            "Why do we configure the logging level to DEBUG? What happens if we set it to ERROR?",
            ["Think about what messages would be shown", "Consider when you want to see all messages vs only errors"]
        )
        
        self.ask_guided_question(
            "How could an attacker exploit logging if we log user input without sanitization?",
            ["What is log injection?", "How could malicious input affect log files?"]
        )
        
        self.explain_concept(
            "Log Injection Prevention",
            """Log Injection occurs when attackers inject malicious content into log messages.

Attack Example:
• User input: "admin\nERROR: Password changed to 'hacked'"
• Log entry: "User admin logged in\nERROR: Password changed to 'hacked'"

Prevention:
• Sanitize all user input before logging
• Use structured logging with separate fields
• Validate and escape special characters
• Never log sensitive information (passwords, tokens)

The quiz question about 'sanitizing outbound log messages' addresses this exact vulnerability."""
        )
        
        self.topics_completed.append("Logging Concepts")
        
    def run_hash_table_session(self):
        """Interactive session for understanding hash tables"""
        print("\n🗂️ HASH TABLE CONCEPTS SESSION")
        print("=" * 50)
        
        self.explain_concept(
            "What is a Hash Table?",
            """A hash table is a data structure that maps keys to values using a hash function.

How it works:
1. Hash function converts key to array index
2. Store value at that index
3. Handle collisions (multiple keys map to same index)

Benefits:
• Fast lookup: O(1) average case
• Fast insertion and deletion
• Used in databases, caches, symbol tables

Security Applications:
• Password storage (as we saw in hashing)
• Digital signatures
• Message authentication codes
• Bloom filters for spam detection"""
        )
        
        hash_table_code = '''def simple_hash_function(city_id, num_slots):
    return city_id % num_slots

def process_cities(input_str):
    city_list = input_str.split(',')
    hash_table = {slot: [] for slot in range(10)}
    
    for city in city_list:
        city_info = city.split()
        city_id = int(city_info[0])
        city_name = " ".join(city_info[1:])
        slot = simple_hash_function(city_id, 10)
        hash_table[slot].append(city_name)
    
    return hash_table'''
        
        self.analyze_code_line_by_line(hash_table_code, "Hash Table Implementation")
        
        self.ask_guided_question(
            "Why do we use modulo (%) operation in the hash function? What happens if we don't?",
            ["Think about array bounds", "What if city_id is 1000 but we only have 10 slots?"]
        )
        
        self.ask_guided_question(
            "How does chaining handle collisions? What would happen without chaining?",
            ["What if two cities have IDs that map to the same slot?", "How does the list help?"]
        )
        
        self.explain_concept(
            "Hash Function Properties",
            """Good hash functions should have:

1. Uniform Distribution: Keys should be evenly distributed across slots
2. Deterministic: Same input always produces same output  
3. Fast Computation: Should be quick to calculate
4. Minimal Collisions: Few keys should map to same slot

Our simple hash function (city_id % 10):
• Uniform: If city IDs are random, distribution is even
• Deterministic: Always same output for same input
• Fast: Modulo is O(1) operation
• Collisions: Possible (e.g., 11 and 21 both map to slot 1)

Security Note: For cryptographic hashing, we need additional properties like avalanche effect (small input changes cause large output changes)."""
        )
        
        self.topics_completed.append("Hash Table Concepts")
        
    def run_security_vulnerability_session(self):
        """Interactive session for understanding security vulnerabilities"""
        print("\n🛡️ SECURITY VULNERABILITY SESSION")
        print("=" * 50)
        
        self.explain_concept(
            "Common Security Vulnerabilities",
            """OWASP Top 10 Web Application Security Risks:

1. Injection (SQL, NoSQL, OS, LDAP)
2. Broken Authentication  
3. Sensitive Data Exposure
4. XML External Entities (XXE)
5. Broken Access Control
6. Security Misconfiguration
7. Cross-Site Scripting (XSS)
8. Insecure Deserialization
9. Using Components with Known Vulnerabilities
10. Insufficient Logging & Monitoring

Our labs focus on several of these!"""
        )
        
        # Analyze the template injection vulnerability
        vulnerability_code = '''from string import Template 

CONFIG = {
    "API_KEY": "'you've just exposed your secret_key'"
}

class User:
    def __init__(self, name, email):
        self.name = name
        self.email = email

name = input()
email = input()
user = User(name, email)

# VULNERABLE: Direct string formatting
# greeting = f"Hello, my name is {name}."

# SECURE: Using Template class
name_template = Template("Hello, my name is $name.")
greeting = name_template.substitute(name=name)'''
        
        self.analyze_code_line_by_line(vulnerability_code, "Template Injection Prevention")
        
        self.ask_guided_question(
            "What could an attacker do with malicious input like '${CONFIG[\"API_KEY\"]}' if we used f-strings?",
            ["What happens when Python evaluates expressions in f-strings?", "How could this expose sensitive data?"]
        )
        
        self.ask_guided_question(
            "Why is the Template class safer than f-strings or .format() for user input?",
            ["What does Template.substitute() do differently?", "How does it prevent code execution?"]
        )
        
        self.explain_concept(
            "Template Injection Attack",
            """Template Injection occurs when user input is processed as code/template syntax.

Attack Example with f-string:
• Input: "Jane Doe${CONFIG['API_KEY']}"
• Result: "Hello, my name is Jane Doeyou've just exposed your secret_key"

Why Template class is safe:
• Only substitutes named variables ($name)
• No expression evaluation
• No code execution
• Escapes special characters

Other prevention methods:
• Input validation and sanitization
• Output encoding
• Parameterized queries (for SQL)
• Content Security Policy (for XSS)"""
        )
        
        self.topics_completed.append("Security Vulnerabilities")
        
    def run_input_validation_session(self):
        """Interactive session for understanding input validation"""
        print("\n✅ INPUT VALIDATION SESSION")
        print("=" * 50)
        
        self.explain_concept(
            "Input Validation Importance",
            """Input validation is the process of checking user input before processing.

Types of Validation:
• Type checking: Ensure data is expected type (int, string, etc.)
• Range checking: Ensure value is within acceptable bounds
• Length checking: Ensure string length is appropriate
• Format checking: Ensure data matches expected pattern (email, phone)
• Content checking: Ensure no malicious content

Security Benefits:
• Prevents injection attacks
• Prevents buffer overflows
• Prevents data corruption
• Ensures data integrity"""
        )
        
        validation_code = '''# Range validation
r = range(1, 11)
num = int(input())
if num in r:
    print("The number input is in the range from 1 and 10.")
else:
    print("The number input is not in the range from 1 and 10.")

# Length validation  
password = input()
if len(password) >= 8:
    print("Your password is long enough.")
else: 
    print("Your password is too short.")

# Type validation
try:
    zipCode = int(input())
    print(f'Your zip code is {zipCode}.')
except ValueError:
    print('Please use numeric digits for the zip code.')'''
        
        self.analyze_code_line_by_line(validation_code, "Input Validation Examples")
        
        self.ask_guided_question(
            "Why do we need both client-side AND server-side validation?",
            ["What if an attacker bypasses the client?", "How could malicious requests be sent directly to the server?"]
        )
        
        self.ask_guided_question(
            "What happens if we don't validate input before using it in SQL queries?",
            ["Research SQL injection attacks", "How could malicious input break database queries?"]
        )
        
        self.explain_concept(
            "Defense in Depth",
            """Input validation is part of "Defense in Depth" strategy:

Layer 1: Client-side validation (UX, not security)
Layer 2: Server-side validation (primary security)
Layer 3: Parameterized queries (SQL injection prevention)
Layer 4: Output encoding (XSS prevention)
Layer 5: Access controls (authorization)
Layer 6: Logging and monitoring (detection)

Each layer provides additional protection. Never rely on just one layer!"""
        )
        
        self.topics_completed.append("Input Validation")
        
    def run_unit_testing_session(self):
        """Interactive session for understanding unit testing"""
        print("\n🧪 UNIT TESTING SESSION")
        print("=" * 50)
        
        self.explain_concept(
            "What is Unit Testing?",
            """Unit testing is testing individual components (units) of code in isolation.

Benefits:
• Catch bugs early in development
• Ensure code works as expected
• Prevent regressions when making changes
• Document expected behavior
• Improve code quality and confidence

Types of Assertions:
• assertEqual: Check if two values are equal
• assertIsNone: Check if value is None
• assertTrue/assertFalse: Check boolean conditions
• assertRaises: Check if exception is raised
• assertIn: Check if item is in container"""
        )
        
        testing_code = '''import unittest

def multiply_numbers(x, y):
    if x is None:
        print("x is a null value")
        return y
    elif y is None:
        print("y is a null value")
        return x
    else:
        return x * y   

class TestForNone(unittest.TestCase):
    def test_when_a_is_null(self):
        try:
            self.assertIsNone(multiply_numbers(5, None))
        except AssertionError as msg:
            print(msg)'''
        
        self.analyze_code_line_by_line(testing_code, "Unit Testing Implementation")
        
        self.ask_guided_question(
            "Why do we test for None values? What could happen if we don't handle them?",
            ["Think about what happens when you multiply by None", "How could this cause runtime errors?"]
        )
        
        self.ask_guided_question(
            "Why is the test failing? What should the function return when y is None?",
            ["Look at the function logic", "What does assertIsNone expect?"]
        )
        
        self.explain_concept(
            "Testing Best Practices",
            """Good unit tests should be:

1. Independent: Each test can run alone
2. Repeatable: Same result every time
3. Fast: Run quickly for frequent feedback
4. Clear: Easy to understand what's being tested
5. Comprehensive: Cover edge cases and error conditions

Security Testing:
• Test with malicious input
• Test boundary conditions
• Test error handling
• Test authentication and authorization
• Test data validation

The failing test shows the importance of understanding expected vs actual behavior!"""
        )
        
        self.topics_completed.append("Unit Testing")
        
    def show_session_summary(self):
        """Display summary of completed learning sessions"""
        end_time = time.time()
        total_time = end_time - self.session_start_time if self.session_start_time else 0
        
        print("\n" + "=" * 70)
        print("🎓 LEARNING SESSION SUMMARY 🎓")
        print("=" * 70)
        
        hours = int(total_time // 3600)
        minutes = int((total_time % 3600) // 60)
        seconds = int(total_time % 60)
        
        print(f"⏱️  Total Learning Time: {hours}h {minutes}m {seconds}s")
        print(f"📚 Topics Completed: {len(self.topics_completed)}")
        
        print("\n✅ Topics Covered:")
        for i, topic in enumerate(self.topics_completed, 1):
            print(f"   {i}. {topic}")
        
        print("\n🎯 Next Steps:")
        print("   1. Practice implementing these concepts in your own code")
        print("   2. Run the cybersecurity quiz to test your knowledge")
        print("   3. Experiment with the code examples")
        print("   4. Research additional security best practices")
        
        print("\n🔐 Remember:")
        print("   • Security is an ongoing learning process")
        print("   • Always validate and sanitize user input")
        print("   • Use defense in depth strategies")
        print("   • Test your code thoroughly")
        
        print("=" * 70)
        
    def run_all_sessions(self):
        """Run all learning sessions"""
        self.display_header()
        self.session_start_time = time.time()
        
        sessions = [
            ("Hashing Concepts", self.run_hashing_session),
            ("Logging Concepts", self.run_logging_session),
            ("Hash Table Concepts", self.run_hash_table_session),
            ("Security Vulnerabilities", self.run_security_vulnerability_session),
            ("Input Validation", self.run_input_validation_session),
            ("Unit Testing", self.run_unit_testing_session)
        ]
        
        print(f"\n📋 Available Learning Sessions:")
        for i, (name, _) in enumerate(sessions, 1):
            print(f"   {i}. {name}")
        
        print(f"\n🎯 Options:")
        print("   1. Run all sessions (recommended)")
        print("   2. Choose specific sessions")
        
        choice = input("\nEnter your choice (1 or 2): ").strip()
        
        if choice == "1":
            for name, session_func in sessions:
                print(f"\n🚀 Starting: {name}")
                session_func()
                input(f"\n⏸️  Press Enter to continue to next session...")
        else:
            print("\nSelect sessions to run (enter numbers separated by commas):")
            for i, (name, _) in enumerate(sessions, 1):
                print(f"   {i}. {name}")
            
            try:
                selected = input("\nEnter session numbers (e.g., 1,3,5): ").strip()
                indices = [int(x.strip()) - 1 for x in selected.split(',')]
                
                for idx in indices:
                    if 0 <= idx < len(sessions):
                        name, session_func = sessions[idx]
                        print(f"\n🚀 Starting: {name}")
                        session_func()
                        input(f"\n⏸️  Press Enter to continue...")
            except (ValueError, IndexError):
                print("❌ Invalid selection. Running all sessions...")
                for name, session_func in sessions:
                    print(f"\n🚀 Starting: {name}")
                    session_func()
                    input(f"\n⏸️  Press Enter to continue to next session...")
        
        self.show_session_summary()

def main():
    """Main function to run learning sessions"""
    try:
        sessions = CodingLearningSessions()
        sessions.run_all_sessions()
    except KeyboardInterrupt:
        print("\n\n⏹️  Learning session interrupted by user. Goodbye!")
        sys.exit(0)
    except Exception as e:
        print(f"\n❌ An error occurred: {e}")
        sys.exit(1)

if __name__ == "__main__":
    main()
