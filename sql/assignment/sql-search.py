
import sqlite3

# connect to the database
with sqlite3.connect ("newnum.db") as connection:
    # establish a cursor
    c = connection.cursor ()
    # while (True):
    #     print ("Choose a number \n")
    #
    #     print ("Enter 1 for AVG")
    #     print ("Enter 2 for MAX")
    #     print ("Enter 3 for MIN")
    #     print ("Enter 4 for SUM")
    #     print ("Enter 5 for EXIT")
    #     check = int (input ("\n"))
    #
    #     if check == 1:
    #         c.execute ("SELECT avg(num) FROM numbers")
    #         row = c.fetchall ()
    #         for i in row:
    #             print (i)
    #
    #     if check == 2:
    #         c.execute ("SELECT MAX(num) FROM numbers")
    #         row = c.fetchall ()
    #         for i in row:
    #             print (i)
    #
    #     if check == 3:
    #         c.execute ("SELECT MIN(num) FROM numbers")
    #         row = c.fetchall ()
    #         for i in row:
    #             print (i)
    #
    #     if check == 4:
    #         c.execute("SELECT SUM(num) FROM numbers")
    #         row = c.fetchall ()
    #         for i in row:
    #             print (i[0])
    #
    #     if check == 5:
    #         break

    prompt = """
    Select the operation that you want to perform [1-5]:
    1. Average
    2. Max
    3. Min
    4. Sum
    5. Exit
    """
    while True:
        user_input = input(prompt)
        if user_input in ["1", "2", "3", "4"]:
            operation = {1:"avg", 2:"max", 3:"min", 4:"sum"}[int(user_input)]
            c.execute("SELECT {}(num) FROM numbers".format(operation))
            get = c.fetchone()
            print(operation + ": %f" % get[0])

        elif user_input == "5":
            print("Exit")
            break
