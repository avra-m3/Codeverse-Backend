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

        self.myConnection = pymysql.connect(
            user=cfg.mysql['user'], 
            password=cfg.mysql['password'], 
            db=cfg.mysql['db'],
            host=cfg.mysql['host']
            )
    # createChallenge(self, problem_id, status)
    # returns Challenge_ID of new challenge created
    
    def createChallenge(self, problem_id, status):
        now = datetime.datetime.now()
        now.strftime('%Y-%m-%d %H:%M:%S')

        dothisSQL = 'INSERT INTO Challenges '
        dothisSQL += '(Problem_ID, CreatedAt, Status) '
        dothisSQL += 'VALUES ( %s, %s, %s)'
        cur = self.myConnection.cursor()
        cur.execute(dothisSQL, (problem_id, now, status))
        self.myConnection.commit()
        return cur.lastrowid

    # updateChallengeStatus(self, challenge_id, new_status)
    # Updates the status associated with a given challenge

    def updateChallengeStatus(self, challenge_id, new_status):
        dothisSQL = 'UPDATE Challenges '
        dothisSQL += 'SET Status = %s '
        dothisSQL += 'WHERE Challenge_ID = %s'
        cur = self.myConnection.cursor()
        cur.execute(dothisSQL, (new_status, challenge_id))
        self.myConnection.commit()


    # listChallenges(self)
    # returns list[ dict{Challenge_ID, Problem_ID, CreatedAt, Status}];

    def listChallenges(self, status):
        cur = self.myConnection.cursor()
        dothisSQL = 'SELECT * '
        dothisSQL += 'FROM Challenges '
        dothisSQL += 'WHERE Status = %s'
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

        return resultList

    # getChallenge(self, Challenge_ID)
    # returns list[ dict{Challenge_ID, Problem_ID, CreatedAt, Status}];

    def getChallenge(self, challenge_ID):
        cur = self.myConnection.cursor()
        dothisSQL = 'SELECT * '
        dothisSQL += 'FROM Challenges '
        dothisSQL += 'WHERE Challenge_ID = %s'
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

        return resultList[0]


if __name__ == "__main__":
    challenges = Challenges() 
    print(challenges.createChallenge(2, "In progress"))
    print(challenges.listChallenges("InProgress"))
    print(challenges.getChallenge(1))
    challenges.updateChallengeStatus(5, "Finalised")

