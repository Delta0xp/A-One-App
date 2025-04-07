---

# A One Public Welfare Foundation – Community Health Center App

## Overview
The **A One Public Welfare Foundation** is a non-profit organization based in Edenvale, South Africa, with the goal of providing accessible, affordable healthcare services to underserved communities. The Foundation operates a Community Health Center offering general medical consultations, basic medications, and preventative care.

## Features of the App:
- **Medicine Stock Management:** Track stock in/out, expiry dates, and supplier details.
- **Doctor & Prescription Records:** Maintain patient history, prescriptions, and treatment details.
- **Finance & Accounts:** Manage income, expenses, donations, invoices, and generate reports.
- **Membership & Donor Management:** Keep records of donors and permanent members.
- **Banking & Payments:** Integration with bank systems for donations and expense tracking.
- **Social Media & Website Integration:** Connect with Facebook, Instagram, TikTok, and X.
- **User Access Control:** Set access levels for doctors, accountants, and members.
- **Mobile & Web-based App:** Accessible on both mobile (React Native) and web (React).

## Technology Stack:
- **Frontend:** React Native
- **Backend:** FastAPI
- **Database:** SQLite3
- **Authentication:** JWT Tokens
- **Deployment:** Docker, Heroku, or AWS

## Installation

Clone this repository:

```bash
git clone https://github.com/username/aone-health-center.git
cd aone-health-center
```

Create a virtual environment and install dependencies:

```bash
python -m venv venv
source venv/bin/activate  # On Windows: venv\Scripts\activate
pip install -r requirements.txt
```

### Running the Backend (FastAPI)
To run the FastAPI backend:

```bash
uvicorn main:app --reload
```

### Running the Frontend (React Native)
Navigate to the frontend folder and install dependencies:

```bash
cd frontend
npm install
```

Run the app in development mode:

```bash
npm start
```

To run the app on a device or simulator, follow the instructions in the [React Native documentation](https://reactnative.dev/docs/environment-setup).

## Database Setup
The database schema is pre-configured in SQLite3. Ensure the database is populated with initial data by running:

```bash
python manage.py migrate
python manage.py loaddata initial_data.json
```

## Conclusion
The **A One Public Welfare Foundation Community Health Center** app aims to streamline operations for medical staff, donors, and administrators, enabling better service delivery and financial transparency.

---

