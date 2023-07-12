##Used the import statement to import MongoClient from MongoDB Atlas and linked the url to establish the MongoDB Client connection.
from pymongo import MongoClient
url = "mongodb+srv://admin:admin@cluster0.bcg6ygj.mongodb.net/?retryWrites=true&w=majority"
client = MongoClient(url)

##Linked up the "pytech" database and the "students" collection that resides in the pytech database.  
db = client["pytech"]
mydata = db["students"] 

##Assigned variables to create each student document in the "students" collection of the pytech database.
student1 = {
    "student_id" :1007,
    "first_name":"John",
    "last_name":"Doe"
}

student2 = {
    "student_id": 1008,
    "first_name": "Riley",
    "last_name": "Miller"
}

student3 = {
    "student_id": 1009,
    "first_name": "Wesley",
    "last_name": "White"
}

##Executed the insert_one() method for each student document. 
result1 = mydata.insert_one(student1)
result2 = mydata.insert_one(student2)
result3 = mydata.insert_one(student3)

##Executed the output statement to inform the user of the type of action that will get performed by the program. 
print("-- INSERT STATEMENTS --")

##Executed the output statements to demonstrates each action that was taken to insert each "student" document into the "students" collection of the "pytech" database. 
print("Inserted student records John Doe into the students collection with document id ", result1.inserted_id)
print("Inserted student records Riley Miller into the students collection with document id ", result2.inserted_id)
print("Inserted student records Wesley White into the students collection with document id ", result3.inserted_id)

##Executed the input function to end the program.
input("End of program, press any key to exit...")