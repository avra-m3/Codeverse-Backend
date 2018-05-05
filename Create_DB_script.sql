
-- Creates Tables to be used for SocialCode BackEnd Database

DROP DATABASE IF EXISTS testDB;

CREATE DATABASE IF NOT EXISTS testDB;

USE testDB;

CREATE TABLE Users(
	User_ID VARCHAR(100) NOT NULL,
	firstname VARCHAR(100),
	lastname VARCHAR(100),
	PRIMARY KEY( User_ID)
);

CREATE TABLE Problems(
	Problem_ID INT NOT NULL AUTO_INCREMENT,
	ProblemStatement MEDIUMTEXT,
	ExpectedTime INT,
	ShortName VARCHAR(20),
	PRIMARY KEY(Problem_ID)
);

CREATE TABLE Challenges(
	Challenge_ID INT NOT NULL AUTO_INCREMENT,
	Problem_ID INT,
	CreatedAt DATETIME DEFAULT Now(),
	Status VARCHAR(20) DEFAULT 'Created',
	PRIMARY KEY( Challenge_ID),
	FOREIGN KEY(Problem_ID) REFERENCES Problems(Problem_ID)
);

CREATE TABLE Collaborators(
	Challenge_ID INT,
	User_ID VARCHAR(100),
	PlaybackStream MEDIUMTEXT,
	CodeStatus VARCHAR(1000),
	SubmittedAt DATETIME DEFAULT NULL,
	ExecutionTime INT,
	SubmissionID VARCHAR(20),
	PRIMARY KEY( Challenge_ID, User_ID),
	FOREIGN KEY( User_ID) REFERENCES Users(User_ID),
	FOREIGN KEY( Challenge_ID) REFERENCES Challenges(Challenge_ID)
);

CREATE TABLE TestCases(
	TestCase_ID INT NOT NULL AUTO_INCREMENT,
	Problem_ID INT,
	ExpectedOutput VARCHAR(100),
	Precode MEDIUMTEXT,
	Postcode MEDIUMTEXT,
	PRIMARY KEY(TestCase_ID),
	FOREIGN KEY(Problem_ID) REFERENCES Problems(Problem_ID)
);



INSERT INTO Users VALUES (1, "Test", "User1");
INSERT INTO Users VALUES (2, "Test", "User2");
INSERT INTO Users VALUES (3, "Test", "User3");

INSERT INTO Problems VALUES 
	(	1, 
		"Input:  An int x between zero and 50 
		Problem: Write a function that returns x + 3
		MethodSignature: function plusThree(x){ //Your Code Here// }", 
		10, 
		"PlusThree Problem"
	);

INSERT INTO TestCases VALUES 
	(	1, 
		1, 
		"true", 
		"/* precode */", 
		"\nif (plusThree(5) == 8){putstr(true);} else {putstr(false);}"
	);

INSERT INTO Problems VALUES 
	(	2, 
		"Write a function that tests whether a string is a palindrome.
		Return true if StringA is a palindrome, else false
		MethodSignature: function isPalindrome(StringA){ //Your Code Here// }", 
		10, 
		"isPalindromeProblem"
	);

INSERT INTO TestCases VALUES 
	(	2, 
		2, 
		"true", 
		"/* precode */", 
		"\n if (isPalindrome(""madam"") == true){putstr(true);} else {putstr(false);}"
	);

INSERT INTO Problems VALUES 
	(	3, 
		"Given two strings, write a program that efficiently finds the longest common subsequence.
		Return a string being that longest common subsequence.
		MethodSignature: function getCommonSubsequence(stringA, stringB){ //Your Code Here// }", 
		10, 
		"getCommonSubsquenceProblem"
	);

INSERT INTO TestCases VALUES 
	(	3, 
		3, 
		"true", 
		"/* precode */", 
		"\nif (getCommonSubsequence('abaacd', 'dbaacd').localeCompare('baacd') == 0)
			{putstr(true);} 
			else {putstr(false);}"
	);


INSERT INTO Challenges (Challenge_ID, Problem_ID, Status) VALUES (1, 1, "InProgress");
INSERT INTO Challenges (Challenge_ID, Problem_ID, Status) VALUES (2, 2, "InProgress");
INSERT INTO Challenges (Challenge_ID, Problem_ID, Status) VALUES (3, 3, "InProgress");


