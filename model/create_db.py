# db_interaction.py
# Handles interaction with MYSQL database

import pymysql


class db_interaction:
	# myConnection = MySQLdb.connect(db='base', user='root', passwd='root-1234', host='localhost')

	def __init__(self):
		self.myConnection = pymysql.connect(user='root', password='MyNewPass', db='testDB', host='')
		# myConnection = pymysql.connect(
		# 	user='Alex18', 
		# 	password='coLiOSidereC', 
		# 	db='testDB', 
		# 	host='fbhack18db.cdf1m3s6jm9l.ap-southeast-2.rds.amazonaws.com')

	def insertUser(self, firstname, lastname):
		self.firstname = firstname
 		self.lastname = lastname
		cur = self.myConnection.cursor()

 		# insertSQL = 'INSERT INTO USERS VALUES (1, "test", "user")'
 		insertSQL = 'INSERT INTO USERS VALUES (2, "' + firstname + '", "' + lastname + '")'
		cur.execute(insertSQL)
		self.myConnection.commit()



 	
	# def createUser(self, firstname, lastname):
	# 	self.firstname = firstname
 #       	self.lastname = lastname

	# 	insertSql = 'INSERT INTO USERS VALUES ("' + firstname + ", " + lastname + ")"
	# 	cur = self.myConnection.cursor()
	# 	cur.execute(insertSQL)
	# 	myConnection.commit()


	# def getUser():

		# cur = myConnection.cursor()
		# cur.execute('SELECT vtype FROM USERS WHERE vtype LIKE "%otorcycle%";')
		# cycleList = cur.fetchall()

		# selectSQL = ('''
		# 	SELECT t.vtype, a.accident_severity
		# 	FROM accidents_2015 AS a
		# 	JOIN vehicles_2015 AS v ON a.accident_index = v.Accident_Index
		# 	JOIN vehicle_type AS t ON v.Vehicle_Type = t.vcode
		# 	WHERE t.vtype LIKE %s
		# 	ORDER BY a.accident_severity;''')
		
		# insertSQL = ('''
		# 	INSERT INTO accident_medians VALUES (%s, %s);''')
		
		# for cycle in cycleList:
		# 	cur.execute(selectSQL,cycle[0])
		# 	accidents = cur.fetchall()
		# 	quotient, remainder = divmod(len(accidents),2)
		# 	if  remainder:
		# 		med_sev = accidents[quotient][1]
		# 	else:
		# 		med_sev = (accidents[quotient][1] + accidents[quotient+2][1])/2
		# 	print('Finding median for',cycle[0])
		# 	cur.execute(insertSQL,(cycle[0],med_sev))

		# myConnection.commit()
		# myConnection.close()

if __name__ == "__main__":
	db = db_interaction() 
	db.insertUser("test", "user")

