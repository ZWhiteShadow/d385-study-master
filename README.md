# D385 Study Master 🎓

**[🚀 Try the Live App]g

A comprehensive study application for WGU's D385 Software Engineering Capstone course, featuring interactive patterns, quiz questions, and flashcards to help you master the material.

## 🌟 Key Features

### 📊 Smart Weighted Scoring
- **Patterns: 70%** | **Quiz+Cards: 30%** (reflects real exam weight)
- Individual pass/fail indicators per mode (70% threshold)
- "🎓 Congratulations, you passed!" message when you hit 70% weighted score
- Real-time progress tracking with percentages

### ⏱️ Intelligent Timer (4 hours)
- Auto-starts, counts down from 4:00:00
- Tracks only **correct answers** (3.5 min each)
- Shows "+X Min Ahead" or "-X Min Behind" status
- Updates every 3.5 minutes + when you answer

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
   git clone https://github.com/yourusername/d385-study-master.git
   cd d385-study-master
   ```

2. **Open the app**:
   - Simply open `study_app.html` in any modern web browser
   - No installation or setup required!

3. **Start studying**:
   - Choose your study mode (Patterns, Quiz, or Flashcards)
   - Use the timer to track your progress
   - Access study tips for Reddit wisdom

## 📖 How to Use

### 🔵 Patterns Mode (70% of score)
- Practice 14 coding patterns with hints, explanations, and full test questions
- **Learning Mode**: Side-by-side code editor with real-time Levenshtein distance feedback
  - Color-coded similarity (Green 90%+, Yellow 70-89%, Orange 50-69%, Red <50%)
  - Smart indentation and trailing whitespace detection
  - "I'm Ready - Test Me!" button at 100% match
- Unlimited retries to master each pattern

### 🟣 Quiz Mode (15% of score - part of 30%)
- 24 multiple choice questions with detailed explanations for all options
- Once answered, can't re-answer (simulate exam conditions)
- View right/wrong answers even after completion

### 🟢 Flashcards Mode (15% of score - part of 30%)
- 30 key concepts covering HTTP status codes, attacks, and prevention
- Self-assess as "Got it right" or "Got it wrong"
- Once answered, can't re-answer (locked like quiz)

## 🛠️ Technical Details

- **Pure HTML/CSS/JavaScript**: No build process required
- **React 18**: Modern component-based architecture
- **Tailwind CSS**: Responsive and beautiful styling
- **Babel**: JSX transpilation in the browser
- **Local Storage**: Progress is saved in your browser

## 📊 Test Distribution & Weighted Scoring

Based on Reddit community feedback and exam analysis:

| Section     | Questions | Weight | Time Allocation | Pass Threshold |
|-------------|-----------|--------|-----------------|----------------|
| Patterns    |    14     |  70%   |  49 minutes     |     70%        |
| Quiz        |    24     |  30%*  |  84 minutes     |     70%        |
| Flashcards  |    30     |  30%*  | 105 minutes     |     70%        |
| **Total**   |  **68**   | **100%** | **238 minutes** |   **70%**      |

*\*Quiz and Flashcards combined = 30% weight (54 questions total)*

### Weighted Score Formula
```
Final Score = (Patterns % × 0.70) + ((Quiz + Cards) % × 0.30)
```

**Example:**
- Patterns: 12/14 = 85.7%
- Quiz + Cards: 40/54 = 74.1%
- **Weighted Score**: (85.7 × 0.70) + (74.1 × 0.30) = **60% + 22.2% = 82.2%** ✅ PASSED!

## 🎯 Study Strategy

1. **Focus on Patterns FIRST**: They're 70% of your final score! Master all 14 patterns
2. **Use Learning Mode**: Practice patterns side-by-side with real-time feedback
3. **Complete Quiz Questions**: Test your conceptual understanding (24 questions)
4. **Review Flashcards**: Reinforce key concepts and definitions (30 cards)
5. **Monitor Your Progress**: Watch the weighted score and individual mode percentages
6. **Use the Timer**: Stay on track - aim for 3.5 minutes per correct answer
7. **Check Study Tips**: Access consolidated Reddit wisdom and best practices

**Pro Tip**: Since Patterns are 70% of your score, getting 14/14 Patterns (100%) and only 27/54 Quiz+Cards (50%) still gives you a passing score of 85%!

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