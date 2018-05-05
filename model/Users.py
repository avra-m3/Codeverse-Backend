# User

# Return dict with keys as db columns

# Users - get, create


import pymysql


class Users:

	def __init__(self):
		self.myConnection = pymysql.connect(user='root', password='MyNewPass', db='testDB', host='')
		# myConnection = pymysql.connect(
		# 	user='Alex18', 
		# 	password='coLiOSidereC', 
		# 	db='testDB', 
		# 	host='fbhack18db.cdf1m3s6jm9l.ap-southeast-2.rds.amazonaws.com')

	def getUser(self, id):
		cur = self.myConnection.cursor()
 		dothisSQL = 'SELECT * '
 		dothisSQL += 'FROM Users '
 		dothisSQL += 'WHERE User_ID = %s'
		cur.execute(insertSQL, id)
		self.myConnection.commit()
		queryResult = cur.fetchall()
		# print(queryResult)
		return queryResult[0] #Should return user object 

	def createUser(self, id, firstname, lastname):
		dothisSQL = 'INSERT INTO Users '
 		dothisSQL += 'VALUES ( %s, %s, %s)'
		cur = self.myConnection.cursor()
		# print(dothisSQL)
		cur.execute(dothisSQL, (id, firstname, lastname))
		self.myConnection.commit()

if __name__ == "__main__":
	users = Users() 
	# db.insertUser(3, "test", "user")
	# user.getUser(3)
	users.createUser(4, "test", "user4")

