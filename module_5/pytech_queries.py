from pymongo import MongoClient
url = "mongodb+srv://admin:admin@cluster0.bcg6ygj.mongodb.net/?retryWrites=true&w=majority"
client = MongoClient(url)


db = client["pytech"]
mydata= db["students"] 

print("-- DISPLAYING STUDENTS DOCUMENTS FROM find() QUERY --")

All_data = mydata.find({},{"student_id":1, "first_name":1,"last_name":1})

for x in All_data: 
    print("Student ID :", x['student_id'])
    print("First_Name :", x['first_name'])
    print("Last_Name :" , x['last_name'])
    print()

print("-- DISPLAYING STUDENT DOCUMENT FROM find_one() QUERY --")


x_data = mydata.find_one({"student_id":1008})

if x_data:
    student_id = x_data["student_id"]
    first_name = x_data["first_name"]
    last_name = x_data["last_name"]

    print("Student ID:", student_id)
    print("First Name:", first_name)
    print("Last Name:", last_name)
input("End of program, press any key to continue...")