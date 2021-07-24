#!/usr/bin/env python
#-*- coding:utf-8 -*-

#!! OUTPUTS a file 'products.csv' in the /rsc folder

""" 
SYNTAX
$python3 b_products.py {number_records}

OUTPUT
One file will be generated into the /in folder "products.csv" for reuse, eg : 

CONFIG & CUSTOMIZATION
You can customize product names using the productname() def below
"""

def main():

    import sys
    import random
    from random import choice
    from random import randrange

    # Number of products created for each price category
    # calculated as items_num_price_category * num_records (default 100)
    number_records_default  = 100
    if (len(sys.argv)==2):
        number_records = sys.argv[1]
    else:
        number_records = number_records_default


    def productname():
        liste_adj = ["big","small","little","huge","good","wicked","easy","cool",
                    "marvelous","amazing","fabulous","fantastic","astonishing","astounding","surprising",
                    "delightful","great","stunning","bewildering","extraordinaire","excellent","superb",
                    "lovely","precious","cute","kawai","sublime","divine"]
        
        list_colors = ["white","black","red","blue","green","yellow","maroon","orange","pink","grey","lilac","beige","violet"]
        
        list_obj = ["device","widget","object","thingie","stuff","appliance","tool","artefact","solution",
                    "gadget","instrument","gizmo","machine","contraption","phenomenon","bit","unit","shtuff"]
        
        list_syllables = ["ba","bo","bro","bra","bi","do","da","di","fa","fi","fo","ga","go","ha","hi","ho"
                        ,"la","lo","li","ma","mo","mi","na","no","ni","pa","po","pi","ra","ri","ro","ta","ti","to"
                        ,"za","zo","zi","xi","xa","nu","ru","qi","ka","ko","ku","shu","shi","sha","bha","phi"]
        syllables = random.sample(list_syllables,4)
        
        productname = "".join(syllables).capitalize()+","
        productname += random.choice(list_colors).capitalize()+" "
        productname += random.choice(liste_adj).capitalize()+random.choice(liste_adj).capitalize()+" "
        productname += random.choice(list_obj).capitalize()

        return productname
        

    list_cheap = ['Baby Products', 'Beauty','Books','Cell Phones Accessories','Grocery & Gourmet Food', 'Health and Personal Care','Music','Office Products','Pet Supplies','Video Content','Toys and Games', 'Video Games','Watches']

    list_medium = ['Cell Phones','Home and Garden','Outdoors','Software','Tools and Home Improvement','Toys and Games']

    list_expensive = ['Automotive','Powersports','Camera and Photo','Consumer Electronics','Major Appliances','Musical Instruments','Outdoors','Personal Computers']





    # CSV GENERATOR -- Start
    #timestamp = time.strftime("%m%d%H%M")
    f = open("./in/products.csv","w+")
    f.write("product_id,brand,product_name,price,category\n") 

    k=1
    for cat in list_cheap:
        for i in range(number_records_default):
            product_id = 10000000+k
            product_name = productname()
            pname = product_name.split(',')
            cents = [0.05,0.10,0.20,0.50,0.99,0.95]
            price = round(random.randrange(4,30)+random.choice(cents),2)
            category = cat
            # -- write line to the file
            f.write(str(product_id)+","+pname[0]+","+pname[1]+","+str("{:.2f}".format(price))+","+category+"\n")
            k+=1
    k+=50


    k+=1
    for cat in list_medium:
        
        for j in range(number_records_default):
            product_id = 10000000+k
            product_name = productname()
            pname = product_name.split(',')        
            cents = [0.05,0.10,0.20,0.50,0.99,0.95]
            price = round(random.randrange(30,80)+random.choice(cents),2)
            category = cat
            # -- write line to the file
            f.write(str(product_id)+","+pname[0]+","+pname[1]+","+str("{:.2f}".format(price))+","+category+"\n")
            k+=1


    k+=1
    for cat in list_expensive:
        
        for j in range(number_records_default):
            product_id = 10000000+k
            product_name = productname()
            pname = product_name.split(',')        
            cents = [0.05,0.10,0.20,0.50,0.99,0.95]
            price = round(random.randrange(80,600)+random.choice(cents),2)
            category = cat
            # -- write line to the file
            f.write(str(product_id)+","+pname[0]+","+pname[1]+","+str("{:.2f}".format(price))+","+category+"\n")
            k+=1        
            
    f.close()


    print("\n***\n***")
    print(str(k)+" rows created")
    print("***\n***")
    

if __name__ == "__main__":
    main()        
