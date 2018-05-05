# Problems

# Problems 
# get full list: {Problem ID, Shortname, expected time}; 
# get by id {all fields}


import pymysql


class Problems:

	def __init__(self):
		self.myConnection = pymysql.connect(user='root', password='MyNewPass', db='testDB', host='')
		# myConnection = pymysql.connect(
		# 	user='Alex18', 
		# 	password='coLiOSidereC', 
		# 	db='testDB', 
		# 	host='fbhack18db.cdf1m3s6jm9l.ap-southeast-2.rds.amazonaws.com')

	# listProblems(self)
	# returns list[ dict{Problem ID, Shortname, expected time}];

	def listProblems(self):
		cur = self.myConnection.cursor()
 		dothisSQL = 'SELECT * '
 		dothisSQL += 'FROM PROBLEMS'
		cur.execute(dothisSQL)
		self.myConnection.commit()
		queryResult = cur.fetchall()

		resultList = list()

		for result in queryResult:

			itemDict = dict()
			itemDict['Problem_ID'] = result[0]
			itemDict['Problem_Statement'] = result[1]
			itemDict['ExpectedTime'] = result[2]
			itemDict['Shortname'] = result[3]
			resultList.append(itemDict)

		# print(resultList)

		return resultList

	# getProblem(self)
	# returns dict{Problem ID, Shortname, expected time};

	def getProblem(self, problem_id):
		cur = self.myConnection.cursor()
 		dothisSQL = 'SELECT * '
 		dothisSQL += 'FROM PROBLEMS ' 
 		dothisSQL += 'WHERE Problem_ID = %s'
		cur.execute(dothisSQL, problem_id)
		self.myConnection.commit()
		queryResult = cur.fetchall()

		resultList = list()

		for result in queryResult:

			itemDict = dict()
			itemDict['Problem_ID'] = result[0]
			itemDict['Problem_Statement'] = result[1]
			itemDict['ExpectedTime'] = result[2]
			itemDict['Shortname'] = result[3]
			resultList.append(itemDict)

		# print(resultList[0])

		return resultList[0]

if __name__ == "__main__":
	problems = Problems() 
	# db.insertUser(3, "test", "user")
	# user.getUser(3)
	problems.listProblems()
	# problems.getProblems(1)

