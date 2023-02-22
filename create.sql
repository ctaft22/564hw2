drop TABLE if exists Items;
drop TABLE if exists Categories;
drop TABLE if exists Users;
drop TABLE if exists Bids;

CREATE TABLE Items(
    itemID INTEGER PRIMARY KEY,
    itemName TEXT,
    currently TEXT,
    buyPrice FLOAT,
    firstBid FLOAT,
    numBid INTEGER, 
    startDate TEXT,
    endDate TEXT,
    description TEXT,
    sellerID INTEGER
);

CREATE TABLE Categories (
    item_ID INTEGER, 
    category TEXT,
);

CREATE TABLE Users(
     userID TEXT PRIMARY KEY,
     rating INTEGER, 
     location TEXT,
     country TEXT,
);
