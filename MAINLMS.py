
import mysql.connector as sqlcon

CONNECTION = sqlcon.connect(host="localhost" , user="root" , password="python" , database="lms")


def AddBk():

    BK_NAME = input("ENTER BOOK NAME :")
    BK_CODE = input("ENTER BOOK CODE :")
    BK_TOTAL = input("ENTER TOTAL BOOKS :")
    BK_TYPE = input("ENTER THE TYPE OF BOOK :")

    DATA = (BK_NAME,BK_CODE,BK_TOTAL,BK_TYPE)

    SQL = 'insert into BOOKS_INFO values(%s,%s,%s,%s)'
    CRSR = CONNECTION.cursor()
    CRSR.execute(SQL,DATA)
    CONNECTION.commit()

    print("------------DATA ENTERED SUCCESSFULLY------------")
    contrl()




def IssueBk():

    BK_ISSUE_NAME = input("ENTER BOOK NAME ISSUED TO USER :")
    BK_QUANTITY = input("ENTER TOTAL BOOKS ISSUED :")
    BK_CODE = input("ENTER BOOK CODE :")
    BK_USER = input("ENTER USER NAME :")
    USER_REG = input("ENTER REG NUMBER :")
    ISSUE_DATE = input("ENTER ISSUE DATE :")

    DATA = (BK_ISSUE_NAME,BK_QUANTITY,BK_CODE,BK_USER,USER_REG,ISSUE_DATE)

    SQL = "insert into ISSUE_INFO values(%s,%s,%s,%s,%s,%s)"
    CRSR = CONNECTION.cursor()
    CRSR.execute(SQL,DATA)
    CONNECTION.commit()

    print("---------------DATA ENTERED SUCCESSFULLY---------------")
    print("BOOK ISSUED TO => ",BK_USER)

    BookUp(BK_CODE,-1)




def SbmtBk():

    BK_NAME_TO_SBMT = input("ENTER BOOK NAME TO SUBMIT :")
    BK_QUANTITY_TO_SBMT = input("ENTER QUANTITY OF BOOK TO SUBMIT :")
    BK_USER = input("ENTER THE USER NAME :")
    USER_REG = input("ENTER THE REG NUMBER :")
    BK_CODE = input("ENTER THE BOOK CODE :")
    SUBMIT_DATE = input("ENTER SUBMIT DATE :")

    DATA = (BK_NAME_TO_SBMT,BK_QUANTITY_TO_SBMT,BK_USER,USER_REG,BK_CODE,SUBMIT_DATE)

    SQL = "insert into SUBMISSION_INFO values(%s,%s,%s,%s,%s,%s)"
    CRSR = CONNECTION.cursor()
    CRSR.execute(SQL,DATA)
    CONNECTION.commit()

    print("---------------DATA ENTERED SUCCESSFULLY---------------")
    print("BOOK SUBMITTED FROM => ",BK_USER)

    BookUp(BK_CODE,1)




def DelBk():

    BK_CODE = input("ENTER THE BOOK CODE :")
    SQL = "delete from BOOKS_INFO where BOOK_CODE = %s"
    DATA = (BK_CODE,)
    CRSR = CONNECTION.cursor(buffered=True)
    CRSR.execute(SQL,DATA)
    CONNECTION.commit()
    contrl()




def DispBk():
    SQL = "select * from BOOKS_INFO"
    CRSR = CONNECTION.cursor()
    CRSR.execute(SQL)
    MyRes = CRSR.fetchall()

    for i in MyRes:
        print("BOOK NAME : ", i[0])
        print("BOOK CODE : ", i[1])
        print("TOTAL : ", i[2])
        print("SUBJECT : ", i[3])
        print(">-------------------------<")
    
    contrl()



def BookUp(BK_CODE,u):

    SQL = "select BOOK_TOTAL from BOOKS_INFO where BOOK_CODE = %s"
    DATA = (BK_CODE,)
    CRSR = CONNECTION.cursor(buffered=True)
    CRSR.execute(SQL,DATA)
    MyRes = CRSR.fetchone()
    total = MyRes[0] + u

    SQL = "update BOOKS_INFO set BOOK_TOTAL = %s where BOOK_CODE = %s"
    DATA = (total,BK_CODE)
    CRSR.execute(SQL,DATA)
    CONNECTION.commit()
    contrl()




def contrl():

    print("""
                1. TO ADD BOOK ENTER (1)
                2. TO ISSUE BOOK ENTER (2)
                3. TO DELETE BOOK ENTER (3)
                4. TO SUBMIT BOOK ENTER (4)
                5. TO DISPLAY BOOK ENTER (5)
         """)

    USR_CMD = input("ENTER THE OPERATION TO BE PERFORMED BE SEEING THE ABOVE INSTRUCTION => ")


    if USR_CMD == "1":
        AddBk()
    
    elif USR_CMD == "2":
        IssueBk()

    elif USR_CMD == "3":
        DelBk()

    elif USR_CMD == "4":
        SbmtBk()

    elif USR_CMD == "5":
        DispBk()
    
    else:
        print("WRONG INPUT !")
        contrl()





def PsWrd():

    PASS = "python"
    USR_PASS = input("ENTER THE PASSWORD => ")

    if USR_PASS == PASS:
        contrl()
    else:
        print("WRONG PASSWORD !")
        PsWrd()

PsWrd()
