marks={}

First_Subject_Marks=int(input("Enter marks of first subject: "))
marks.update({"First Subject": First_Subject_Marks})

Second_Subject_Marks=int(input("Enter marks of second subject: "))
marks.update({"Second Subject": Second_Subject_Marks})

Third_Subject_Marks=int(input("Enter marks of third subject: "))        
marks.update({"Third Subject": Third_Subject_Marks})

print("Marks of 3 subjects are:", marks)