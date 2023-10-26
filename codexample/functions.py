
def return_value(value):
    return value

def raise_error(msg_kw):
    raise ValueError(f"Exception {msg_kw} raised")

def factorielle(n):
    if n == 0:
        return 1
    else:
        return n  * factorielle(n-1)

def consulta():
    import mysql.connector

    cnx = mysql.connector.connect(user='scott', database='employees')
    cursor = cnx.cursor()

    query = ("SELECT nombreFROM liga where puesto=3")
    data = cursor.execute(query)
    print(data)
     

    cursor.close()
    cnx.close()
    return print(data)