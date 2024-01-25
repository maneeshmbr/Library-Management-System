import pymysql

hostname = '127.0.0.1'
username = 'root'
password = 'Bobby12345678'
database = 'library'

myConnection = pymysql.connect( host=hostname, user=username, passwd=password, db=database)

def table_exists(cursor, table_name):
    cursor.execute(f"SHOW TABLES LIKE '{table_name}'")
    return cursor.fetchone() is not None


def createTableBook(conn):
    cur = conn.cursor()
    if not table_exists(cur, 'Book'):
        query = 'CREATE TABLE Book(Isbn VARCHAR(10) NOT NULL, Title VARCHAR(255), Availability INT NOT NULL DEFAULT 1, CONSTRAINT BKPK PRIMARY KEY(Isbn));'
        cur.execute(query)
        print("Created Table Book")

# Function to create the "Authors" table
def createTableAuthors(conn):
    cursor = conn.cursor()
    
    if not table_exists(cursor, 'Authors'):
        create_table_query = '''
            CREATE TABLE Authors (
                Author_id INT NOT NULL AUTO_INCREMENT,
                Name VARCHAR(255) NOT NULL,
                PRIMARY KEY (Author_id)
            );
        '''
        cursor.execute(create_table_query)
        print("Created Table Authors")
    cursor.close()

# Function to create the "Book_Authors" table
def createTableBookAuthors(conn):
    cursor = conn.cursor()
    
    if not table_exists(cursor, 'Book_Authors'):
        create_table_query = '''
            CREATE TABLE Book_Authors (
                Isbn VARCHAR(10) NOT NULL,
                Author_id INT NOT NULL,
                FOREIGN KEY (Author_id) REFERENCES Authors (Author_id) ON DELETE CASCADE,
                PRIMARY KEY (Isbn, Author_id)
            );
        '''
        cursor.execute(create_table_query)
        print("Created Table Book_Authors")
    cursor.close()


def createTableBorrower(conn):
    cur = conn.cursor()
    if not table_exists(cur, 'Borrower'):
        query = 'CREATE TABLE Borrower(Card_id INT NOT NULL AUTO_INCREMENT, Ssn VARCHAR(9) NOT NULL UNIQUE, Bname VARCHAR(255), Address VARCHAR(255), Phone VARCHAR(14), CONSTRAINT BRPK PRIMARY KEY(Card_id));'
        cur.execute(query)
        print("Created Table Borrower")

def createTableBookLoans(conn):
    cur = conn.cursor()
    if not table_exists(cur, 'Book_Loans'):
        query = 'CREATE TABLE Book_Loans(Loan_id INT NOT NULL AUTO_INCREMENT, Isbn VARCHAR(10),Card_id INT, Date_out DATE, Due_date DATE, Date_in DATE, CONSTRAINT BKLPK PRIMARY KEY(Loan_id), CONSTRAINT BKLFK FOREIGN KEY(Isbn) REFERENCES Book(Isbn) ON DELETE SET NULL, CONSTRAINT BKLFKB FOREIGN KEY(Card_id) REFERENCES Borrower(Card_id) ON DELETE SET NULL);'
        cur.execute(query)
        print("Created Table Book Loans")

def createTableFines(conn):
    cur = conn.cursor()
    if not table_exists(cur, 'Fines'):
        query = 'CREATE TABLE Fines(Loan_id INT NOT NULL , Fine_amt DECIMAL(9,2) NOT NULL DEFAULT 0, Paid INT DEFAULT 0, CONSTRAINT FNPK PRIMARY KEY(Loan_id), CONSTRAINT FOREIGN KEY(Loan_id) REFERENCES Book_Loans(Loan_id) ON DELETE CASCADE);'
        cur.execute(query)
        print("Created Table Fines")

cursor = myConnection.cursor()
#cursor.execute("CREATE DATABASE IF NOT EXISTS library;")
#cursor.execute("DROP SCHEMA library;")
#cursor.execute("CREATE SCHEMA library;")
cursor.execute("USE library;")

createTableBook(myConnection)
createTableBookAuthors(myConnection)
createTableAuthors(myConnection)
createTableBorrower(myConnection)
createTableBookLoans(myConnection)
createTableFines(myConnection)
myConnection.close()


