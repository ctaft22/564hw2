SELECT count(DISTINCT Categories.category)
FROM Categories
JOIN Bids ON Categories.itemID = Bids.itemID
WHERE Bids.bidAmount > 100