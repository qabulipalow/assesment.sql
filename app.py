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
        print(f"price          name     material    id    brand   gender   ")
        for shoes in results:
            print(f"{'shoes'[1]:<40} {'shoes'[2]:<40} {'shoes'[3]:<50}{'shoes'[4]:<50}{'shoes'[5]:<50}{'shoes'[6]:<50}")
        db.close()
    elif mode == "2":
        db = sqlite3.connect(DATABASE)
        cursor = db.cursor()
        sql = "SELECT * FROM brand;"
        cursor.execute(sql)
        results = cursor.fetchall()
        print(f"price          name     material    id    brand   gender   ")
        for shoes in results:
            print(f"{brand[1]:<40}")
        db.close()
    elif mode == "3":
        db = sqlite3.connect(DATABASE)
        cursor = db.cursor()
        sql = "SELECT * FROM gender;"
        cursor.execute(sql)
        results = cursor.fetchall()
        print(f"price          name     material    id    brand   gender   ")
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


while True:
    print("Welcome to my shoe database")
    operation = input(
'''
what would you like to do: \n(1) look at shoes\n(2) add shoes\n(3) exit
''')
    try:
        if operation == "1":
            print_data()
        elif operation == "2":
            add_data()
        elif operation == "3":
            break
    except:
        print("please write the operation you want")
        