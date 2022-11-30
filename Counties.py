counties_dict = {"Arapahoe":422829, "Denver":463353, "Jefferson":432438}

voting_data = [{"county":"Arapahoe", "registered_voters": 422829}, {"county":"Denver", "registered_voters":463353}, {"county":"Jefferson", "registered_voters":432438}]

#Print each dictionary in voting data
for county_dict in voting_data:
    print (county_dict)

#Use range to iterate over the list of dictionaries and print counties in voting data 
for i in range(len(voting_data)):
    print (voting_data[i]['county'])

#Retrieve only values from each dictionary 
for county_dict in voting_data:
    for value in county_dict.values():
        print(value)

#Retrieve number of registered voters from each dictionary 
for county_dict in voting_data:
    print (county_dict['registered_voters'])

# Only print county name for each dictionary 
for county_dict in voting_data:
    print(county_dict['county'])
