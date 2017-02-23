#!/usr/bin/python

import mysql.connector
from mysql.connector import errorcode
from datetime import datetime, timedelta
import time


##===============================================

class DatabaseUtility:
    ##Inicializar base de dados
    def __init__(self, database, tableName, queryLinesLimit, linha, tempoObjectivo, tempoIntermedio, tempoMinimo, tempoMaximo):
        self.db = database
        self.tableName = tableName
        self.queryLinesLimit= queryLinesLimit
        self.tempoObjectivo = tempoObjectivo
        self.tempoIntermedio = tempoIntermedio
        self.tempoMinimo = tempoMinimo
        self.tempoMaximo = tempoMaximo
        self.linha = str(linha)


        #Password definida para a base de dados
        p = 'eSmed'

        self.cnx = mysql.connector.connect(user='root',
                                           password=p,
                                           host='127.0.0.1', charset='utf8',
                                           use_unicode=True)

        self.cursor = self.cnx.cursor(buffered=True)
        self.ConnectToDatabase()
        self.CreateTable()
        self.didSetTime()

    ##Coneccao a base de dados
    def ConnectToDatabase(self):
        try:
            self.cnx.database = self.db
        except mysql.connector.Error as err:
            if err.errno == errorcode.ER_BAD_DB_ERROR:
                self.CreateDatabase()
                self.cnx.database = self.db
            else:
                print(err.msg)


    ## Criar tabela apartir do ficheiro "novaDB.sql"

    def CreateDatabase(self):
        try:
            self.RunCommand("CREATE DATABASE %s DEFAULT CHARACTER SET 'utf8';" % self.db)
        except mysql.connector.Error as err:
            print("Failed creating database: {}".format(err))


    ## Criar tabela apartir do ficheiro "novaDB.sql"
    def CreateTable(self):

        fd = open('novaDB.sql', 'r')
        sqlFile = fd.read()
        fd.close()

        # all SQL commands (split on ';')
        sqlCommands = sqlFile.split(';')

        # Execute every command from the input file
        for command in sqlCommands:
            # This will skip and report errors
            # For example, if the tables do not yet exist, this will skip over
            # the DROP TABLE commands
            try:
                self.cursor.execute(command)
            except:
                pass


    def GetTableToExport(self):
        return self.RunCommand("SELECT * FROM %s WHERE linha = '%s';" % (self.tableName,self.linha))

    def Show(self):
        return self.RunCommand("select column_name from information_schema.columns where table_name='%s'" % self.tableName)



    #Obter valor limite para circulo verde . Valor a mostrar no tempo objectivo
    def obterValorlimite(self, limite):
        SEG = str(timedelta(seconds=limite))[3:]
        if (SEG == str("9:59")):
            limite = str(timedelta(seconds=limite))[3:]

        else:
            limite = "0"+str(timedelta(seconds=limite))[3:]
        return limite


    ## Obter tabela dos ultimos tempos
    def GetTable_last_data(self, data, hora, tempo,cor):
        self.CreateTable()
        return self.RunCommand("SELECT DISTINCT  %s,%s,%s, %s"
                               " FROM %s "
                               "where linha = '%s'"
                               "ORDER BY ID DESC "
                               "LIMIT %d ;" % (data, hora, tempo, cor, self.tableName,self.linha, self.queryLinesLimit))


    ## Obter tabela dos melhores tempos
    def GetTable_best_data(self, data, hora, tempo,cor):
        self.CreateTable()
        limiteTempoInferior = self.obterValorlimite(self.tempoMinimo)
        limiteTempoSuperior = self.obterValorlimite(self.tempoMaximo)
        return self.RunCommand("SELECT DISTINCT  %s,%s,%s,%s "
                               "FROM %s "
                               "WHERE linha = '%s' "
                               "and tempo > '%s' "
                               "and tempo < '%s' "
                               "ORDER BY tempo ASC "
                               "LIMIT %d ;"
                               % (data, hora, tempo, cor, self.tableName,self.linha, limiteTempoInferior, limiteTempoSuperior, self.queryLinesLimit))



    def RunCommand(self, cmd):
        # print ("RUNNING COMMAND: " + cmd)
        try:
            self.cursor.execute(cmd)
            self.cnx.commit()

        except mysql.connector.Error as err:
            print ('ERROR MESSAGE: ' + str(err.msg))
            pass

        try:
            msg = self.cursor.fetchall()
        except:
            msg = self.cursor.fetchone()
        return msg

    def RunCommand2(self):
        try:
            self.cnx.commit()

        except mysql.connector.Error as err:
            print ('ERROR MESSAGE: ' + str(err.msg))
            pass

        try:
            msg = self.cursor.fetchall()
        except:
            msg = self.cursor.fetchone()
        return msg



    ##Adiciona registo a base de dados
    def AddEntryToTable(self,  tempo, linia):
        print "Chamado a colocar"
        date1 = datetime.now().strftime("%y-%m-%d")
        time2 = datetime.now().strftime("%H:%M:%S")


        tempo_Objectivo = timedelta(seconds=self.tempoObjectivo)
        tempo_Intermedio = timedelta(seconds=self.tempoIntermedio)
        tempoMinimo = timedelta(seconds=self.tempoMinimo)
        tempoMaximo = timedelta(seconds=self.tempoMaximo)


        print  self.tempoObjectivo
        if tempo < tempo_Objectivo:
            self.cursor.execute("SELECT cor FROM Cores WHERE tempo_max = '%s'", [self.tempoObjectivo])
            teste = self.RunCommand2()
            sol = [seq[0] for seq in teste][0]
            s= sol
        elif (tempo_Objectivo < tempo < tempo_Intermedio):
            self.cursor.execute("SELECT cor FROM Cores WHERE tempo_max = '%s'", [self.tempoIntermedio])
            teste = self.RunCommand2()
            sol = [seq[0] for seq in teste][0]
            s = sol
        else :
            s = "Vermelho"

        s2 = tempo.total_seconds()
        ai = '{:02}:{:02}:{:02}'.format(s2 // 3600, s2 % 3600 // 60, s2 % 60)
        st = str(tempo.microseconds)
        st2 = st[:3]
        st4 = time.strftime("%M:%S.", time.gmtime(tempo.seconds))
        ultimo = st4 + st2




        if tempo < tempoMinimo or tempo > tempoMaximo :
            ## MP
            self.cursor.execute("SELECT tipo FROM Paragens WHERE ID = 2")
            teste = self.RunCommand2()
            sol = [seq[0] for seq in teste][0]
            d = sol
        else:
            ## SMED
            self.cursor.execute("SELECT tipo FROM Paragens WHERE ID = 1")
            teste = self.RunCommand2()
            sol = [seq[0] for seq in teste][0]
            d = sol
        cmd = " INSERT INTO " + self.tableName + " (linha,data, hora, tempo, cor, tipo)"
        cmd += " VALUES ('%s','%s', '%s', '%s' , '%s' , '%s');" % (linia, date1, time2, ultimo,s,d )
        self.RunCommand(cmd)


    def didSetTime(self):
        array1 = []
        cmd = " UPDATE Cores SET tempo_max = '%s' WHERE cor = 'Verde';" %(self.tempoObjectivo)
        cmd2 = " UPDATE Cores SET tempo_max = '%s' WHERE cor = 'Laranja';" %(self.tempoIntermedio)
        cmd3 = " UPDATE Cores SET tempo_max = '%s' WHERE cor = 'Vermelho';" %(self.tempoMaximo)
        array1.extend([cmd,cmd2,cmd3])
        for cmd in array1:
            self.RunCommand(cmd)

    ##DEL
    def __del__(self):
        self.cursor.close()
        self.cnx.close()



##===============================================
##===============================================


if __name__ == '__main__':
    db = 'FaureciaSmed'
    tableName = 'Tempos'

    dbu = DatabaseUtility(db, tableName)
