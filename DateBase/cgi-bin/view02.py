import cgi
import sqlite3


def html_bd():
    sql1 = '''INSERT INTO author(id_aut,last_name,first_name,father_name,pseudonym,date_birth) VALUES(?,?,?,?,?,?)'''
    sql2 = (int(text_id), text_ln, text_fn, text_fath, text_pseud, text_date)
    con.execute(sql1, sql2)

    con.commit()


form = cgi.FieldStorage()


con = sqlite3.connect('example.db')
cur = con.cursor()

text_id = form.getfirst("id_aut", "0")
text_ln = form.getfirst("last_name", "Не задано")
text_fn = form.getfirst("first_name", "Не задано")
text_fath = form.getfirst("father_name", "Не задано")
text_pseud = form.getfirst("pseudonym", "Не задано")
text_date = form.getfirst("date_birth", "Не задано")

html_bd()

print("Content-type: text/html\n")
print("""<!DOCTYPE HTML>
    <html>
    <head>
        <meta charset="utf-8">
        <title>Обработка авторов </title>
    </head>
    <body>""")
print("<h1>Обработка авторов</h1>")
print("<p>Id: %s</p>" % text_id)
print("<p>Фамилия: %s</p>" % text_ln)
print("<p>Имя: %s</p>" % text_fn)
print("<p>Отчество: %s</p>" % text_fath)
print("<p>Псевдоним: %s</p>" % text_pseud)
print("<p>Дата рождения: %s</p>" % text_date)
print("""</body> </html>""")
