#!/usr/bin/python

import mysql.connector
from mysql.connector import errorcode
from datetime import datetime

##===============================================

class DatabaseUtility:
        def __init__(self, database, tableName):
                self.db = database
                self.tableName = tableName
                p = 'raspberry'
                self.cnx = mysql.connector.connect(user = 'root',
                                                                        password = p,
                                                                        host = '127.0.0.1', charset='utf8',
                     use_unicode=True)
                self.cursor = self.cnx.cursor()


                self.ConnectToDatabase()
                self.DeleteDatabase()


        def ConnectToDatabase(self):
                try:
                        self.cnx.database = self.db
                except mysql.connector.Error as err:
                        if err.errno == errorcode.ER_BAD_DB_ERROR:
                                self.CreateDatabase()
                                self.cnx.database = self.db
                        else:
                                print(err.msg)

        def DeleteDatabase(self):
                try:
                        self.RunCommand("DROP DATABASE %s" %self.db)
                except mysql.connector.Error as err:
                        print("Failed creating database: {}".format(err))



        def RunCommand(self, cmd):
                #print ("RUNNING COMMAND: " + cmd)
                try:
                        self.cursor.execute(cmd)
                        self.cnx.commit()

                except mysql.connector.Error as err:
                        #print ('ERROR MESSAGE: ' + str(err.msg))
                        #print ('WITH ' + cmd)
                        print "erro"
                try:
                        msg = self.cursor.fetchall()
                except:
                        msg = self.cursor.fetchone()
                return msg


if __name__ == '__main__':
        db = 'FaureciaSmed'
        tableName = 'Tempos'

        dbu = DatabaseUtility(db, tableName)





