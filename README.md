KMBR Architecture Compliance Tool
This is a lightweight web-based tool designed to assist architecture students, professionals, and institutions in quickly referencing compliance rules from the Kerala Municipality Building Rules (KMBR) and National Building Code (NBC). The tool fetches rules dynamically based on building type and helps ensure alignment with government-specified standards.

🚀 Features
Fetch KMBR/NBC building regulations based on building type

Dynamic calculators: FSI, Setback, Coverage, Toilets, Parking, etc.

Compliance assistant for validating rule adherence

JSON-based data store for easy updates and portability

Built with Python Flask, HTML/CSS, and Bootstrap

🗂️ Project Structure
project-folder/
│
├── app.py                  # Flask backend logic
├── templates/              # HTML templates
├── static/                 # CSS, images, etc.
├── kmbr_full_dataset.json  # Main data file (KMBR rules)
├── calculators/            # FSI, setback, coverage calculators
└── README.md               # You're here


🛠️ Tech Stack
Python 3.x
Flask
HTML5 + CSS3 (Bootstrap)
JSON (for rule storage)

🧪 How to Run
Clone this repository:
git clone https://github.com/your-username/kmbr-compliance-tool.git
cd kmbr-compliance-tool
Install requirements:
nginx
pip install flask
Run the app:
python app.py

Open your browser and go to:
http://127.0.0.1:5000

💡 Future Improvements
AI-based compliance suggestion system

User login and saved project capability

Rule comparisons between NBC and state-specific rules

Mobile UI and PWA support

📄 License
MIT License

🙋‍♂️ About the Developer
B.E. CSE (Cybersecurity) student passionate about penetration testing, cloud computing, and AI-driven automation.
Actively working on real-world security projects and architecture compliance systems using Flask, GCP, and Python.
Let’s connect on LinkedIn or explore more at GitHub.
