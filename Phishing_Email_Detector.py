import re

# Predefined suspicious phishing keywords and phrases
phishing_keywords = [
    "verify your account", "login urgently", "update your information",
    "you have won", "click here", "act now", "suspend your account",
    "unauthorized login", "confirm password", "bank account", "urgent action required",
    "limited time", "confirm your identity", "reset your password"
]

def detect_phishing(email_text):
    email_text = email_text.lower()
    suspicious_found = []

    # Keyword matching
    for keyword in phishing_keywords:
        if keyword in email_text:
            suspicious_found.append(keyword)

    # Extracting suspicious URLs
    suspicious_links = re.findall(r'http[s]?://\S+', email_text)

    # Display results
    if suspicious_found or suspicious_links:
        print("\n⚠  Potential Phishing Detected!\n")
        if suspicious_found:
            print("Suspicious Phrases Found:")
            for phrase in suspicious_found:
                print(f"  • {phrase}")
        if suspicious_links:
            print("\nSuspicious Links Found:")
            for link in suspicious_links:
                print(f"  • {link}")
    else:
        print("\n✅ Email appears safe (no obvious phishing indicators found).")

# ---- Main Program ----
if _name_ == "_main_":
    print("=== 🛡 Phishing Email Detector ===")
    print("Paste the email content below (press Enter twice to finish):\n")

    # Multiline input collection
    lines = []
    while True:
        line = input()
        if line.strip() == "":
            break
        lines.append(line)

    email_content = "\n".join(lines)
    detect_phishing(email_content)
