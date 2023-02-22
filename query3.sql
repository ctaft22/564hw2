SELECT count(*) 
FROM Categories
WHERE count(category) > 4
GROUP BY itemID