📜 Mail Merge Certificate Agent

Automated Certificate Generation using Google ADK + Python

The Mail Merge Certificate Agent is an AI-powered automation project that generates personalized certificates from a DOCX template and student details stored in an Excel file.

Instead of manually editing each certificate, the agent validates the student data and automatically creates an individual certificate for every student.

✨ What Does It Do?

📊 Student_Data.xlsx
        │
        ▼
🔍 Validate Student Data
        │
        ▼
📄 certificate.docx
        │
        ▼
🔄 Replace Placeholders
        │
        ▼
📁 Generated Certificates


The agent can:

* ✅ Validate the Excel file
* ✅ Check required columns
* ✅ Check for missing student information
* ✅ Generate personalized certificates
* ✅ Replace placeholders automatically
* ✅ Keep the original certificate unchanged
* ✅ Save generated certificates in the `output` folder

 🛠️ Technologies

| Technology    | Purpose              |
| ------------- | -------------------- |
| 🐍 Python     | Core implementation  |
| 🤖 Google ADK | AI agent framework   |
| ✨ Gemini      | Agent model          |
| 📊 Pandas     | Excel processing     |
| 📄 DOCX       | Certificate template |
| 📑 Excel      | Student data         |



 📌 Version 1

This repository contains Version 1 of the Mail Merge Certificate Agent.

Version 1 uses a predefined certificate template and a predefined Excel structure.

📄 Default Files


certificate.docx
Student_Data.xlsx


📊 Required Excel Columns


Student Name
Roll No
Coordinator
HOD


 🏷️ Certificate Placeholders

The certificate template uses:


{{STUDENT_NAME}}
{{ROLL_NO}}
{{COORDINATOR}}
{{HOD}}
```

The agent replaces these placeholders with the corresponding student information.



 📊 Sample Student Data

The current `Student_Data.xlsx` contains:

| Student Name  | Roll No  | Coordinator      | HOD             |
| ------------- | -------- | ---------------- | --------------- |
| Ananya Reddy  | 23CSE001 | Dr. Rajesh Kumar | Dr. Suresh Babu |
| Vikram Sharma | 23CSE002 | Dr. Rajesh Kumar | Dr. Suresh Babu |
| Sneha Patel   | 23CSE003 | Dr. Rajesh Kumar | Dr. Suresh Babu |
| Arjun Verma   | 23CSE004 | Dr. Rajesh Kumar | Dr. Suresh Babu |
| Kavya Nair    | 23CSE005 | Dr. Rajesh Kumar | Dr. Suresh Babu |

➡️ 5 student records → 5 personalized certificates



# 📂 Project Structure


mail_merge_agent/
│
├── 📄 .env
├── 📄 .env.example
├── 📄 .gitignore
├── 📄 requirements.txt
│
├── 📄 certificate.docx
├── 📊 Student_Data.xlsx
│
├── 📁 mail_merge_agent/
│   ├── 📄 __init__.py
│   ├── 🤖 agent.py
│   └── 🔧 tools.py
│
└── 📁 output/
    └── Generated certificates




 ⚙️ How It Works

1️⃣ Excel Validation

The agent first checks the Excel file.

It verifies:


✔ File exists
✔ Required columns exist
✔ Student records exist
✔ Required fields are filled


If validation fails, certificate generation stops.


 2️⃣ Read Student Information

For each student, the agent reads:


Student Name
Roll No
Coordinator
HOD

 3️⃣ Replace Certificate Placeholders

For example:


{{STUDENT_NAME}}


becomes:


Ananya Reddy

and:


{{ROLL_NO}}


becomes:


23CSE001


The same process is performed for the Coordinator and HOD.

4️⃣ Generate Certificates

A separate DOCX file is created for every student.

Example:


Ananya Reddy_23CSE001.docx
Vikram Sharma_23CSE002.docx
Sneha Patel_23CSE003.docx
Arjun Verma_23CSE004.docx
Kavya Nair_23CSE005.docx


All generated files are stored inside:


output/


# 🚀 Installation & Setup

## Step 1 — Open the Project


cd C:\Users\arema\Downloads\mail_merge_agent


## Step 2 — Create Virtual Environment


python -m venv .venv


## Step 3 — Activate Virtual Environment


.venv\Scripts\Activate


You should see:


(.venv)


at the beginning of your command prompt.

## Step 4 — Install Dependencies


pip install -r requirements.txt

# ▶️ Run the Agent

The Mail Merge Certificate Agent can be run and interacted with through the Google ADK Dev UI.

## Step 1 — Start the Google ADK Interface

Make sure your virtual environment is activated:


.venv\Scripts\Activate


Then start the ADK web interface:


adk web mail_merge_agent


The terminal will start the local ADK server.

## Step 2 — Open the Dev UI

Open the following URL in your browser:

http://127.0.0.1:8000/dev-ui


The ADK Dev UI provides an interactive interface for communicating with the Mail Merge Certificate Agent.

## Step 3 — Select the Agent

In the Dev UI, select:

mail_merge_certificate_agent


## Step 4 — Request Certificate Generation

Enter a request such as:

> Generate certificates for all students in the Excel file.

The agent will then perform the complete workflow:


💬 User Request
      │
      ▼
🤖 ADK Agent
      │
      ▼
🔍 Validate Student_Data.xlsx
      │
      ▼
📄 Read certificate.docx
      │
      ▼
🔄 Replace Placeholders
      │
      ▼
📁 Generate Certificates
      │
      ▼
✅ Save files in output/

## Step 5 — Check the Generated Certificates

After successful execution, the generated certificates will be available inside:


output/


For the sample Excel file, 5 certificates will be generated.

### 🌐 ADK Dev UI

The complete interactive workflow is performed through:


http://127.0.0.1:8000/dev-ui

This allows the user to communicate with the agent and trigger the certificate-generation process without directly calling the Python functions.


 🧪 Direct Testing

The certificate-generation tool can also be tested directly without opening the ADK interface.

Run:


python -c "from mail_merge_agent.tools import generate_certificates; print(generate_certificates())"


A successful execution will display:


Successfully generated 5 certificates:


The generated files will be available in:

output/


# 🔒 Data Validation

The agent does not generate certificates if required information is missing.

For example, if a student does not have a Roll No:


Validation failed.

Student Name (No Roll No) -> Roll No

No certificates should be generated.


This ensures that incomplete student data does not result in incomplete certificates.


# 🧩 Agent Components

`agent.py`

Defines the Google ADK agent:


mail_merge_certificate_agent


It provides the agent instructions and connects the certificate-generation tools.

### `tools.py`

Contains the certificate-processing functions:


validate_excel_file()
generate_certificates()


The actual validation and certificate generation logic is implemented here.



# 📦 Output

After successful execution:


output/
│
├── Ananya Reddy_23CSE001.docx
├── Vikram Sharma_23CSE002.docx
├── Sneha Patel_23CSE003.docx
├── Arjun Verma_23CSE004.docx
└── Kavya Nair_23CSE005.docx


The original:

certificate.docx


remains unchanged.



# 🔄 Version 2

A more generic implementation of the Mail Merge Agent is available in a separate repository.

### Version 2 Repository


mail_merge_agent_v2


Version 2 is maintained separately from this Version 1 repository.


## 👩‍💻 Project

Mail Merge Certificate Agent — Version 1

Built with:

Python + Google ADK + Gemini + Pandas + DOCX

Automating repetitive certificate generation with an AI-powered workflow.
