
"""
FILE: skeleton_parser.py
------------------
Author: Firas Abuzaid (fabuzaid@stanford.edu)
Author: Perth Charernwattanagul (puch@stanford.edu)
Modified: 04/21/2014

Skeleton parser for CS564 programming project 1. Has useful imports and
functions for parsing, including:

1) Directory handling -- the parser takes a list of eBay json files
and opens each file inside of a loop. You just need to fill in the rest.
2) Dollar value conversions -- the json files store dollar value amounts in
a string like $3,453.23 -- we provide a function to convert it to a string
like XXXXX.xx.
3) Date/time conversions -- the json files store dates/ times in the form
Mon-DD-YY HH:MM:SS -- we wrote a function (transformDttm) that converts to the
for YYYY-MM-DD HH:MM:SS, which will sort chronologically in SQL.

Your job is to implement the parseJson function, which is invoked on each file by
the main function. We create the initial Python dictionary object of items for
you; the rest is up to you!
Happy parsing!
"""

import sys
from json import loads
from re import sub

columnSeparator = "|"

# Dictionary of months used for date transformation
MONTHS = {'Jan':'01','Feb':'02','Mar':'03','Apr':'04','May':'05','Jun':'06',\
        'Jul':'07','Aug':'08','Sep':'09','Oct':'10','Nov':'11','Dec':'12'}

"""
Returns true if a file ends in .json
"""
def isJson(f):
    return len(f) > 5 and f[-5:] == '.json'

"""
Converts month to a number, e.g. 'Dec' to '12'
"""
def transformMonth(mon):
    if mon in MONTHS:
        return MONTHS[mon]
    else:
        return mon

"""
Transforms a timestamp from Mon-DD-YY HH:MM:SS to YYYY-MM-DD HH:MM:SS
"""
def transformDttm(dttm):
    dttm = dttm.strip().split(' ')
    dt = dttm[0].split('-')
    date = '20' + dt[2] + '-'
    date += transformMonth(dt[0]) + '-' + dt[1]
    return date + ' ' + dttm[1]

"""
Transform a dollar value amount from a string like $3,453.23 to XXXXX.xx
"""

def transformDollar(money):
    if money == None or len(money) == 0:
        return money
    return sub(r'[^\d.]', '', money)

"""
go through item and organize by item_id, name, currently, buyprice, firstbid, num_bid, started, ends, description, user_id (seller)
"""
def itemsTable(item):
    item_id = item["ItemID"]
    name = item["Name"]
    currently = transformDollar(item["Currently"])
    
    if ("Buy_Price" in item.keys()):
        buyprice = transformDollar(item["Buy_Price"])
    else:
        buyprice = "NULL"
    firstbid = transformDollar(item["First_Bid"])
    num_bid = item["Number_of_Bids"]
    started = transformDttm(item["Started"])
    ends = transformDttm( item["Ends"])
    description = item["Description"]
    if (description == None):
        description = "NULL"
    seller_id = item["Seller"]["UserID"]
    item_parsed = item_id + "|" + name + "|" + currently + "|" + buyprice  + "|" + firstbid + "|" + num_bid + "|" + started + "|" + ends + "|" + description + "|" + seller_id + "\n"

    return item_parsed

"""
go through item and organize by userid categories 
"""
def categoriesTable(item):
    item_id = item["ItemID"]
    categories = item["Category"]
    all_categories = ""
    for i in range(len(categories)):
        all_categories = all_categories + item_id + "|" + categories[i] + "\n"
    return all_categories


"""
go through item and organize by userid time amount 
"""
def bidsTable(item):
    item_id = item["ItemID"]

    pass

"""
go through item and organize by userid location country and rating
"""
def userTable(item):
    seller = item["Seller"]["UserID"]
    s_rating = item["Seller"]["Rating"]
    s_country = item["Country"]
    s_location = item["Location"]
    all_user = seller + "|" + s_rating + "|" + s_location + "|" + s_country + "\n"

    num_bid = int(item["Number_of_Bids"])
    
    if (num_bid == 0) :
        return all_user
    
    for i in range(num_bid):
        buyerinfo = item["Bids"][i]["Bid"]["Bidder"]
        b_id = buyerinfo["UserID"]
        b_rating = buyerinfo["Rating"]
        if ("Location" in buyerinfo.keys()) :
            b_location = buyerinfo["Location"]
        else:
            b_location = "NULL"
        if ("Country" in buyerinfo.keys()):
            b_country = buyerinfo["Country"]
        else:
            b_country = "NULL"
        all_user = all_user + b_id + "|" + b_rating + "|" + b_location + "|" + b_country + "\n"
    return all_user



"""
Parses a single json file. Currently, there's a loop that iterates over each
item in the data set. Your job is to extend this functionality to create all
of the necessary SQL tables for your database.
"""
def parseJson(json_file):
    with open(json_file, 'r') as f:
        categoriesfile = open("categories.dat", "w")
        itemsfile = open("items.dat", "w")
        usersfile = open("users.dat", "w")
        items = loads(f.read())['Items'] # creates a Python dictionary of Items for the supplied json file
        for item in items:
            """
            TODO: traverse the items dictionary to extract information from the
            given `json_file' and generate the necessary .dat files to generate
            the SQL tables based on your relation design
            """

            itemsfile.write(itemsTable(item))
            usersfile.write(userTable(item))
            categoriesfile.write(categoriesTable(item))


            pass
        itemsfile.close()
        usersfile.close()
        categoriesfile.close()

"""
Loops through each json files provided on the command line and passes each file
to the parser
"""
def main(argv):
    if len(argv) < 2:
        print >> sys.stderr, 'Usage: python skeleton_json_parser.py <path to json files>'
        sys.exit(1)
    # loops over all .json files in the argument
    for f in argv[1:]:
        if isJson(f):
            parseJson(f)
            print "Success parsing " + f

if __name__ == '__main__':
    main(sys.argv)
