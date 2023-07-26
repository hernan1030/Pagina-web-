import sqlite3


def extraer_datos():
    ruta = "C://Users/hernan garcia serran//OneDrive//Escritorio//curso_django/webpersonal//db.sqlite3"
    conn = sqlite3.connect(ruta)
    cursor = conn.cursor()
    cursor.execute("SELECT * FROM portfolio_project")

    data = cursor.fetchall()
    conn.commit()

    print(data)


if __name__ == "__main__":

    extraer_datos()
