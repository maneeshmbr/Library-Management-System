import pandas as pd
import pymysql

hostname = '127.0.0.1'
username = 'root'
password = 'Bobby12345678'
database = 'library'

myConnection = pymysql.connect(host=hostname, user=username, passwd=password, db=database)
cur = myConnection.cursor()

cur.execute("DELETE FROM Book;")
cur.execute("DELETE FROM Book_Authors;")
cur.execute("DELETE FROM Authors;")
cur.execute("DELETE FROM Borrower;")
cur.execute("DELETE FROM Book_Loans;")
cur.execute("DELETE FROM Fines;")

cur.execute("ALTER TABLE Book_Authors AUTO_INCREMENT = 1;")
cur.execute("ALTER TABLE Authors AUTO_INCREMENT = 1;")
cur.execute("ALTER TABLE Borrower AUTO_INCREMENT = 1;")
cur.execute("ALTER TABLE Book_Loans AUTO_INCREMENT = 1;")
cur.execute("ALTER TABLE Fines AUTO_INCREMENT = 1;")

books = pd.read_csv('book.csv')
borrowers = pd.read_csv('borrower.csv')

def insertIntoBook(conn, data):
    cur = conn.cursor()
    # Disable foreign key checks
    cur.execute("SET FOREIGN_KEY_CHECKS = 0;")
    for index, row in data.iterrows():
        isbn10 = row['ISBN10']
        title = row['Title'].replace('"', '')
        author_data = row['Author']
        if isinstance(author_data, str):
           authors = [author.strip() for author in author_data.split(',')]
        else:
           authors = []
        availability = 1
        query = 'INSERT INTO Book (Isbn, Title, Availability) VALUES(%s, %s, %s);'
        cur.execute(query, (isbn10, title, availability))
        book_id = cur.lastrowid  

        for author in authors:
         cur.execute("SELECT Author_id FROM Authors WHERE Name = %s;", (author,))
         author_row = cur.fetchone()
         if author_row:
             author_id = author_row[0]
        else:
         cur.execute('INSERT INTO Authors (Name) VALUES (%s);', (author,))
         author_id = cur.lastrowid  

        if author_id and isbn10:
            cur.execute('SELECT COUNT(*) FROM Book_Authors WHERE Author_id = %s AND Isbn = %s;', (author_id, isbn10))
            record_count = cur.fetchone()[0]
            if record_count == 0:
             cur.execute('INSERT INTO Book_Authors (Author_id, Isbn) VALUES (%s, %s);', (author_id, isbn10))



def insertIntoBorrower(conn, data):
    cur = conn.cursor()
    for index, row in data.iterrows():
        ssn = str(row['ID0000id'])
        bname = row['first_name'] + ' ' + row['last_name']
        address = row['address'] + ', ' + row['city'] + ', ' + row['state']
        phone = row['phone']
        query = 'INSERT INTO Borrower (Ssn, Bname, Address, Phone) VALUES(%s, %s, %s, %s);'
        cur.execute(query, (ssn, bname, address, phone))

try:
    insertIntoBook(myConnection, books)
    insertIntoBorrower(myConnection, borrowers)
    myConnection.commit()
    print("Data inserted successfully.")
except Exception as e:
    print("Error:", str(e))
    myConnection.rollback()
finally:
    myConnection.close()


