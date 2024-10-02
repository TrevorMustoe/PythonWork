from buildings import Building
from city import City
import datetime

def construct():
    date_constucted = datetime.datetime.now()
    return(date_constucted.strftime("%b %d, %Y"))
  
def purchase(name):
    owner = "This was bought by:" + " " + name
    return(owner)

building_1 = Building('Devon Bristol Shaw Mustoe', construct(), purchase("Trevor"), '2342 East 14th St Brooklyn, NY', 'test stories1')
building_2 = Building('John Cena', construct(), purchase("Trevor"), '25 North 4th St Miami', 'test stories2')
building_3 = Building('New Guy', construct(), purchase("Elen"), '42 East 1st St, Miami', 'test stories3')
building_4 = Building('Geff', construct(), purchase("Forshien"), '34 East St Miami', 'test stories4')
building_5 = Building('JEff', construct(), purchase("Cory"), '2342 East 14th St Brooklyn, NY', 'test stories5')

city1 = City('Miami')
city2 = City('St.pete')
city3 = City('Tampa')

city1.buildingList.append(building_1)
city1.buildingList.append(building_2)
city1.buildingList.append(building_3)

#print(f'Building 1:',building_1.date_constructed, building_1.designer, building_1.owner, building_1.address, building_1.stories)
#print(f'Building 2:',building_2.date_constructed, building_2.designer, building_2.owner, building_2.address, building_2.stories)
#print(f'Building 3:',building_3.date_constructed, building_3.designer, building_3.owner, building_3.address, building_3.stories)
#print(f'Building 4:',building_4.date_constructed, building_4.designer, building_4.owner, building_4.address, building_4.stories)
#print(f'Building 5:',building_5.date_constructed, building_5.designer, building_5.owner, building_5.address, building_5.stories)
#print(f'City Name Test:', city1.city_name)

for buildings_new in city1.buildingList:
  print(f'Building Address: {buildings_new.address}')
