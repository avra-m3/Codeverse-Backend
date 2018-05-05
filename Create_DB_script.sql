
-- Creates Tables to be used for SocialCode BackEnd Database

DROP DATABASE IF EXISTS testDB;

CREATE DATABASE IF NOT EXISTS testDB;

USE testDB;

CREATE TABLE Users(
	User_ID INT NOT NULL AUTO_INCREMENT,
	firstname VARCHAR(100),
	lastname VARCHAR(100),
	PRIMARY KEY( User_ID)
);


CREATE TABLE Collaborators(
	Challenge_ID INT,
	User_ID INT,
	PlaybackStream MEDIUMTEXT,
	CodeStatus VARCHAR(20),
	SubmittedAt DATETIME DEFAULT NULL,
	ExecutionTime INT
	PRIMARY KEY( Challenge_ID, User_ID)
	FOREIGN KEY(User_ID) REFERENCES Users(User_ID)
	FOREIGN KEY(Challenge_ID) REFERENCES Challenges(Challenge_ID)
);

CREATE TABLE Challenges(
	Challenge_ID INT NOT NULL AUTO_INCREMENT,
	Problem_ID INT,
	CreatedAt DATETIME,
	Status VARCHAR(20),
	PRIMARY KEY( Challenge_ID)
	FOREIGN KEY(Problem_ID) REFERENCES Problems(Problem_ID)
);

CREATE TABLE Problems(
	Problem_ID INT NOT NULL AUTO_INCREMENT,
	ProblemStatement MEDIUMTEXT,
	ExpectedTime INT,
	ShortName VARCHAR(20),
	PRIMARY KEY(Problem_ID)
);

CREATE TABLE TestCases(
	TestCase_ID INT NOT NULL AUTO_INCREMENT,
	Problem_ID INT,
	ExpectedOutput VARCHAR(100),
	Precode MEDIUMTEXT,
	Postcode MEDIUMTEXT,
	PRIMARY KEY(ProblemOutput_ID)
	FOREIGN KEY(Problem_ID) REFERENCES Problems(Problem_ID)
);


