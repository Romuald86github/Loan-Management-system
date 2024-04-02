import psycopg2
import random
import string
from datetime import date, timedelta
import csv

# Connect to the PostgreSQL database
conn = psycopg2.connect(
    host="localhost",
    database="loanee_db",
    user="postgres",
    password="2964"
)

# Create a cursor object
cur = conn.cursor()

# Create the table
with open('create_loanees_table.sql', 'r') as file:
    create_table_query = file.read()

cur.execute(create_table_query)
conn.commit()


# Function to generate random data
def generate_random_data():
    # Generate random values for each column
    name = ''.join(random.choices(string.ascii_letters, k=10))
    age = random.randint(18, 65)
    gender = random.choice(['Male', 'Female'])
    amount_borrowed = round(random.uniform(1000, 100000), 2)
    date_borrowed = str(date.today() - timedelta(days=random.randint(1, 365)))
    loan_term = random.randint(12, 60)
    expected_repayment_date = str(date.today() + timedelta(days=loan_term * 30))
    employment_status = random.choice(['Employed', 'Self-employed', 'Unemployed'])
    income = round(random.uniform(20000, 100000), 2)
    credit_score = random.randint(500, 850)
    loan_purpose = random.choice(['Personal', 'Business', 'Education', 'Home'])
    loan_type = random.choice(['Secured', 'Unsecured'])
    interest_rate = round(random.uniform(0.1, 0.2), 2)
    amount_to_be_repaid = amount_borrowed + (amount_borrowed * interest_rate)
    address = ''.join(random.choices(string.ascii_letters + string.digits, k=20))
    city = ''.join(random.choices(string.ascii_letters, k=10))
    state = ''.join(random.choices(string.ascii_letters, k=2))
    zip_code = ''.join(random.choices(string.digits, k=5))
    country = 'USA'
    email = ''.join(random.choices(string.ascii_letters + string.digits, k=10)) + '@example.com'
    phone_number = ''.join(random.choices(string.digits, k=10))
    marital_status = random.choice(['Single', 'Married', 'Divorced', 'Widowed'])
    dependents = random.randint(0, 5)
    education_level = random.choice(['High School', 'Bachelor', 'Master', 'Doctorate'])
    employer = ''.join(random.choices(string.ascii_letters, k=10))
    job_title = ''.join(random.choices(string.ascii_letters, k=10))
    years_employed = random.randint(0, 20)
    
    # Generate date_repaid
    repaid_status = random.choice([None, 'early', 'late'])
    if repaid_status == 'early':
        days_before = random.randint(1, 30)
        date_repaid = (expected_repayment_date + str(timedelta(days=-days_before)))
    elif repaid_status == 'late':
        days_after = random.randint(1, 30)
        date_repaid = (expected_repayment_date + str(timedelta(days=days_after)))
    else:
        date_repaid = None


    return (name, age, gender, amount_borrowed, date_borrowed, expected_repayment_date, date_repaid, amount_to_be_repaid, employment_status,
            income, credit_score, loan_purpose, loan_type, interest_rate, loan_term, address, city, state, zip_code, country, email, phone_number,
            marital_status, dependents, education_level, employer, job_title, years_employed)

        
# Insert 20,000 initial data rows
for _ in range(20000):
    data = generate_random_data()
    insert_query = """
    INSERT INTO loanee (name, age, gender, amount_borrowed, date_borrowed, expected_repayment_date,
                         date_repaid, amount_to_be_repaid, employment_status, income, credit_score, loan_purpose,
                         loan_type, interest_rate, loan_term, address, city, state, zip_code, country, email, phone_number,
                         marital_status, dependents, education_level, employer, job_title, years_employed)
    VALUES (%s, %s, %s, %s, %s, %s, %s, %s, %s, %s, %s, %s, %s, %s, %s, %s, %s, %s, %s, %s, %s, %s, %s, %s, %s, %s, %s, %s);
    """
    
    # Count the number of placeholders
    num_placeholders = insert_query.count('%s')
    
    # Verify the number of placeholders matches the number of elements in the data tuple
    if num_placeholders != len(data):
        print(f"Error: Number of placeholders ({num_placeholders}) does not match number of data elements ({len(data)}).")
        break
    
    cur.execute(insert_query, data)
    conn.commit()


# Function to add a new loanee
def add_new_loanee():
    # Get user inputs
    name = input("Enter name: ")
    age = int(input("Enter age: "))
    gender = input("Enter gender: ")
    amount_borrowed = float(input("Enter amount borrowed: "))
    date_borrowed = str(date.today())
    loan_term = int(input("Enter loan term (in months): "))
    expected_repayment_date = str(date.today() + timedelta(days=loan_term * 30))
    employment_status = input("Enter employment status: ")
    income = float(input("Enter income: "))
    credit_score = int(input("Enter credit score: "))
    loan_purpose = input("Enter loan purpose: ")
    loan_type = input("Enter loan type: ")
    interest_rate = round(random.uniform(0.1, 0.2), 2)
    amount_to_be_repaid = amount_borrowed + (amount_borrowed * interest_rate)
    address = input("Enter address: ")
    city = input("Enter city: ")
    state = input("Enter state: ")
    zip_code = input("Enter zip code: ")
    country = input("Enter country: ")
    email = input("Enter email: ")
    phone_number = input("Enter phone number: ")
    marital_status = input("Enter marital status: ")
    dependents = int(input("Enter number of dependents: "))
    education_level = input("Enter education level: ")
    employer = input("Enter employer: ")
    job_title = input("Enter job title: ")
    years_employed = int(input("Enter years employed: "))

    # Insert the new loanee into the database
    insert_query = """
    INSERT INTO loanee (name, age, gender, amount_borrowed, date_borrowed, expected_repayment_date,
                         date_repaid, amount_to_be_repaid, employment_status, income, credit_score, loan_purpose,
                         loan_type, interest_rate, loan_term, address, city, state, zip_code, country, email, phone_number,
                         marital_status, dependents, education_level, employer, job_title, years_employed)
    VALUES (%s, %s, %s, %s, %s, %s, %s, %s, %s, %s, %s, %s, %s, %s, %s, %s, %s, %s, %s, %s, %s, %s, %s, %s, %s, %s, %s, %s);
    """
    data = (name, age, gender, amount_borrowed, date_borrowed, expected_repayment_date, None, amount_to_be_repaid, employment_status,
            income, credit_score, loan_purpose, loan_type, interest_rate, loan_term, address, city, state, zip_code, country, email, phone_number,
            marital_status, dependents, education_level, employer, job_title, years_employed)
    cur.execute(insert_query, data)
    conn.commit()
    print('loanee added successfully!')
    
    


    
# Function to update an existing loanee's information
def update_loanee_info():
    # Get the loanee ID from the user
    loanee_id = int(input("Enter the loanee ID: "))

    # Get the new information from the user
    name = input("Enter the new name (or leave blank to keep the same): ") or None
    age = int(input("Enter the new age (or leave blank to keep the same): ")) or None
    gender = input("Enter the new gender (or leave blank to keep the same): ") or None
    amount_borrowed = float(input("Enter the new amount borrowed (or leave blank to keep the same): ")) or None
    employment_status = input("Enter the new employment status (or leave blank to keep the same): ") or None
    income = float(input("Enter the new income (or leave blank to keep the same): ")) or None
    credit_score = int(input("Enter the new credit score (or leave blank to keep the same): ")) or None
    loan_purpose = input("Enter the new loan purpose (or leave blank to keep the same): ") or None
    loan_type = input("Enter the new loan type (or leave blank to keep the same): ") or None
    interest_rate = round(random.uniform(0.1, 0.2), 2)
    address = input("Enter the new address (or leave blank to keep the same): ") or None
    city = input("Enter the new city (or leave blank to keep the same): ") or None
    state = input("Enter the new state (or leave blank to keep the same): ") or None
    zip_code = input("Enter the new zip code (or leave blank to keep the same): ") or None
    country = input("Enter the new country (or leave blank to keep the same): ") or None
    email = input("Enter the new email (or leave blank to keep the same): ") or None
    phone_number = input("Enter the new phone number (or leave blank to keep the same): ") or None
    marital_status = input("Enter the new marital status (or leave blank to keep the same): ") or None
    dependents = int(input("Enter the new number of dependents (or leave blank to keep the same): ")) or None
    education_level = input("Enter the new education level (or leave blank to keep the same): ") or None
    employer = input("Enter the new employer (or leave blank to keep the same): ") or None
    job_title = input("Enter the new job title (or leave blank to keep the same): ") or None
    years_employed = int(input("Enter the new years employed (or leave blank to keep the same): ")) or None

    # Update the loanee's information in the database
    update_query = """
    UPDATE loanee
    SET name = COALESCE(%s, name),
        age = COALESCE(%s, age),
        gender = COALESCE(%s, gender),
        amount_borrowed = COALESCE(%s, amount_borrowed),
        employment_status = COALESCE(%s, employment_status),
        income = COALESCE(%s, income),
        credit_score = COALESCE(%s, credit_score),
        loan_purpose = COALESCE(%s, loan_purpose),
        loan_type = COALESCE(%s, loan_type),
        interest_rate = COALESCE(%s, interest_rate),
        address = COALESCE(%s, address),
        city = COALESCE(%s, city),
        state = COALESCE(%s, state),
        zip_code = COALESCE(%s, zip_code),
        country = COALESCE(%s, country),
        email = COALESCE(%s, email),
        phone_number = COALESCE(%s, phone_number),
        marital_status = COALESCE(%s, marital_status),
        dependents = COALESCE(%s, dependents),
        education_level = COALESCE(%s, education_level),
        employer = COALESCE(%s, employer),
        job_title = COALESCE(%s, job_title),
        years_employed = COALESCE(%s, years_employed)
    WHERE loanee_id = %s;
    """
    data = (name, age, gender, amount_borrowed, employment_status, income, credit_score, loan_purpose,
            loan_type, interest_rate, address, city, state, zip_code, country, email, phone_number,
            marital_status, dependents, education_level, employer, job_title, years_employed, loanee_id)
    cur.execute(update_query, data)
    conn.commit()
    print("Loanee information updated successfully!")
    
    
    
    
    
    

# Function to record a new borrowing for an existing loanee
def record_new_borrowing():
    loanee_id = input("Enter the loanee ID: ")

    # Fetch loanee details
    cur.execute("SELECT * FROM loanee WHERE loanee_id = %s;", (loanee_id,))
    loanee_data = cur.fetchone()

    if not loanee_data:
        print(f"No loanee found with ID {loanee_id}")
        return

    (loanee_id, name, age, gender, amount_borrowed, date_borrowed, expected_repayment_date, amount_to_be_repaid, employment_status, 
     income, credit_score, loan_purpose, loan_type, interest_rate, address, city, state, zip_code, country, email, 
     phone_number, marital_status, dependents, education_level, employer, job_title, years_employed) = loanee_data[:27]

    amount_borrowed = float(input("Enter the amount borrowed: "))
    loan_term = int(input("Enter the loan term (in months): "))
    loan_purpose = input("Enter the loan purpose: ")
    loan_type = input("Enter the loan type: ")

    # Calculate expected repayment date
    date_borrowed = str(date.today())
    expected_repayment_date = str(date.today() + timedelta(days=loan_term * 30))

    # Calculate amount to be repaid (including interest)
    interest_rate = round(random.uniform(0.1, 0.2), 2)
    amount_to_be_repaid = amount_borrowed + (amount_borrowed * interest_rate)

    # Insert the new borrowing record into the database
    insert_query = """
    INSERT INTO loanee (name, age, gender, amount_borrowed, date_borrowed, expected_repayment_date, amount_to_be_repaid, employment_status, income, credit_score,
                        loan_purpose, loan_type, interest_rate, address, city, state, zip_code, country, email, phone_number, marital_status, dependents,
                        education_level, employer, job_title, years_employed, loanee_id)
    VALUES (%s, %s, %s, %s, %s, %s, %s, %s, %s, %s, %s, %s, %s, %s, %s, %s, %s, %s, %s, %s, %s, %s, %s, %s, %s, %s, %s);
    """

    data = (name, age, gender, amount_borrowed, date_borrowed, expected_repayment_date, amount_to_be_repaid, employment_status, income, credit_score,
            loan_purpose, loan_type, interest_rate, address, city, state, zip_code, country, email, phone_number, marital_status, dependents,
            education_level, employer, job_title, years_employed, loanee_id)
    
    cur.execute(insert_query, data)
    conn.commit()

    print("New borrowing recorded successfully!")
    export_to_csv()


    
    
    
    
    
    
    
# Function to update the repayment status of an existing loanee
def update_repayment_status():
    # Get the loanee ID from the user
    loanee_id = int(input("Enter the loanee ID: "))

    # Get the repayment date from the user
    date_repaid = input("Enter the repayment date (YYYY-MM-DD) or leave blank if not yet repaid: ") or None

    # Update the repayment status in the database
    update_query = """
    UPDATE loanee
    SET date_repaid = %s
    WHERE loanee_id = %s;
    """
    data = (date_repaid, loanee_id)
    cur.execute(update_query, data)
    conn.commit()
    print("repayment status updated successfully!")
    
    
    
    
    
    
 
# Function to export data to CSV
def export_to_csv():
    # Fetch all rows from the database
    select_query = "SELECT * FROM loanee;"
    cur.execute(select_query)
    rows = cur.fetchall()

    # Write the rows to a CSV file
    with open("loanee.csv", "w", newline="") as csvfile:
        writer = csv.writer(csvfile)
        writer.writerow([desc[0] for desc in cur.description])  # Write the column names
        writer.writerows(rows)

    print("Data exported to loanee.csv")
    
    
    
    
    

    
# Main application loop
while True:
    print("\nLoanee Management System")
    print("1. Add a new loanee")
    print("2. Update an existing loanee's information")
    print("3. Record a new borrowing for an existing loanee")
    print("4. Update the repayment status of an existing loanee")
    print("5. Export data to CSV")
    print("6. Exit")

    choice = input("Enter your choice (1-6): ")

    if choice == "1":
        add_new_loanee()
    elif choice == "2":
        update_loanee_info()
    elif choice == "3":
        record_new_borrowing()
    elif choice == "4":
        update_repayment_status()
    elif choice == "5":
        export_to_csv()
    elif choice == "6":
        break
    else:
        print("Invalid choice. Please try again.")

# Close the database connection
cur.close()
conn.close()

    




