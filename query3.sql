SELECT count(*)
FROM(
SELECT count(*)
FROM Categories
GROUP BY itemID
HAVING count(*) = 4
)