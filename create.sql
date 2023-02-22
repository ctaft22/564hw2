-- drop table if exists Items
drop table if exists categories;
-- drop table if exists Users
-- drop table if exists Bids

-- create table Items(
--     itemID int,
--     itemName Char(max),
--     currently Char(max),
--     buyPrice Float,
--     numBid int, 
--     startDate Datetime,
--     endDate Datetime,
--     description Char(max),
--     sellerID int
-- );

CREATE TABLE categories (
    item_ID INTEGER PRIMARY KEY, 
    category TEXT,
);

-- create table Users(
--     userID Char(max),
--     rating int, 
--     location Char(max),
--     country Char(max),
-- );
