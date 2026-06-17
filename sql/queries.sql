-- Total Sales
SELECT SUM(Sales)
FROM superstore;

-- Total Profit
SELECT SUM(Profit)
FROM superstore;

-- Sales By Category
SELECT Category,
SUM(Sales)
FROM superstore
GROUP BY Category;

-- Profit By Region
SELECT Region,
SUM(Profit)
FROM superstore
GROUP BY Region;

-- Top 10 Products
SELECT Product_Name,
SUM(Sales)
FROM superstore
GROUP BY Product_Name
ORDER BY SUM(Sales) DESC
LIMIT 10;