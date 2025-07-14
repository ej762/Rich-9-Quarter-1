student={}

studentName= input("Enter your student's name: ")
student ["Name"] = studentName




Studentage= input("How old are you")
student ["Age"] = Studentage


hobbies=[]
hobby = input("Enter your student's hobby; Type 'done' when done:").lower()
hobbies.append(hobby)

while hobby != "done":
 hobby = input("Enter your student's hobby; Type 'done' when done:").lower()
hobbies.append(hobby)

student["Hobbies"]=hobbies

print(student)



