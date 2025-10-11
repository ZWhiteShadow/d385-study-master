# D385 Study Master 🎓

**[🚀 Try the Live App]g

A comprehensive study application for WGU's D385 Software Engineering Capstone course, featuring interactive patterns, quiz questions, and flashcards to help you master the material.

## 🌟 Features

### 📚 Three Study Modes
- **Patterns (14)**: Interactive coding patterns with hints, explanations, and original questions
  - **Learning Mode**: Side-by-side code editor with real-time similarity feedback
  - Uses Levenshtein distance algorithm for accurate code comparison
  - Smart indentation and whitespace detection
  - "I'm Ready" button appears at 100% to test your knowledge
- **Quiz (24)**: Multiple choice questions with detailed explanations
  - Difficulty levels: Easy, Medium, Hard
  - Category tags for organized studying
  - Detailed explanations for all answer options
- **Flashcards (30)**: Self-paced flashcard review system
  - Difficulty levels and category tags
  - Covers HTTP status codes, attacks, prevention, and more

### ⏱️ Smart Timer
- **4-hour countdown timer** matching the actual exam duration
- **Intelligent time tracking**: 3.5 minutes per CORRECT question
- **Progress indicators** showing if you're ahead or behind schedule
  - Updates every 3.5 minutes and when you answer correctly
  - Only counts correct answers toward expected time
  - Formula: `(correct_answers × 3.5 min) - time_elapsed`

### 🎯 Scoring System
- **Weighted Final Score**: Patterns 70%, Quiz+Cards 30%
  - Reflects actual exam importance
  - Shows individual pass/fail for each mode (70% threshold)
  - Overall "Congratulations, you passed!" message when complete
- **Individual Mode Progress**: Track percentage for Patterns, Quiz, and Cards separately
- **Retry Options**: 
  - Retry individual modes (clears that mode's scores, timer keeps running)
  - Reset All (clears everything and resets timer to 4 hours)

### 🎓 Study Tools
- **Study Tips Panel**: Consolidated Reddit wisdom and best practices
- **Progress Tracking**: Visual indicators for completed questions
- **Randomization**: Questions and patterns shuffle on each session
- **Original Questions**: Full-length test questions with line numbers

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

### Patterns Mode
- Practice coding patterns with hints and explanations
- Click "Show Original Question" to see full test questions
- Get immediate feedback with Levenshtein distance similarity scoring
- **Learning Mode**: 
  - Toggle side-by-side comparison with correct answer
  - Real-time percentage match as you type
  - Color-coded feedback (Green 90%+, Yellow 70-89%, Orange 50-69%, Red <50%)
  - Indentation warning: Detects when you use wrong number of spaces (PEP 8 recommends 4)
  - Trailing whitespace detection: Alerts you to extra spaces at line ends
  - "I'm Ready - Test Me!" button appears when you reach 100% match

### Quiz Mode
- Answer multiple choice questions
- View detailed explanations for each option
- Track your progress with visual indicators

### Flashcards Mode
- Review key concepts and definitions
- Rate yourself as "Got it right" or "Got it wrong"
- Self-paced learning with progress tracking

### Timer Features
- **Auto-Start**: Timer starts automatically when you begin
- **Start/Pause/Reset**: Full control over the 4-hour countdown
- **Real-Time Progress**: See if you're ahead or behind schedule
- **Smart Calculation**: Only counts correct answers (3.5 minutes each)
- **Updates every 3.5 minutes**: Status refreshes periodically for accuracy

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