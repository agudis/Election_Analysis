counties = ["Arapahoe", "Denver", "Jefferson"]

if "Arapahoe" in counties or "El Paso" in counties:

    print('Arapahoe or El Paso is in the list of counties.')

else: 

    print('Arapahoe or El Paso is not in the list of counties.')

for county in counties:
    print(county)

counties_dict = {"Arapahoe" : 422829, "Denver" : 463353, "Jefferson":432438}

for county, voters in counties_dict.items():
    print(f"{county} county has {voters:,} registered voters.")

voting_data = [{"county":"Arapahoe", "registered_voters": 422829}, {"county":"Denver", "registered_voters":463353}, {"county":"Jefferson", "registered_voters":432438}]

for counties_dict in voting_data:
    print(f"{county} county has {voters:,} registered voters.")
