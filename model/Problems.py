# Problems

# Problems 
# get full list: {Problem ID, Shortname, expected time}; 
# get by id {all fields}


import pymysql

from model.Template import Template


class Problems(Template):


    # listProblems(self)
    # returns list[ dict{Problem ID, Shortname, expected time}];

    def listProblems(self):
        cur = self.myConnection.cursor()
        dothisSQL = 'SELECT * '
        dothisSQL += 'FROM Problems'
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
        dothisSQL += 'FROM Problems ' 
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
    print(problems.listProblems())
    print(problems.getProblem(1))

