# TestCases - getByProblem_ID return {all cols} 

import pymysql
from model.Template import Template


class TestCases(Template):


    # listTestCases(problem_id)
    # returns List [ dict{"TestCase_ID", "Problem_ID", "ExpectedOutput", "Precode", "Postcode"} ]

    def listTestCases(self, problem_id):
        cur = self.myConnection.cursor()
        dothisSQL = 'SELECT * '
        dothisSQL += 'FROM TestCases ' 
        dothisSQL += 'WHERE Problem_ID = %s'
        cur.execute(dothisSQL, problem_id)
        self.myConnection.commit()
        queryResult = cur.fetchall()

        resultList = list()

        for result in queryResult:

            itemDict = dict()
            itemDict['TestCase_ID'] = result[0]
            itemDict['Problem_ID'] = result[1]
            itemDict['ExpectedOutput'] = result[2]
            itemDict['Precode'] = result[3]
            itemDict['Postcode'] = result[4]
            resultList.append(itemDict)

        return resultList

if __name__ == "__main__":
    testcases = TestCases() 
    print(testcases.listTestCases(1))

