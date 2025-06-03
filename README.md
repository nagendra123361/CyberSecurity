# CyberSecurity

## 🛡 Phishing Email Detector

This Python script is a simple terminal-based **Phishing Email Detector** that analyzes raw email content to flag potentially malicious messages. It uses a predefined list of common phishing keywords and scans for suspicious URLs to help users identify fraudulent emails.

### 🔍 Features

* **Keyword Detection**: Scans email content for phrases often used in phishing attacks (e.g., *"verify your account"*, *"click here"*, *"urgent action required"*, etc.).
* **Suspicious Link Detection**: Extracts and lists any URLs present in the email that may be phishing traps.
* **Case-insensitive Search**: Detects keywords regardless of how they are capitalized.
* **User Input Support**: Accepts multiline email input directly in the terminal.

### 🚀 How It Works

1. The script prompts the user to paste the content of an email.
2. It converts the email to lowercase for uniform analysis.
3. It searches for known phishing keywords and URLs.
4. If any suspicious indicators are found, it warns the user and displays them.

### ✅ Sample Output

```
⚠  Potential Phishing Detected!

Suspicious Phrases Found:
  • verify your account
  • urgent action required

Suspicious Links Found:
  • http://malicious-site.com/verify
```

### ▶ How to Run

Make sure you have Python installed (preferably 3.x), then run:

```bash
python phishing_detector.py
```

Paste your email content when prompted, and press Enter twice to analyze.
