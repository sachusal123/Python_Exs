class student:

   def get_data(self,roll_no,stud_name,mark):
       self.roll_no=roll_no
       self.stud_name=stud_name
       self.mark=mark

   def print_data(self):
       sum_mark=0
       print("Roll No of student=",self.roll_no)
       print("Name of Student=",self.stud_name)
       print("Marks of six subjects=",self.mark)
       for i in self.mark:
           sum_mark=sum_mark+i
       percentage_mark=(sum_mark/600)*100
       print("Sum of total marks=",sum_mark)
       print("Percentage of total mark=",percentage_mark)

class marks(student):

    def input_data(self,roll_no,stud_name,mark):
        student.get_data()

    def out_data(self,roll_no,stud_name,mark):
        student.print_data()



mark=[]
i=0
roll_no=int(input("Enter roll no of student:"))
stud_name=input("Enter Name of Student:")
print("Enter mark of 6 subjects")

while i<6:
    mk=int(input("Enter mark:"))
    mark.append(mk)
    i=i+1

print(mark)

ob=student()
ob.get_data(roll_no,stud_name,mark)
ob.print_data()