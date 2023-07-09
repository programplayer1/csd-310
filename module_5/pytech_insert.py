from pymongo import MongoClient
url = "mongodb+srv://admin:admin@cluster0.bcg6ygj.mongodb.net/?retryWrites=true&w=majority"
client = MongoClient(url)


db = client["pytech"]
mydata= db["students"] 

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

result1 = mydata.insert_one(student1)
result2 = mydata.insert_one(student2)
result3 = mydata.insert_one(student3)

print("-- INSERT STATEMENTS --")

print("Inserted student records John Doe into the students collection with document id ", result1.inserted_id)
print("Inserted student records Riley Miller into the students collection with document id ", result2.inserted_id)
print("Inserted student records Wesley White into the students collection with document id ", result3.inserted_id)

input("End of program, press any key to exit...")