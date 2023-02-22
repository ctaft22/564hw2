drop TABLE if exists Items;
drop TABLE if exists Categories;
drop TABLE if exists Users;
drop TABLE if exists Bids;

CREATE TABLE Items(
    itemID INTEGER PRIMARY KEY,
    itemName TEXT,
    currently Float,
    buyPrice FLOAT,
    firstBid FLOAT,
    numBid INTEGER, 
    startDate TEXT,
    endDate TEXT,
    description TEXT,
    sellerID INTEGER
);
CREATE TABLE BIDS(
    userID TEXT,
    bidTime TEXT,
    bidAmount FLOAT
);
CREATE TABLE Users(
    userID TEXT ,
    rating INTEGER, 
    location TEXT,
    country TEXT
);
CREATE TABLE Categories(
    itemID INTEGER,
    category Float
);

