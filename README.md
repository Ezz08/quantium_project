# 📦 Python Project Setup (Git + Virtual Environment + Dash)

# 1️⃣ Clone the repository
git clone <repo-url>
cd <repo-name>

# 2️⃣ Create virtual environment
python -m venv venv

# 3️⃣ Activate virtual environment (Windows PowerShell)
.\venv\Scripts\Activate.ps1

# OR (Windows CMD)
# venv\Scripts\activate

# OR (Mac/Linux)
# source venv/bin/activate

# 4️⃣ Install dependencies
pip install dash pandas

# Install Dash testing dependencies
pip install "dash[testing]"

# 5️⃣ Save dependencies (optional but recommended)
pip freeze > requirements.txt

# 🧩 Why Virtual Environment?
# - Isolates project dependencies
# - Prevents version conflicts between projects
# - Keeps system Python clean
# - Makes projects reproducible on other machines

# 📁 Git Best Practice
# ❌ Do NOT upload venv/ to GitHub
# ✔ Upload only:
# - source code
# - requirements.txt
# - project files

# 🎯 Final Workflow
# git clone <repo>
# cd <repo>
# python -m venv venv
# activate venv
# pip install -r requirements.txt
