"""
Author:  Paul Lorenz III
Date: July 12, 2023
Description: Inserting and deleteing the data from collection  using pymongo 

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

insert_student_document1 = {
    "student_id": 1010,
    "first_name": "Russel",
    "last_name" : "Granger"
}

student_result = mydata.insert_one(insert_student_document1)

print("-- INSERT STATEMENTS --")

print("Inserted student record Russel Granger into the students collection with document id",  student_result.inserted_id)

print("f\n-- DISPLAYING STUDENT TEST DOC --")

##Executed the find_one method to find one student document that resides in the collection of the database.
x_data = mydata.find_one({"student_id":1010})

##Executed an if statement to retrieve the information that goes along with one student document that is in the collection of the database.
student_id = x_data["student_id"]
first_name = x_data["first_name"]
last_name = x_data["last_name"]

##Executed the output statements to display the information that goes along with the student document that was found in the collection of the database. 
print("Student ID:", student_id)
print("First Name:", first_name)
print("Last Name:", last_name)


DeleteQuery = {"student_id":1010}

mydata.delete_one(DeleteQuery)



##Executed the find() method to display all student documents in the collection of the database.
All_data = mydata.find({},{"student_id":1, "first_name":1,"last_name":1})

##Executed a for loop to output the results of all the student documents that come from the collection of the database.
for x in All_data: 
    print("Student ID :", x['student_id'])
    print("First_Name :", x['first_name'])
    print("Last_Name :" , x['last_name'])
    print()

input("End of program, press any key to continue...")