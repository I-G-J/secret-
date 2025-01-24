# Message Coder & Decoder

This project is a Python-based GUI application that allows users to **encode** and **decode messages** using a simple yet secure logic. The interface is built using the `tkinter` library, providing an intuitive and interactive user experience.

---

## Features
- **Encode Messages**:
  - For messages with more than 3 characters:
    - The message is reversed.
    - Three random characters are added to the beginning and end.
  - For messages with 3 or fewer characters:
    - The first character is moved to the end, and the string is reversed.

- **Decode Messages**:
  - For messages with more than 3 characters:
    - The first 3 and last 3 characters are removed, and the string is reversed.
  - For messages with 3 or fewer characters:
    - The string is reversed, and the last character is moved to the front.

- **Copy to Clipboard**:
  - Encoded and decoded messages can be copied directly to the clipboard.

- **User-Friendly GUI**:
  - The application features a clean and responsive interface with buttons for encoding, decoding, and exiting.

---

## Getting Started

### Prerequisites
- Python 3.x installed on your system.
- Required library:
  - `tkinter` (pre-installed with Python).

---

### How to Run the Program
1. Clone this repository:
   ```bash
 
