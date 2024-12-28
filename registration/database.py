import mysql.connector

def open():
    global conn
    global cursor
    conn=mysql.connector.connect(host='localhost',database='stu',user='root',password='123456')
    cursor=conn.cursor()
def close():
    conn.commit()
    cursor.close()
    conn.close()

def login(username,course,paymentstatus):
    open()
    query=f"select * from students1 where username='{username}'and course='{course}'and paymentstatus='{paymentstatus}'"
    #print("qyery",query)
    cursor.execute(query)
    rec=cursor.fetchall()
    if len(rec)>0:
        return True
    else:
        return False
    close()
