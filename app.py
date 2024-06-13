#docstring- Murtaza Shafiyee- shoes database application
#imports
import sqlite3

#constants and variables
DATABASE = "assesment.db"

def print_data():
    mode = input("select which table you would like to view:\n(1) shoes \n(2) brands \n(3) price")
    if mode == "1":
        db = sqlite3.connect(DATABASE)
        cursor = db.cursor()
        sql = "SELECT * FROM shoes;"
        cursor.execute(sql)
        results = cursor.fetchall()
        print(f"{'shoes'[1]:<40} {'shoes'[2]:<40} {'shoes'[3]:<50}")
        for shoes in results:
            print(f"{shoes[1]:<40} {shoes[2]:<40} {shoes[3]:<50}")
        db.close()
    elif mode == "2":
        db = sqlite3.connect(DATABASE)
        cursor = db.cursor()
        sql = "SELECT * FROM brand;"
        cursor.execute(sql)
        results = cursor.fetchall()
        print(f"{'brand':<40}")
        for shoes in results:
            print(f"{brand[1]:<40}")
        db.close()
    elif mode == "3":
        db = sqlite3.connect(DATABASE)
        cursor = db.cursor()
        sql = "SELECT * FROM gender;"
        cursor.execute(sql)
        results = cursor.fetchall()
        print(f"{'gender':<40}")
        for shoes in results:
            print(f"{gender[1]:<40}")
    elif mode == "4":
        join_data()
    elif mode == "5":
        extra_option()
    else:
        print("that is not the code for one of the operations")

def add_data():
    mode = input("select which table you would like to add to:\n(1) shoes \n(2) brand \n(3) gender")
    if mode == "1":
        shoe_name = input("enter the name of a new shoe\n")
        price = input("enter the price of that shoe\n")
        shoe_material = input("enter the material of that shoe\n")
        print_brand()
        brand_id = int(input("enter the id of the brand that made this shoe\n"))
        db = sqlite3.connect(DATABASE)
        sql = "INSERT INTO shoes (shoe_name,price, shoe_material, brand_id) VALUES (?,?,?,?);"
        cursor.execute(sql,(shoe_name,price, shoe_material, brand_id))
        db.commit()
        db.close
    
    elif mode == "2":
        brand_name = input("enter the name of a shoe\n")
        db = sqlite3.connect(DATABASE)
        cursor = db.cursor()
        sql = "INSERT INTO shoes (shoes) VALUES (?);"
        cursor.execute(sql,(shoe_name,))

    elif mode == "3":
        brand = input("enter the name of a brand\n")
        brand_description = input("enter the description of that brand\n")
        db = sqlite3.connect(DATABASE)
        sql = "INSERT INTO brand (brand,defintion) VALUES (?,?);"  
        cursor.execute(sql,(brand, brand_description))     
        db.commit()
        db.close
    elif mode == "4":
        print_shoes()
        shoe




#functions
def print_all_shoes():
    '''print all the shoes nicely'''
    db = sqlite3.connect(DATABASE)
    cursor = db.cursor()
    sql = "SELECT price, shoe_name, brand_name, shoe_material, gender_name FROM shoes JOIN brand ON shoes.brand_id = brand.brand_id JOIN gender ON shoes.gender_id = gender.gender_id;"
    cursor.execute(sql)
    results = cursor.fetchall()
    #loop through all the results
    print(f"price         shoe_name                     brand_id           shoe_material                                 gender_id")
    for shoes in results:
        print(f"{shoes[0]:<10}{shoes[1]:<35}{shoes[2]:<20}{shoes[3]:<45}{shoes[4]:<6}")
    #loop finished here
    db.close()

def print_all_shoes_ascending():
    '''print all the shoes ascending in price'''
    db = sqlite3.connect(DATABASE)
    cursor = db.cursor()
    sql = "SELECT price, shoe_name, brand_name, shoe_material, gender_name FROM shoes JOIN brand ON shoes.brand_id = brand.brand_id JOIN gender ON shoes.gender_id = gender.gender_id ORDER BY price ASC;"
    cursor.execute(sql)
    results = cursor.fetchall()
    #loop through all the results
    print(f"price      shoe_name                        brand_id           shoe_material                                 gender_id")
    for shoes in results:
        print(f"{shoes[0]:<10}{shoes[1]:<35}{shoes[2]:<20}{shoes[3]:<45}{shoes[4]:<6}")
    #loop finished here
    db.close()

def print_shoe_price_and_material():
    '''print all the shoes with their price and material'''
    db = sqlite3.connect(DATABASE)
    cursor = db.cursor()
    sql = "SELECT price, shoe_name, shoe_material FROM shoes;"
    cursor.execute(sql)
    results = cursor.fetchall()
    #loop through all the results
    print(f"price         shoe_name                    shoe_material                  ")
    for shoes in results:
        print(f"{shoes[0]:<10}{shoes[1]:<35}{shoes[2]:<45}")
    #loop finished here
    db.close()

def print_everything():
    '''print all of the information'''
    db = sqlite3.connect(DATABASE)
    cursor = db.cursor()
    sql = "SELECT * FROM shoes;"
    cursor.execute(sql)
    results = cursor.fetchall()
    #loop through all the results
    print(f"id        price           shoe_name                        brand_id             shoe_material                                   gender_id")
    for shoes in results:
        print(f"{shoes[0]:<10}{shoes[1]:<12}{shoes[2]:<40}{shoes[3]:<20}{shoes[4]:<50}{shoes[5]:<50}")
    #loop finished here
    db.close()

#main code loop
while True:
    user_input = input(
"""      
What would you like to do?
1. Print all shoes and information
2. Print all shoes ascending in price
3. Print all shoes and their price and material
4. Print everything
5. Cat
6. Exit
""")
    if user_input == "1":
        print_all_shoes()
    elif user_input == "2":
        print_all_shoes_ascending()
    elif user_input == "3":
        print_shoe_price_and_material()
    elif user_input == "4":
        print_everything()
    elif user_input == "5":
        print(
"""
            *     ,MMM8&&&.            *
                  MMMM88&&&&&    .
                 MMMM88&&&&&&&
     *           MMM88&&&&&&&&
                 MMM88&&&&&&&&
                 'MMM88&&&&&&'
                   'MMM8&&&'      *    
          |\___/|     /\___/|
          )     (     )    ~( .              '
         =\     /=   =\~    /=
           )===(       ) ~ (
          /     \     /     |
          |     |     ) ~   (
         /       \   /     ~ |
         \       /   \~     ~/
  jgs_/\_/\__  _/_/\_/\__~__/_/\_/\_/\_/\_/\_
  |  |  |  |( (  |  |  | ))  |  |  |  |  |  |
  |  |  |  | ) ) |  |  |//|  |  |  |  |  |  |
  |  |  |  |(_(  |  |  (( |  |  |  |  |  |  |
  |  |  |  |  |  |  |  |\)|  |  |  |  |  |  |
  |  |  |  |  |  |  |  |  |  |  |  |  |  |  |
""")
    elif user_input == "6":
        break
    else:
        print("That was not an option\n")
    #if its 4

    #if its' x: exit


#etc


#print_all_shoes()