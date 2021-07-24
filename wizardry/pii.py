from json import dumps
import random
from random import choice
from random import randrange

def email_gen(first,last):
        email_domains = ["gmail.com","live.com","facebook.com","xyz.com","yahoo.com","icloud.com","hotmail.com",
        "free.com","outlook.com","aol.com","mail.com","zoho.com","gmx.com","yandex.com","memail.com"]
        emailprovider = choice(email_domains)
        randomchoice = random.randint(1,24)
        if randomchoice%2==0 and randomchoice%3==0:
            emailaddress = first[0]+last+"@"+emailprovider
        elif(randomchoice%2==0):
            emailaddress = first+last[0]+"@"+emailprovider
        elif(randomchoice%3==0):
            emailaddress = first+"."+last+"@"+emailprovider
        else:
            emailaddress = first[0:2]+last+"@"+emailprovider
        
        return emailaddress

def geoLocations():
    cities = [line.strip() for line in open("./in/cities.txt","r")]
    list_cities = ([])
    for value in cities:
        location = value.split(',')
        #city,country,state,region,lat,long
        list_cities.append([location[0],location[1],location[2],location[3],location[4],location[5]])
    return list_cities


def male_firstname():
    list_guys = [line.strip() for line in open("./in/firstman.txt","r")]
    return choice(list_guys)

def female_firstname():
    list_girlz = [line.strip() for line in open("./in/firstwoman.txt","r")]
    return choice(list_girlz)

def lastname():
    list_surnames = [line.strip() for line in open("./in/lastnames.txt","r")]
    return choice(list_surnames)


"""
#Purpose : Generate a new random position from a starting lat-long point. 
Coordinates from cities.txt typically start in the  city center.
#Config : tweaking the divider below will increase or decrease the radius around the starting point. 
The current setting yields 2 decimals (0.0x) change on coordinates which corresponds to ~1km radius.
#Caveat : there is no check against ending in the water. This might come later with help from https://onwater.io/
"""
def randomlatlong(lat,long):

    dec_lat = random.randrange(-10000000,10000000, 7)/1000000000
    dec_long = random.randrange(-10000000,10000000, 7)/1000000000
    new_lat = float(lat)+dec_lat
    new_long = float(long)+dec_long
    return (new_lat,new_long)

