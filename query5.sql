SELECT COUNT(DISTINCT sellerID)
FROM Items
JOIN Users on Items.sellerID = Users.userID
WHERE Users.rating > 1000