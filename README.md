# D385 Study Master 🎓

**[🚀 Try the Live App](https://zwhiteshadow.github.io/d385-study-master/study_app.html)**

A comprehensive study application for WGU's D385 Software Engineering Capstone course, featuring interactive patterns, quiz questions, and flashcards to help you master the material.

## 🌟 Key Features

### 📊 Smart Weighted Scoring
- **Patterns: 45%** | **Quiz: 35%** | **Cards: 20%** (reflects exam importance & time)
- Real exam: 31 questions (14 patterns + 17 other)
- Practice app: 68 questions for thorough preparation
- Individual pass/fail indicators per mode (70% threshold)
- "🎓 Congratulations, you're ready!" when you hit 70% exam readiness
- Real-time progress tracking with percentages

### ⏱️ Intelligent Timer (4 hours)
- Auto-starts, counts down from 4:00:00
- **Weighted time tracking** (Patterns: 7.7 min, Quiz: 3.5 min, Cards: 1.6 min)
- Tracks only **correct answers**
- Shows "+X Min Ahead" or "-X Min Behind" status
- Updates every 2 minutes + when you answer

### 🎓 Three Study Modes (68 questions)
- **Patterns (14)**: Interactive coding with Learning Mode, hints, full test questions
- **Quiz (24)**: Multiple choice with detailed explanations, difficulty tags
- **Flashcards (30)**: Self-paced review with category tags

### 🛠️ Advanced Tools
- **Learning Mode**: Side-by-side code editor with Levenshtein distance (real-time % match)
- **Study Tips**: Consolidated Reddit wisdom
- **Retry Options**: Reset individual modes or full app
- **Progress Bars**: Visual tracking for all 68 questions

## 🚀 Quick Start

1. **Clone the repository**:
   ```bash
   git clone https://github.com/ZWhiteShadow/d385-study-master.git
   cd d385-study-master
   ```

2. **Open the app**:
   - **Option A**: Use the [Live App](https://zwhiteshadow.github.io/d385-study-master/study_app.html) - No download needed!
   - **Option B**: Open `study_app.html` locally in any modern web browser
   - No installation or setup required!

3. **Start studying**:
   - Choose your study mode (Patterns, Quiz, or Flashcards)
   - Use the timer to track your progress
   - Access study tips for Reddit wisdom

## 📖 How to Use

### 🔵 Patterns Mode (45% of exam score)
- Practice 14 coding patterns (same 14 that appear on real exam!)
- **Learning Mode**: Side-by-side code editor with real-time Levenshtein distance feedback
  - Color-coded similarity (Green 90%+, Yellow 70-89%, Orange 50-69%, Red <50%)
  - Smart indentation and trailing whitespace detection
  - "I'm Ready - Test Me!" button at 100% match
- Unlimited retries to master each pattern

### 🟣 Quiz Mode (part of 55% - exam has 17, we have 54 practice)
- 24 multiple choice questions with detailed explanations for all options
- Once answered, can't re-answer (simulate exam conditions)
- View right/wrong answers even after completion

### 🟢 Flashcards Mode (part of 55% - exam has 17, we have 54 practice)
- 30 key concepts covering HTTP status codes, attacks, and prevention
- Self-assess as "Got it right" or "Got it wrong"
- Once answered, can't re-answer (locked like quiz)

## 🛠️ Technical Details

- **Pure HTML/CSS/JavaScript**: No build process required
- **React 18**: Modern component-based architecture
- **Tailwind CSS**: Responsive and beautiful styling
- **Babel**: JSX transpilation in the browser
- **Local Storage**: Progress is saved in your browser

## 📊 Real Exam vs Practice App

### Real D385 Exam
- **Total**: 31 questions in 4 hours
- **Patterns**: 14 questions (45% of exam)
- **Other**: 17 questions (55% of exam - mix of quiz/concept questions)

### Our Practice App
- **Total**: 68 practice questions
- **Patterns**: 14 questions (same as exam!)
- **Quiz**: 24 questions (extra practice)
- **Flashcards**: 30 questions (extra practice)

### Weighted Score Formula
Your "Exam Readiness" score reflects exam priorities:

```
Exam Readiness = (Patterns % × 0.45) + (Quiz % × 0.35) + (Cards % × 0.20)
```

**Time Allocation:**
- Patterns: 108 minutes (45%) → 7.7 min each
- Quiz: 84 minutes (35%) → 3.5 min each  
- Cards: 48 minutes (20%) → 1.6 min each

**Example:**
- Patterns: 12/14 = 85.7%
- Quiz: 20/24 = 83.3%
- Cards: 25/30 = 83.3%
- **Exam Readiness**: (85.7 × 0.45) + (83.3 × 0.35) + (83.3 × 0.20) = **38.6% + 29.2% + 16.7% = 84.5%** ✅ READY!

## 🎯 Study Strategy

1. **Master ALL 14 Patterns**: They're 45% of exam - these exact patterns appear on the test!
2. **Use Learning Mode**: Practice side-by-side until you hit 100% match consistently
3. **Complete Quiz Questions**: Build conceptual understanding (54 practice vs 17 on exam)
4. **Review Flashcards**: Memorize key concepts, HTTP codes, and security principles
5. **Monitor "Exam Readiness"**: Aim for 80%+ weighted score for confidence
6. **Use the Timer**: Simulate exam pressure - 3.5 minutes per correct answer
7. **Check Study Tips**: Reddit wisdom and best practices in the menu

**Pro Tip**: Getting 14/14 Patterns (100%) + 30/54 Quiz+Cards (55.6%) = **75.6% Exam Readiness** ✅ That's a pass! Focus on patterns!

## 🤝 Contributing

This project is open source! Feel free to:
- Add more questions or patterns
- Improve the UI/UX
- Fix bugs or add features
- Share your study tips

## 📝 License

This project is open source and available under the MIT License.

## 🙏 Acknowledgments

### 📚 Primary Sources
This study app was created using content and insights from the following sources:

- **[D385 Assessments - Notion](https://glass-diadem-acc.notion.site/D385-Assessments-3261412dc25f4bce829d34341f33e8b3)** - Comprehensive assessment materials and patterns
- **[D385 Pre-Assessment Flashcards](https://quizlet.com/813493586/d385-pre-assessment-all-correct-flash-cards/)** - Pre-assessment question bank
- **[D385 Flashcards](https://quizlet.com/902866897/d385-flash-cards/)** - Core concept flashcards
- **[D385 Malicious Attacks & Response Codes](https://quizlet.com/932321419/wgu-d385-malicious-attacks-and-response-codes-flash-cards/)** - Security-focused flashcards

### 🎯 Original Reddit Thread
All sources above were compiled from the comprehensive Reddit discussion:
**[Updated 11/2023 Software Security and Testing D385](https://www.reddit.com/r/wgu_devs/comments/17quy61/updated_112023_software_security_and_testing_d385/)**

### 🤖 AI Development
- **Prompt Engineering**: Wade Helquist
- **Practice Test Questions**: Generated entirely using prompt engineering with Cursor AI and Claude
- **Study Tips**: Consolidated from Reddit community wisdom and best practices
- **App Development**: Built with React, Tailwind CSS, and modern web technologies

### 👥 Community
- WGU D385 course materials
- Reddit community study tips and insights
- WGU Software Engineering students for feedback and testing

**Good luck with your D385 exam! 🍀**