##Used the import statement to import MongoClient from MongoDB Atlas and linked the url to establish the MongoDB Client connection.
from pymongo import MongoClient
url = "mongodb+srv://admin:admin@cluster0.bcg6ygj.mongodb.net/?retryWrites=true&w=majority"
client = MongoClient(url)

##Linked up the "pytech" database and the "students" collection that resides in the pytech database.
db = client["pytech"]
mydata= db["students"]

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
print("-- DISPLAYING STUDENT DOCUMENT FROM find_one() QUERY --")

##Executed the find_one method to find one student document that resides in the collection of the database.
x_data = mydata.find_one({"student_id":1007})