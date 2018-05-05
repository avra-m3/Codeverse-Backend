# Collaborators

# Collaborators - getbyChallengeID; return list {All cols}; update(challenge_ID, User_ID) return true;
# get create list update
# Return dict with keys as db columns

import pymysql
import datetime
import time


class Collaborators:

	def __init__(self):

		self.myConnection = pymysql.connect(
			user=cfg.mysql['user'], 
			password=cfg.mysql['password'], 
			db=cfg.mysql['db'], 
			host=cfg.mysql['host'])



	# getCollaborators(self, challenge_id); 
	# returns list [ Dict { Challenge_ID, User_ID, PlaybackStream, CodeStatus, 
	#	SubmittedAt, ExecutionTime, SubmissionID} ]; 

	def getCollaborator(self, challenge_id, user_id):
			cur = self.myConnection.cursor()
	 		dothisSQL = 'SELECT * '
	 		dothisSQL += 'FROM Collaborators '
	 		dothisSQL += 'WHERE Challenge_ID = %s '
	 		dothisSQL += 'AND User_ID = %s'
			cur.execute(dothisSQL, (challenge_id, user_id))
			self.myConnection.commit()
			queryResult = cur.fetchall()
			resultList = list()
			
			for result in queryResult:

				itemDict = dict()
				itemDict['Challenge_ID'] = result[0]
				itemDict['User_ID'] = result[1]
				itemDict['PlaybackStream'] = result[2]
				itemDict['CodeStatus'] = result[3]
				itemDict['SubmittedAt'] = result[4]
				itemDict['ExecutionTime'] = result[5]
				itemDict['SubmissionID'] = result[6]
				resultList.append(itemDict)

			return resultList[0]

	# listCollaborators(self, challenge_id); 
	# returns list [ Dict { Challenge_ID, User_ID, PlaybackStream, CodeStatus, 
	#	SubmittedAt, ExecutionTime, SubmissionID} ]; 

	def listCollaborators(self, challenge_id):
		cur = self.myConnection.cursor()
 		dothisSQL = 'SELECT * '
 		dothisSQL += 'FROM Collaborators '
 		dothisSQL += 'WHERE Challenge_ID = %s'
		cur.execute(dothisSQL, challenge_id)
		self.myConnection.commit()
		queryResult = cur.fetchall()

		resultList = list()

		for result in queryResult:

			itemDict = dict()
			itemDict['Challenge_ID'] = result[0]
			itemDict['User_ID'] = result[1]
			itemDict['PlaybackStream'] = result[2]
			itemDict['CodeStatus'] = result[3]
			itemDict['SubmittedAt'] = result[4]
			itemDict['executionTime'] = result[5]
			itemDict['submissionID'] = result[6]
			resultList.append(itemDict)

		# print(resultList)

		return resultList


	# createCollaborator(self, challenge_id, user_id, playbackStream, codeStatus, submittedAt, executionTime, submissionID)

	def createCollaborator(self, challenge_id, user_id, playbackStream, codeStatus, submittedAt, executionTime, submissionID):
		dothisSQL = 'INSERT INTO Collaborators '
 		dothisSQL += 'VALUES ( %s, %s, %s, %s, %s, %s, %s)'
		cur = self.myConnection.cursor()
		# print(dothisSQL)
		cur.execute(dothisSQL, (challenge_id, user_id, playbackStream, codeStatus, submittedAt, executionTime, submissionID))
		self.myConnection.commit()
		return

	# updateCollaborator(self, challenge_id, user_id)
	# Updates the user_id associated with a give challenge

	def updateCollaborator(self, challenge_id, user_id):
		dothisSQL = 'UPDATE Collaborators '
		dothisSQL += 'SET User_ID = %s '
		dothisSQL += 'WHERE Challenge_ID = %s'
		cur = self.myConnection.cursor()
		cur.execute(dothisSQL, (user_id, challenge_id))
		self.myConnection.commit()


if __name__ == "__main__":
	collaborators = Collaborators() 

	now = datetime.datetime(2018, 5, 5)
	now.strftime('%Y-%m-%d %H:%M:%S')

	collaborators.createCollaborator(2,3,"playbackStream","finished", now, "30", 99)
	print(collaborators.getCollaborator(2,2))
	print(collaborators.listCollaborators(1))
	collaborators.updateCollaborator(2,1)

