import sqlite3
from http.server import HTTPServer
from http.server import CGIHTTPRequestHandler
import os.path
from lxml import etree, objectify


def parse_book_xml(xml_file):
    with open(xml_file) as fobj:
        xml = fobj.read()

    root = etree.fromstring(xml)

    books = []
    for book in root.getchildren():
        one_book = []
        for elem in book.getchildren():
            if not elem.text:
                one_book.append("None")
            else:
                one_book.append(elem.text)
        books.append(one_book)

    return [tuple(i) for i in books]


def create_appt(data):  # Создаем изначальную структуру XML

    appt = objectify.Element("author")
    appt.id_aut = data["id_aut"]
    appt.last_name = data["last_name"]
    appt.first_name = data["first_name"]
    appt.father_name = data["father_name"]
    appt.pseudonym = data["pseudonym"]
    appt.date_birth = data["date_birth"]
    return appt


def create_xml():  # Создаем XML файл

    xml = '''<?xml version="1.0"?>
    <author_table>
    </author_table>
    '''

    root = objectify.fromstring(xml)

    appt = create_appt({"id_aut": "1",
                        "last_name": "Peshkov",
                        "first_name": "Aleksey",
                        "father_name": "Maksimovich",
                        "pseudonym": "Maksim Gorkiy",
                        "date_birth": "28-03-1868"}
                       )
    root.append(appt)

    appt = create_appt({"id_aut": "2",
                        "last_name": "Poetov",
                        "first_name": "Poet",
                        "father_name": "Poetovich",
                        "pseudonym": "Poet",
                        "date_birth": "01-01-2001"}
                       )
    root.append(appt)

    # удаляем все lxml аннотации.
    objectify.deannotate(root)
    etree.cleanup_namespaces(root)

    # конвертируем все в привычную нам xml структуру.
    obj_xml = etree.tostring(root, pretty_print=True, xml_declaration=True)

    try:
        with open("base_in.xml", "wb") as xml_writer:
            xml_writer.write(obj_xml)
        print("О Палмолив мой нежный гель!")
    except IOError:
        print("Мне плоха!")
        pass


if not os.path.isfile('example.db'):
    con = sqlite3.connect('example.db')
    cur = con.cursor()

    cur.execute('''CREATE TABLE author
            (id_aut INTEGER PRIMARY KEY AUTOINCREMENT,
            last_name TEXT,
            first_name TEXT,
            father_name TEXT,
            pseudonym TEXT,
            date_birth TEXT)''')

    cur.execute('''CREATE TABLE publisher
            (id_pub INTEGER PRIMARY KEY AUTOINCREMENT,
            name VARCHAR(30),
            address VARCHAR(50),
            foundation TEXT)''')

    cur.execute('''CREATE TABLE book
            (id_book INTEGER PRIMARY KEY AUTOINCREMENT,
            name VARCHAR(50),
            id_aut INTEGER,
            genre VARCHAR(15),
            id_pub INTEGER,
            publication TEXT,
            FOREIGN KEY (id_aut) REFERENCES author(id_aut),
            FOREIGN KEY (id_pub) REFERENCES publisher(id_pub))''')

    authors = [(1, 'Peshkov', 'Aleksey', 'Maksimovich', 'Maksim Gorkiy', '28-03-1868'),
           (2, 'Poetov', 'Poet', 'Poetovich', 'Poet', '01-01-2001'),
           (3, 'Ivanov', 'Petr', 'Sidorovich', 'Petr Ivanov', '11-12-2013')]

    sql1 = '''INSERT INTO author(id_aut,last_name,first_name,father_name,pseudonym,date_birth) VALUES(?,?,?,?,?,?)'''
    con.executemany(sql1, authors)

    publishers = [(1, 'Sharashkina Kontora', 'Moscow', '1812'),
              (2, 'Big Brother', 'London', '1984'),
              (3, 'Zarya', 'Moscow', '1996')]

    sql1 = '''INSERT INTO publisher(id_pub,name,address,foundation) VALUES(?,?,?,?)'''
    con.executemany(sql1, publishers)

    books = [(1, 'Sdelai Sam', 3, 'Horror', 1, '32-13-0'),
         (2, 'Sbornik Sochinenii', 1, 'Thriller', 3, '15-01-1920'),
         (3, 'Python for the young and the dumb', 2, 'Love Story', 2, '28-10-2021')]

    sql1 = '''INSERT INTO book(id_book,name,id_aut,genre,id_pub,publication) VALUES(?,?,?,?,?,?)'''
    con.executemany(sql1, books)

    xml_books = parse_book_xml("base_out.xml")  #
    con.executemany(sql1, xml_books)  #

    con.commit()

create_xml()  #

server_address = ("localhost", 8000)
http_server = HTTPServer(server_address, CGIHTTPRequestHandler)
http_server.serve_forever()

#cur.execute('SELECT * FROM book')
#print(cur.fetchall())
