-- drop database dbmsfinal;

CREATE USER 'rkin'@'localhost' IDENTIFIED BY '2393';
GRANT ALL PRIVILEGES ON dbmsfinal.* TO 'rkin'@'localhost';

create database dbmsfinal;
use dbmsfinal;


CREATE TABLE  road(road_id varchar(10) NOT NULL, Status VARCHAR(50) DEFAULT 'Active',PRIMARY KEY(road_id));

CREATE TABLE  Vehicle_in(Date DATE, Type TEXT NOT NULL, Owner_type TEXT NOT NULL, Vehicle_no varchar(50) NOT NULL, P_id varchar(2) NOT NULL,ID varchar(13) NOT NULL,PRIMARY KEY(ID, Date),FOREIGN KEY(P_id) REFERENCES road(road_id));

CREATE TABLE  citizen(Contact varchar(10) NOT NULL, ID varchar(13) NOT NULL, Name varchar(50) NOT NULL, no_of_cars INT,PRIMARY KEY(ID));

CREATE TABLE  officer(Contact varchar(10) NOT NULL, ID varchar(13) NOT NULL, Name varchar(50) NOT NULL,PRIMARY KEY(ID));

INSERT INTO citizen(Contact, ID , Name , no_of_cars) VALUES ("9353820323","PES1UG21CS524","Meghana Goru","1");
INSERT INTO citizen(Contact, ID , Name , no_of_cars) VALUES (	"8310730145","PES1UG21CS489","Rishika Kinger","1");
INSERT INTO citizen(Contact, ID , Name , no_of_cars) VALUES ("9845648878","PES1UG21CS490","Mihir Sanjay","1");
INSERT INTO citizen(Contact, ID , Name , no_of_cars) VALUES ("9916947028","PES1UG21CS491","Rishi Kinger","2");
INSERT INTO citizen(Contact, ID , Name , no_of_cars) VALUES ("9845647028","PES1UG21CS492","Sanjana Kinger","3");


INSERT INTO officer(Contact , ID , Name ) VALUES ("919299292","PES1UGCS100","Nagasundhari");
INSERT INTO officer(Contact , ID , Name ) VALUES ("020202002","PES1UGCS101","Sivagamasundhari");
INSERT INTO officer(Contact , ID , Name ) VALUES ("1993993930","PES1UGCS102","Bhargavi");
INSERT INTO officer(Contact , ID , Name ) VALUES ("9192202001","PES1UGCS103","Ashwini");
INSERT INTO officer(Contact , ID , Name ) VALUES ("199390302","PES1UGCS104","BJD");


INSERT INTO road(road_id, Status) VALUES ('R1', 'Active');
INSERT INTO road(road_id, Status) VALUES ('R2', 'Active');
INSERT INTO road(road_id, Status) VALUES ('R3', 'Active');
INSERT INTO road(road_id, Status) VALUES ('R4', 'Active');
INSERT INTO road(road_id, Status) VALUES ('R5', 'Active');



DELIMITER //
CREATE PROCEDURE StatusUpdation ( IN Road_id VARCHAR(2))
BEGIN
UPDATE road SET Status="Occupied" where road.road_id = Road_id ;
END;
//
Delimiter ;




DELIMITER //
CREATE TRIGGER SETSTATUS  AFTER INSERT ON Vehicle_in
FOR EACH ROW 
BEGIN
    CALL StatusUpdation(NEW.P_id);
END //
Delimiter ;







