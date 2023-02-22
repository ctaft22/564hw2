SELECT count(DISTINCT Items.sellerID)
FROM Items, Bids
WHERE Items.sellerID = Bids.userID