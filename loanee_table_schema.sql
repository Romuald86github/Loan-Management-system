CREATE TABLE IF NOT EXISTS loanee (
    loanee_id SERIAL PRIMARY KEY,
    name TEXT NOT NULL,
    age INTEGER NOT NULL,
    gender TEXT NOT NULL,
    amount_borrowed REAL NOT NULL,
    date_borrowed TEXT NOT NULL,
    expected_repayment_date TEXT NOT NULL,
    date_repaid TEXT,
    amount_to_be_repaid REAL NOT NULL,
    employment_status TEXT NOT NULL,
    income REAL NOT NULL,
    credit_score INTEGER NOT NULL,
    loan_purpose TEXT NOT NULL,
    loan_type TEXT NOT NULL,
    interest_rate REAL NOT NULL,
    loan_term INTEGER NOT NULL,
    address TEXT NOT NULL,
    city TEXT NOT NULL,
    state TEXT NOT NULL,
    zip_code TEXT NOT NULL,
    country TEXT NOT NULL,
    email TEXT NOT NULL,
    phone_number TEXT NOT NULL,
    marital_status TEXT NOT NULL,
    dependents INTEGER NOT NULL,
    education_level TEXT NOT NULL,
    employer TEXT,
    job_title TEXT,
    years_employed INTEGER
);
