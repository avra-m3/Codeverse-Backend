
-- Creates Tables to be used for SocialCode BackEnd Database


CREATE TABLE Users(
	User_ID INT NOT NULL AUTO_INCREMENT,
	firstname VARCHAR(100),
	lastname VARCHAR(100),
	PRIMARY KEY( User_ID)
);


CREATE TABLE Collaborators(
	Challenge_ID INT,
	User_ID INT,
	PlaybackStream MEDIUMTEXT
);

CREATE TABLE Challenges(
	Challenge_ID INT NOT NULL AUTO_INCREMENT,
	TimeRecord DATETIME,
	Status VARCHAR(20),
	PRIMARY KEY( Challenge_ID)
);

CREATE TABLE Problems(
	Problem_ID INT NOT NULL AUTO_INCREMENT,
	ProblemStatement MEDIUMTEXT,
	ShortName VARCHAR(20),
	PRIMARY KEY(Problem_ID)
);

CREATE TABLE ProblemOutputs(
	ProblemOutput_ID INT NOT NULL AUTO_INCREMENT,
	Problem_ID INT,
	ExpectedOutput VARCHAR(100),
	Precode MEDIUMTEXT,
	Postcode MEDIUMTEXT,
	PRIMARY KEY(ProblemOutput_ID)
);


