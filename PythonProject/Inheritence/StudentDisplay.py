from Inheritence.StudentResult import StudentResult


class studentDisply(StudentResult):

    def getDisply(self):
        print("Name:", self.name)
        print("Age:", self.age)
        print("Gender:", self.gender)
        print("class:", self.studentClass)
        print("Chemistry:", self.chemistry)
        print("physics:", self.physics)
        print("Maths:", self.maths)
        print("English:", self.English)


st = studentDisply()
st.getStudent()   # creates name, age, gender
st.getMarks()     # creates marks
st.getDisply()
