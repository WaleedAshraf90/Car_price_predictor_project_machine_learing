SELECT * FROM CARS;

SELECT Price, Make FROM CARS

SELECT Count(*) AS Model
FROM (SELECT DISTINCT Model FROM CARS);


SELECT Count(*) AS Make
FROM (SELECT DISTINCT Make FROM CARS);

SELECT Count(*) AS Transmission
FROM (SELECT DISTINCT Transmission FROM CARS);

SELECT Count(*) AS Color
FROM (SELECT DISTINCT Color FROM CARS);

SELECT Count(*) AS City
FROM (SELECT DISTINCT City FROM CARS);

SELECT * FROM CARS
WHERE City='Cairo';

SELECT * FROM CARS
WHERE Fuel='Electric';

SELECT * FROM CARS
WHERE Fuel='diesel';


SELECT * FROM CARS
WHERE Make='Toyota' AND City='Cairo' and Color ='White' and Transmission='manual';

SELECT * FROM CARS
WHERE model='Lanos' AND City='Cairo' and Color ='White' and Transmission='manual';



SELECT * FROM CARS
WHERE City='Cairo' OR City='6 October';


SELECT * FROM CARS
ORDER BY City DESC;


SELECT * FROM CARS
ORDER BY Model ASC, KM DESC;

SELECT Make, City, Model
FROM cars
WHERE Model IS NULL;

SELECT COUNT(Fuel)
FROM CARS;
SELECT AVG(Price)
FROM CARS;



SELECT SUM(Model)
FROM CARS;



SELECT * FROM CARS
WHERE Price BETWEEN 10000 AND 200000;