"""
Author:  Paul Lorenz III
Date: July 12, 2023
Description: Updating the data from collection using pymongo. 

"""

##Used the import statement to import MongoClient from MongoDB Atlas and linked the url to establish the MongoDB Client connection.
from pymongo import MongoClient
url = "mongodb+srv://admin:admin@cluster0.bcg6ygj.mongodb.net/?retryWrites=true&w=majority"
client = MongoClient(url)

##Linked up the "pytech" database and the "students" collection that resides in the pytech database.
db = client["pytech"]
mydata = db["students"]

##Executed the output statement to inform the user of the type of action that will get performed by the program. 
print("-- DISPLAYING STUDENTS DOCUMENTS FROM find() QUERY --")

##Executed the find() method to display all student documents in the collection of the database.
All_data = mydata.find({},{"student_id":1, "first_name":1,"last_name":1})

##Executed a for loop to output the results of all the student documents that come from the collection of the database.
for x in All_data: 
    print("Student ID :", x['student_id'])
    print("First_Name :", x['first_name'])
    print("Last_Name :" , x['last_name'])
    print()

##Executed the output statement to inform the user of the type of action that will get performed by the program.
print("-- DISPLAYING STUDENT DOCUMENT 1007 --")

##Executed the update_one method to update the student document that contains a student id of 1007.
filter_value = {"student_id" : 1007}

new_value = {"$set": {"last_name" : "Castillo"}}

result = mydata.update_one(filter_value, new_value)


##Executed the find_one method to find one student document that resides in the collection of the database.
x_data = mydata.find_one({"student_id":1007})

##Assigned variables to retrieve the information that goes along with one student document that is in the collection of the database.
student_id = x_data["student_id"]
first_name = x_data["first_name"]
last_name = x_data["last_name"]

##Executed the output statements to display the information that goes along with the student document that was found in the collection of the database. 
print("Student ID:", student_id)
print("First Name:", first_name)
print("Last Name:", last_name)

input("End of program, press any key to continue...")