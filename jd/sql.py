# coding=utf-8
# name=hu_yang_jie
import MySQLdb

# conn = MySQLdb.connect('192.168.1.2', 'root', 'mysql', 'dbd')
# cur = conn.cursor()
# sql1 = 'insert into goods(name) value("apple")'
# sql2 = 'select name from goods where name="iphone3"'
# cur.execute(sql1)
# result = cur.fetchone()
# print result
# conn.commit()
# cur.close()
# conn.close()


def insert_goods(data):
    try:
        # print 'Try to insert data.'
        conn = MySQLdb.connect('192.168.1.2', 'root', 'mysql', 'dbd', charset='utf8')
        cur = conn.cursor()
        sql1 = 'insert into goods(name) value(%s)'
        cur.execute(sql1, data)
        conn.commit()
        print 'Insert goods OK!'
        cur.close()
        conn.close()
    except Exception, e:
        print 'Insert goods error!'
        print e.message


def insert_list(goods_list):
    try:
        conn = MySQLdb.connect('192.168.1.2', 'root', 'mysql', 'dbd', charset='utf8')
        cur = conn.cursor()
        sql2 = 'insert into list(lid,gid,new_old,price,max_price,appendix,time) values(%s,%s,%s,%s,%s,%s,%s)'
        cur.execute(sql2, goods_list)
        conn.commit()
        print 'Insert goods_list OK!'
        cur.close()
        conn.close()
    except Exception, e:
        print e.message


def find_data(data):

    try:
        conn = MySQLdb.connect('192.168.1.2', 'root', 'mysql', 'dbd', charset='utf8')
        cur = conn.cursor()
        sql2 = 'select gid from goods where name=%s'
        cur.execute(sql2, data)
        result = cur.fetchone()
        # print result[0]
        cur.close()
        conn.close()
        return result[0]

    except Exception, e:
        print e.message, '~~~~~'

if __name__ == '__main__':
    # data = ('hu',)
    # list_data = (0, 6, 20, 30, 'huyangjie', 2017-11-13)
    # insert_list(list_data)
    goods_list = [16865884, 89, 3, 2, 99, 'hu', '2017-11-16 10:08:00']
    insert_list(goods_list)

