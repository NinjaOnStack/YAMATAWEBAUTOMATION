# ✅ YamataAppAutomation - Python Playwright Test Framework

This project is a Python-based test automation framework using [Playwright](https://playwright.dev/python/) and `pytest`

---

## 📁 Project Structure

```
CXCAppAutomation_Python/
├── pages/              # Page Object Model (POM) files
├── tests/              # All test cases
├── test_data/          # Config and test data helpers
├── reports/            # Generated test reports (optional)
├── requirements.txt    # Python dependencies
├── pytest.ini          # Pytest config
├── README.md           # Setup instructions (this file)
└── conftest.py         # Shared fixtures and setup
```

---

## ✅ Setup Instructions

### 1. Install Required Tools

#### 🐍 Install Python
Download and install Python 3.11+  
🔗 [https://www.python.org/downloads/](https://www.python.org/downloads/)

**During install:**
✅ Enable **"Add Python to PATH"**

---

#### 💻 Install Visual Studio Code
Download and install VS Code  
🔗 [https://code.visualstudio.com/](https://code.visualstudio.com/)

---

### 2. Setup Python in VS Code

Open VS Code and install these extensions from the Extensions tab (`Ctrl+Shift+X`):

- ✅ **Python** (by Microsoft)
- ✅ **Pylance**
- ✅ (Optional) **Pytest** – for test discovery in VS Code

---

### 3. Open the Project

1. In VS Code: `File → Open Folder... →` select the cloned project folder

---

### 4. Create and Activate a Virtual Environment

In the VS Code terminal (`Ctrl + ~`):

```bash
# Create a virtual environment
python -m venv venv

# Activate it
# Windows:
venv\Scripts\activate

# macOS/Linux:
source venv/bin/activate
```

---

### 5. Install Dependencies

```bash
pip install -r requirements.txt
playwright install
```

This installs:

- Playwright
- Pytest
- All necessary plugins
- Required browser binaries

---

### 6. Run Tests

```bash
pytest
```

---

## 📊 Optional: Generate Test Reports

### HTML Report (Simple)

```bash
pip install pytest-html
pytest --html=reports/report.html --self-contained-html
```

### Allure Report (Advanced)

```bash
pip install allure-pytest
pytest --alluredir=allure-results
allure serve allure-results
```

(Install [Allure CLI](https://docs.qameta.io/allure/#_installing_a_commandline) separately)

---

## 🧪 Notes

- The browser will launch in **non-headless** mode for debugging
- You can find and update selectors in the `pages/` folder
- Login credentials and base URL are stored in `utils/test_data.json` and `utils/config.json`

---