#!/usr/bin/env python
#-*- coding:utf-8 -*-


""" 
SYNTAX
$python3 c_purchases.py {number_records}

OUTPUT
Two file will be generated into the /out folder : 'orders.csv' and 'purchases.csv'

CONFIG & CUSTOMIZATION
You can customize product names using the productname() def below
"""


#import sys
import random
import time
import string
import datetime
from wizardry import stack  # type: ignore
#from datetime import timedelta



# ORDERS
# start from the user_id list including the created_timestamp


#Import USERS : read the array excluding the header column row
file_users = "./in/userid.csv"
users = [line.strip() for line in open(file_users,"r")]
list_users = ([])
for user in users[1:]:
    elements = user.split(',')
    list_users.append([elements[0],elements[1]])

#Import PRODUCTS : excluding the header, read the array from the 2nd element onwards
file_products = "./in/products.csv"
products = [line.strip() for line in open(file_products,"r")]
list_products = ([])
for product in products[1:]:
    elements = product.split(',')
    list_products.append([elements[0],elements[3]])



#Export - CSV

timestamp = time.strftime("%m%d%H%M")
file_purchases_path = "./out/purchases.csv"
purchases = open(file_purchases_path,"w+")
purchases.write("purchase_date,userid,orderid,productid,price,num_articles,purchase_timestamp\n")

#orders aggregates quantites and total_sum from purchases
file_orders_path = "./out/orders.csv"
orders = open(file_orders_path,"w+")
orders.write("purchase_date,oid,userid,totalsum,articles_quantity,purchase_timestamp\n")

#purchases count = number of users * multiplier
num_multiplier_default = 5
num_purchases = len(list_users) * num_multiplier_default
if num_purchases > 1200000:
    num_purchases = 1200000

#START purchases
rows=0
for i in range(num_purchases):    

    # select a USER, get USERid and the user creation date
    user_choice = random.choice(list_users)
    uid = user_choice[0]
    creation_date = user_choice[1]
    
    # purchase date -- calculate random date
    todays_date = time.strftime("%m/%d/%Y %I:%M")
    purchase_date = stack.randomDate(creation_date, todays_date, random.random())
    purchase_timestamp = round(time.mktime(datetime.datetime.strptime(purchase_date, "%m/%d/%Y %I:%M").timetuple()))

    
    # order ID
    oid = stack.randomString()
    products = random.randrange(1,3)
    rows+=products
    totalsum = 0
    totalquantity = 0
    
    # -- record the purchase and the order    
    for j in range(products):
        # product
        product_choice = random.choice(list_products)
        product_id = product_choice[0]
        product_price = product_choice[1]
        product_quantity = random.randrange(1,4)

        purchases.write(purchase_date+","+str(uid)+","+oid+","+str(product_id)+","+str(product_price)+","+str(product_quantity)+","+str(purchase_timestamp)+"\n")        
        totalsum = totalsum +(float(product_price)*product_quantity)
        totalquantity = totalquantity + product_quantity
    orders.write(str(purchase_date)+","+str(oid)+","+str(uid)+","+str("{:.2f}".format(totalsum))+","+str(totalquantity)+","+str(purchase_timestamp)+"\n")

purchases.close()
orders.close()
print("\n***\n***")
print(str(rows)+" products purchased records in the /out folder")
print("***\n***")
    

        
