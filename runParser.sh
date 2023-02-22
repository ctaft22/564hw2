python my_parser.py ebay_data/items-*.json
sort dups_users.dat | uniq > users.dat
sort dups_categories.dat | uniq > categories.dat 
sort dups_bids.dat | uniq > bids.dat
sort dups_items.dat | uniq > items.dat 
rm dups_bids.dat dups_categories.dat dups_items.dat dup_users.dat