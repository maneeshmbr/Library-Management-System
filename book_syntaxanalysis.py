file_path = 'C:\\Users\\manee\\Desktop\\DB_Design\\Library-Management-System-master\\book.csv'

with open(file_path, 'r', encoding="utf-8") as fileObj:
    text_file = list(fileObj)

author_id = 0
author_list = []

for line in text_file[1:21]:
    print('-' * 50)
    line = line.strip()
    column_list = line.split('\t')
    
    isbn13, title, authors = column_list[1], column_list[2], column_list[3]
    
    print(f"INSERT INTO Books VALUES (\"{isbn13}\",\"{title}\");")
    
    authors = authors.split(',')
    
    for author in authors:
        author_id += 1
        if author in author_list:
            print(f"{author} already exists")
        else:
            author_list.append(author)
            print(f"INSERT INTO Authors VALUES (\"{author_id}\",\"{author}\");")
        
        print(f"INSERT INTO Book_authors VALUES (\"{author_id}\",\"{isbn13}\");")

print('=' * 50)
print(author_list)
