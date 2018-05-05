# Challenges

# Challenges - 
# create{} will get problem_ID, return challenge_ID; 
# update by challenge ID(new status); 
# get(status) return list: {Challenge_ID, Problem_ID, CreatedAt}, 
# get by ID

import pymysql
import datetime
import time


class Challenges:

	def __init__(self):
		self.myConnection = pymysql.connect(user='root', password='MyNewPass', db='testDB', host='')
		# myConnection = pymysql.connect(
		# 	user='Alex18', 
		# 	password='coLiOSidereC', 
		# 	db='testDB', 
		# 	host='fbhack18db.cdf1m3s6jm9l.ap-southeast-2.rds.amazonaws.com')



	# createChallenge(self, problem_id, status)
	# returns Challenge_ID of new challenge created

	def createChallenge(self, problem_id, status):

		now = datetime.datetime.now()
		now.strftime('%Y-%m-%d %H:%M:%S')

		dothisSQL = 'INSERT INTO CHALLENGES '
 		dothisSQL += '(Problem_ID, CreatedAt, Status) '
 		dothisSQL += 'VALUES ( %s, %s, %s)'
		cur = self.myConnection.cursor()
		cur.execute(dothisSQL, (problem_id, now, status))
		self.myConnection.commit()
		return cur.lastrowid

	# updateChallengeStatus(self, challenge_id, new_status)
	# Updates the status associated with a given challenge

	def updateChallengeStatus(self, challenge_id, new_status):
		dothisSQL = 'UPDATE CHALLENGES '
		dothisSQL += 'SET STATUS = %s '
		dothisSQL += 'WHERE CHALLENGE_ID = %s'

		print(dothisSQL)
		cur = self.myConnection.cursor()
		cur.execute(dothisSQL, (new_status, challenge_id))
		self.myConnection.commit()


	# listChallenges(self)
	# returns list[ dict{Challenge_ID, Problem_ID, CreatedAt, Status}];

	def listChallenges(self, status):
		cur = self.myConnection.cursor()
 		dothisSQL = 'SELECT * '
 		dothisSQL += 'FROM CHALLENGES '
 		dothisSQL += 'WHERE STATUS = %s'
		cur.execute(dothisSQL, status)
		self.myConnection.commit()
		queryResult = cur.fetchall()

		resultList = list()

		for result in queryResult:

			itemDict = dict()
			itemDict['Challenge_ID'] = result[0]
			itemDict['Problem_ID'] = result[1]
			itemDict['CreatedAt'] = result[2]
			itemDict['Status'] = result[3]
			resultList.append(itemDict)

		# print(resultList)

		return resultList

	# getChallenge(self, Challenge_ID)
	# returns list[ dict{Challenge_ID, Problem_ID, CreatedAt, Status}];

	def getChallenge(self, challenge_ID):
		cur = self.myConnection.cursor()
 		dothisSQL = 'SELECT * '
 		dothisSQL += 'FROM CHALLENGES '
 		dothisSQL += 'WHERE CHALLENGE_ID = %s'
		cur.execute(dothisSQL, challenge_ID)
		self.myConnection.commit()
		queryResult = cur.fetchall()

		resultList = list()

		for result in queryResult:

			itemDict = dict()
			itemDict['Challenge_ID'] = result[0]
			itemDict['Problem_ID'] = result[1]
			itemDict['CreatedAt'] = result[2]
			itemDict['Status'] = result[3]
			resultList.append(itemDict)

		# print(resultList[0])

		return resultList[0]


if __name__ == "__main__":
	challenges = Challenges() 

	# challenges.createChallenge(1, "In progress")
	# challenges.listChallenges("InProgress")
	# challenges.getChallenge(1)
	# challenges.updateChallengeStatus(1, "Finalised")
	# challenges.createChallenge(4, 1, now, "In progress")

