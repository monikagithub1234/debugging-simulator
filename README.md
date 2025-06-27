# debugging-simulator
🎉 Super thrilled to share my recent full-stack project — Python Debugging Simulator!

🧩 This tool is built to help learners and developers practice debugging Python code interactively through real-world challenges and guided feedback.

🔧 Core Features Include:
▫️ 20+ handpicked Python bugs and logical errors
▫️ Real-time error detection with clear test case validation
▫️ Scoring system, progress tracking, and reward badges
▫️ Fully responsive interface with modern UI elements and animations
▫️ Safe backend logic to run and validate user code securely

💡 What I learned:
➤ Exception handling and sandboxed code execution in Python
➤ Flask web framework integration with HTML frontend
➤ UI/UX design for interactive learning
➤ Creating a user-friendly code-based educational platform

👩‍💻 Built using:
🔹 Python, Flask
🔹 HTML/CSS with custom animations
🔹 JSON for challenge storage

🔍 I undertook this project as part of my academic journey to build tools that help learners understand errors deeply and improve debugging confidence.

✅ Live Demo Coming Soon!
🔗 Explore the code on GitHub: github.com/yourusername/debugging-simulator

Would love to hear your feedback or suggestions 😊

#Python #Flask #Debugging #WebDevelopment #ProgrammingTools #FinalYearProject #MonikaPriya #WomenInTech #TechForEducation

📘 📂 Extended GitHub README.md
markdown
Copy
Edit
# 🐞 Python Debugging Simulator

> An interactive Python learning platform focused on **identifying and fixing bugs** in real-time.

## ✨ Overview

The Python Debugging Simulator is a web-based application that helps users learn debugging by working through real code problems that contain intentional errors. The tool checks the user's fixes, validates them against test cases, and offers scores and feedback — making it ideal for students, educators, and coding enthusiasts.

## 🎯 Key Features

- ✅ **20+ Debug Challenges** – From syntax to logic errors
- ✅ **Instant Code Evaluation** – Execute and test your fix in real-time
- ✅ **Error Handling Feedback** – Learn *why* your code failed
- ✅ **Scoring System** – Earn points and track your improvement
- ✅ **Awards & Badges** – Unlock badges after hitting milestones
- ✅ **Modern UI/UX** – Responsive design with hover animations and center-aligned simulator title
- ✅ **Safe Code Execution** – Backend ensures safe evaluation of Python code

## 📌 Project Goals

- Help users **recognize common Python errors**
- Improve **debugging skills through hands-on practice**
- Build a **realistic, user-friendly simulator** for students and beginners

## 🛠️ Tech Stack

| Layer       | Tools Used                     |
|-------------|--------------------------------|
| Frontend    | HTML, CSS                      |
| Backend     | Python, Flask                  |
| Execution   | Custom secure code runner      |
| Storage     | JSON for challenge/test cases  |

## 📁 Project Structure

debugging-simulator/
│
├── app.py # Main Flask app
├── execute.py # Secure code execution logic
├── templates/
│ └── index.html # Frontend UI
├── static/
│ └── style.css # Styles for simulator
├── challenges/
│ └── challenge1.json # List of buggy code and test cases
└── README.md

csharp
Copy
Edit

## 🧪 Sample Challenge Format

Each challenge includes:
- Buggy Python code snippet
- Expected correct output
- Test cases to verify fix

```json
{
  "id": 1,
  "code": "def add(a, b): return a + b\nprint(add(3))",
  "expected_output": "Error: Invalid input",
  "test_cases": [
    {
      "input": "",
      "output": "Error: Invalid input"
    }
  ]
}
🚀 How to Run Locally
bash
Copy
Edit
# Step 1: Clone the repository
git clone https://github.com/yourusername/debugging-simulator.git
cd debugging-simulator

# Step 2: Create virtual environment
python -m venv venv
source venv/bin/activate  # For Windows: venv\Scripts\activate

# Step 3: Install dependencies
pip install flask

# Step 4: Run the app
python app.py

# Visit the simulator in your browser
http://127.0.0.1:5000/
🏆 Awards & Progress System
🧠 Each solved challenge = +10 points

❌ Failed attempts give hints (if enabled)

🏅 Badges every 5 correct fixes

🤝 Contributions
Feel free to:

Fork the repo

Submit issues or enhancements

Add new challenges via JSON

🙋 About Me
Monika Priya Nagam
🎓 4th Year Engineering Student | Full-Stack Enthusiast | Python Lover
📧 monikapriya@example.com
🌐 LinkedIn | GitHub

📄 License
Licensed under the MIT License.
