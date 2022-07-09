# Real Estate

# For example:
# There are 3 houses on Sale
# Downtown Condo Rent $2000 per month 2020yr
# Midtown Townhouse Pre-Construction $1.5M 2025yr
# Uptown House Resale $1.3M 2010yr

class House:
    def __init__(self, location, house_type, deal_type, price, completion_year):
        self.location = location
        self.house_type = house_type
        self.deal_type = deal_type
        self.price = price
        self.completion_year = completion_year 


    def show_detail(self):
        print(self.location, self.house_type, self.deal_type, self.price, self.completion_year)


houses = []
house1 = House("Downtown", "Condo", "Rent", "$2,000 per month", "Built in 2020")
house2 = House("Midtown", "Townhouse", "Pre-Construction", "$1.5M", "Built in 2025")
house3 = House("Uptown", "Uptown", "Resale", "$1.3M", "Built in 2010")
houses.append(house1)
houses.append(house2)
houses.append(house3)

print("There are {0} houses on Sale now".format(len(houses)))
for house in houses:
    house.show_detail()