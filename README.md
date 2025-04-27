# Project Setup Instructions

This guide provides the steps to set up and run the project locally.

---

## Prerequisites

- Python 3.x installed
- `pip` package manager

---

## Setup Steps

### 1. Create a Virtual Environment

Create a virtual environment named `.venv` to isolate project dependencies:

```bash
python -m venv .venv
```

---

### 2. Activate the Virtual Environment

Activate the virtual environment to use its isolated Python environment:

- **On Windows:**

```bash
.venv\Scripts\activate
```

- **On macOS/Linux:**

```bash
source .venv/bin/activate
```

---

### 3. Install Required Libraries

Install the project dependencies listed in the `requirements.txt` file:

```bash
pip install -r requirements.txt
```

---

### 4. Create a `.env` File

In the same working directory, create a `.env` file and add the following line.  
Replace `<25 phrase Mnemonic>` with your 25-word mnemonic phrase:

```env
DEPLOYER=<25 phrase Mnemonic>
```

---

### 5. Run the Main Script

Execute the main Python script to start the application:

```bash
python main.py
```

---

## 🎯 You're all set!

Happy coding!
