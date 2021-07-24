#!/usr/bin/env python
#-*- coding:utf-8 -*-


""" 
SYNTAX
$python3 a_users.py {number_records}

=> outputs 2 files
    1. 'userid.csv' in the /in folder
    2. 'users.csv' in the /out folder

CONFIG & CUSTOMIZATION
The /in folder contains customizable lists of first names and cities
"""


def main():

    import sys
    import time
    import datetime
    import json
    import random
    from random import choice

    from wizardry import stack
    from wizardry import pii


    CSV_EXPORT = True
    SQL_EXPORT = True
    JSON_EXPORT = True

    # DEFAULT values and number of records
    db_start_year_default = 2014

    number_records_default  = 100
    if (len(sys.argv)==2):
        number_records = sys.argv[1]
    else:
        number_records = number_records_default


    cities_APAC = [x for x in pii.geoLocations() if x[3] == "apac"]
    cities_EUROPE = [x for x in pii.geoLocations() if x[3] == "europe"]
    cities_MEA = [x for x in pii.geoLocations() if x[3] == "mea"]
    cities_LATAM = [x for x in pii.geoLocations() if x[3] == "latam"]
    cities_NORTHAM = [x for x in pii.geoLocations() if x[3] == "northam"]




    if(CSV_EXPORT):
        users_csv_filepath = "./out/users.csv"
        userid_csv_filepath = "./in/userid.csv" #userIds go to the /in folder to be reused by other modules
        users = open(users_csv_filepath,"w+")
        useridlist = open(userid_csv_filepath,"w+")
        users.write("Created_Datetime,FirstName,MiddleName,LastName,DOB,Email,Pwd,Gender,UserID,Geo_City_en,"
                +"Geo_Country_en,Geo_State_en,Created_Timestamp,DOB_timestamp")
        users.write("\n")
        useridlist.write("UserID,Created_Datetime")
        useridlist.write("\n")

    if(SQL_EXPORT):
        create_users_table_sql_path = "./out/table_users.sql"
        insert_users_records_sql_path = "./out/insert_users.sql"
        users_table_sql = open(create_users_table_sql_path,"w+")
        userid_insert_sql = open(insert_users_records_sql_path,"w+")

        userid_sql = """CREATE TABLE users (User_created timestamp NOT NULL,FirstName varchar(64),MiddleName varchar(64),
        LastName varchar(64),DOB datetime,Email varchar(128),Pwd varchar(64),Gender varchar(1),
        UserID smallint PRIMARY KEY NOT NULL AUTO_INCREMENT,Geo_City_en varchar(64),Geo_Country_en varchar(64),Geo_State_en varchar,
        Created_Timestamp timestamp,DOB_Timestamp timestamp);
        """
        users_table_sql.write(userid_sql)
        userid_insert_sql.write("INSERT INTO users VALUES")

    if(JSON_EXPORT):
        create_users_json_path = "./out/users.json"
        users_json_file = open(create_users_json_path,"w+")        
        users_json = {}



    # THIS IS WHERE THE ROW BY ROW GENERATION HAPPENS ################################

    timestamp = time.strftime("%m%d%H%M")
    for i in range(int(number_records)):

        # -- Timestamp Creation
        start_date = "1/1/"+str(db_start_year_default)+" 1:30"
        todays_date = time.strftime("%m/%d/%Y %I:%M")
        usr_created_datetime = stack.randomDate(start_date, todays_date, random.random())    
        usr_created_timestamp = round(time.mktime(datetime.datetime.strptime(usr_created_datetime, "%m/%d/%Y %I:%M").timetuple())) 
        userid = str(int(timestamp)+int(i)+1)
        
        # -- Last Name
        selected_lastname = pii.lastname()


        # -- Gender with weighted bias
        gender = random.choice(["Male","Female","Male","Female","Male","Female","Male","Female","Male","Female","Male",
        "Female","Male","Female","Male","Female","Male","Female","Male","Female","Male","Female","Trans*","Unknown"])
        
        if(gender=="Male"):
            # -- choose a first name
            firstname = pii.male_firstname()
            
            # -- has a middle name or not
            guy_hasmidname = random.randint(1,200)
            if(guy_hasmidname%2==0):
                midname = ""
            else:
                midname = pii.male_firstname()
        
        elif(gender=="Female"):
            # -- choose a first name
            firstname = pii.female_firstname()

            # -- has a middle name or not
            girl_hasmidname = random.randint(1,200)
            if(girl_hasmidname%2==0):
                midname = ""
            else:
                midname = pii.female_firstname()

        else:
            flipcoin = random.randint(1,2000)
            if(flipcoin%2==0):
                firstname = pii.female_firstname()
                x_hasmidname = random.randint(1,200)
                if(x_hasmidname%2==0):
                    midname = ""
                else:
                    midname = pii.female_firstname()

            else:
                firstname = pii.male_firstname()
                x_hasmidname = random.randint(1,200)
                if(x_hasmidname%2==0):
                    midname = ""
                else:
                    midname = pii.female_firstname()

    
        
        dob = stack.randomDOB("1/1/1950", "12/31/2001", random.random())

        #usr_created_datetime = stack.randomDate(start_date, todays_date, random.random())    
        #usr_created_timestamp = round(time.mktime(datetime.datetime.strptime(usr_created_datetime, "%m/%d/%Y %I:%M").timetuple())) 
       


        dob_timestamp = round(time.mktime(datetime.datetime.strptime(dob, "%m/%d/%Y").timetuple()))

        email_address = pii.email_gen(firstname,selected_lastname)     # -- Email address


        """
        Defines a weight to random selection for locations by broad world regions
        Europe 35%, North America 40%, APAC 15%, LATAM 5%, Middle East and Africa 5%
        """ 
        if(i < (int(number_records)*35)/100 ):
            city_choice = choice(cities_EUROPE)
        elif(i < (int(number_records)*75)/100 ):
            city_choice = choice(cities_NORTHAM)
        elif(i < (int(number_records)*90)/100 ):
            city_choice = choice(cities_APAC)
        elif(i < (int(number_records)*95)/100 ):
            city_choice = choice(cities_LATAM) 
        else:
            city_choice = choice(cities_MEA) 



        # -- Password generation with stack.pwd_gen(numCharacters)
        #pwd = stack.pwd_gen(8)
        pwd = ""


        # -- WRITING VALUES TO FILES
        if(CSV_EXPORT):
            users.write(usr_created_datetime+","+firstname+","+midname+","+selected_lastname+","
                        +dob+","+email_address.lower()+","+pwd+","+gender+","
                        +userid+","+city_choice[0]+","+city_choice[1]+","+city_choice[2]+","+str(usr_created_timestamp)+","+str(dob_timestamp)+"\n")  
            useridlist.write(userid+","+usr_created_datetime+"\n")

        if(SQL_EXPORT):
            userid_insert_content = "(\""+usr_created_datetime+"','"+firstname+"','"+midname+"','"+selected_lastname+"','"+dob+"','"+email_address.lower()+"','"+pwd+"','"+gender+"','"+userid+"','"+city_choice[0]+"','"+city_choice[1]+"','"+city_choice[2]+"','"+str(usr_created_timestamp)+"','"+str(dob_timestamp)+"\""
            userid_insert_sql.write(userid_insert_content)
            if(int(i)+1 == int(number_records)):
                userid_insert_sql.write(")\n")
            else:
                userid_insert_sql.write("),\n")

        if(JSON_EXPORT):
            users_json[i+1] = {
                "Created_Datetime":usr_created_datetime,
                "FirstName":firstname,
                "MiddleName":midname,
                "LastName":selected_lastname,
                "DOB":dob,
                "Email":email_address.lower(),
                "Pwd":pwd,
                "Gender":gender,
                "UserID":userid,
                "Geo_City_en":city_choice[0],
                "Geo_Country_en":city_choice[1],
                "Geo_State_en":city_choice[2],
                "Created_Timestamp":str(usr_created_timestamp),
                "DOB_timestamp":str(dob_timestamp)
            }


    #close files
    if(CSV_EXPORT):
        users.close()
        useridlist.close()

    if(SQL_EXPORT):
        userid_insert_sql.write(";")

    if(JSON_EXPORT):
        json_dump = json.dumps(users_json) # string
        #print(json_dump)
        #json_object = json.loads(json_dump) # dictionary
        users_json_file.write(json_dump) 


    print("\n***\n***")
    print(str(number_records)+ " created in the ./out directory")
    print("***\n***")

if __name__ == "__main__":
    main()