# FILE-INTEGRITY-CHECKER
This is a tool (software) that checks whether any file in your computer has been changed, deleted, or tampered with.
# File Integrity Checker
A simple desktop tool built in Python to monitor and detect unauthorized changes, deletions, or tampering in your files using hash values.

C FOLDER STRUCTURE 
Organize your files like this:
C:\FileIntegrityChecker\
          ├── dist\
          │   └── file_integrity_gui.exe      <-- Your compiled EXE (via PyInstaller)
          ├── hashes.json                     <-- Auto-generated when running
          ├── log.txt                         <-- Auto-generated when checking
          └── file_integrity_gui.py           <-- Your Python script
        

FEATURES
	Detects if any file is modified, deleted, or replaced
	Uses SHA-256 hashing for strong integrity checking
	Provides a user-friendly GUI (no coding knowledge required)
	Saves results in a `log.txt` file with timestamps
	Standalone `.exe` version available – no need for Python installation

TECHNOLOGIES USED

	`Python`
	`hashlib` – file hashing
	`tkinter` – GUI
	`json` – saving hash data
	`os`, `datetime` – file and time handling
	`pyinstaller` – to create .exe
	`Inno Setup` – to create installer (optional)

HOW TO RUN
Option 1: Run from Python (for developers)
1. Install Python (https://python.org)
2. Open Command Prompt and navigate to the project folder:
                 cd C:\FileIntegrityChecker
3.	Run the script:
python file_integrity_gui.py
Make sure you have tkinter installed (usually included by default in standard Python installations).

Option 2: Run the .exe File (No Python Needed)
1.	Go to the dist/ folder.
2.	Double-click on file_integrity_gui.exe.
It will open the GUI instantly, like any Windows app.

Option 3: Run via CMD using .exe
1.	Open Command Prompt.
2.	Navigate to the dist/ folder:
cd C:\FileIntegrityChecker\dist
3.	Run:
file_integrity_gui.exe

AUTO-GENERATED FILES
•	hashes.json: Stores hashes of files from the selected folder.
•	log.txt: Stores logs of integrity check results.
You don’t need to create them manually — they are created when the tool is run.

NOTES
•	Only file contents are checked (not file names).
•	Safe for any file type: .txt, .pdf, .exe, .docx, etc.
•	Does not modify or delete any file — only reads and reports.




DEVELOPER INFO:
Name: Ashirwad Shukla 
Field: Cybersecurity & Software Development
Tool Type: Desktop GUI Application

