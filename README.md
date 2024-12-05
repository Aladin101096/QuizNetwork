# Python Quiz App

A GUI-based Python quiz application that dynamically loads questions from a text file and uses an obfuscated script for enhanced security.

---

## Features

- **Dynamic Questions**: Loads quiz questions and answers from an external `questions.txt` file.
- **Interactive GUI**: Built with `Tkinter` for a simple and user-friendly interface.
- **Security**: The Python script is obfuscated using PyArmor to protect the source code.
- **Cross-Platform**: Compatible with Windows, Linux, and macOS.

---

## Requirements

- Python 3.x
- `tkinter` module (`python3-tk` for Linux)
- The following files:
  - `GuiQuizApp.py` (main obfuscated script)
  - `questions.txt` (question data)
  - PyArmor runtime files (`pyarmor_runtime.so` and `__init__.py`).

---

## Installation and Usage

### 1. **Install Required Packages**
Ensure Python is installed on your system. If `tkinter` is not available, install it:
- **For Debian/Ubuntu**:
  ```bash
  sudo apt update
  sudo apt install python3-tk

3. Run the Application
Open a terminal or command prompt in the directory containing the files and execute:

bash
Copy code
python3 GuiQuizApp.py
4. Using the Application
The app will display a series of quiz questions.
Select your answer and press "Next" to proceed to the next question.
At the end, your score will be displayed along with a review of your answers.
Notes on Security
The script GuiQuizApp.py is obfuscated using PyArmor for code protection. Ensure the pyarmor_runtime files (pyarmor_runtime.so and __init__.py) are in the same directory as the script.
Contribution
Feel free to contribute by:

Adding more questions to questions.txt.
Improving the GUI or functionality of the app.
License
This project is for educational purposes. Please do not redistribute or modify the obfuscated script for commercial purposes without permission.

Troubleshooting
Error: No module named 'tkinter'
Install the tkinter module as mentioned in the requirements section.

Error: No module named 'pyarmor_runtime'
Ensure the pyarmor_runtime.so and __init__.py files are in the same directory as GuiQuizApp.py.

For any issues, feel free to reach out!

yaml
Copy code

---

### Next Steps
- Place this `README.md` file in the same directory as your project files.
- Share the directory as a zip or through a version control platform (e.g., GitHub, GitLab) for easy access by your colleagues.

Let me know if you need further adjustments!
