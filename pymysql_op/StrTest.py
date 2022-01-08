import pymysql

if __name__ == '__main__':
    db = pymysql.connect("localhost", "root", "Aa123123...", "test")

    cursor = db.cursor()

    try:
        cursor.execute("SELECT u.* FROM test_u u")

        data = cursor.fetchone()

        print("VERSION is : %s" % data)

    except:
        print("read record error!")

    db.close()
