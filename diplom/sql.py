import mysql.connector as mysql
import time


class SQL:
    def verify_order(self):
        db = mysql.connect(host="localhost",
                           user="root",
                           passwd="",
                           database="litecart")

        cursor = db.cursor()
        query = "SELECT order_status_id FROM lc_orders WHERE customer_id = 2"
        time.sleep(2)
        cursor.execute(query)
        order_status_id = cursor.fetchall()[0][0]
        assert order_status_id == 0
