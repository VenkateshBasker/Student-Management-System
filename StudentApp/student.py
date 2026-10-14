class Student:
    def __init__(self,name):
        self.name = name
        self.marks = []
        self.pass_fail = []
        self.sub_grades = []
        self.subjects = ["Tamil", "English", "Maths", "Science", "Social"]
        self.lowest_subgrade=""
        self.subject_grade_lowest=[]
        self.subject_grade=[]
        self.highest_subgrade=""
        self.total_marks=0
        self.average_marks=0
        self.highest_mark=0
        self.highest_subject=""
        self.lowest_mark=0
        self.lowest_subject=""
        self.performance=""
        self.grade=""
        self.result=""

    def get_marks(self):
        for subject in self.subjects:
            while True:
                try:
                    scr = int(input(f"Enter {self.name}'s {subject} Mark : "))
                    if scr > 100 or scr < 0:
                        print("please enter a Valid Mark!!!")
                    else:
                        if scr >= 35:
                            self.pass_fail.append("Pass")
                            if scr >= 90:
                                self.sub_grades.append("A")
                            elif scr >= 75:
                                self.sub_grades.append("B")
                            elif scr >= 50:
                                self.sub_grades.append("C")
                            else:
                                self.sub_grades.append("D")
                        else:
                            self.pass_fail.append("Fail")
                            self.sub_grades.append("E")
                        self.marks.append(scr)
                        break
                except ValueError:
                    print("please enter a Valid Mark!!!")
        self.result = "Pass"
        for i in self.pass_fail:
            if i == "Fail":
                self.result = "FAIL"
                break
        return self.result

    def update_report(self):
        self.pass_fail=[]
        self.sub_grades=[]
        for scr in self.marks:
            if scr >= 35:
                self.pass_fail.append("Pass")
                if scr >= 90:
                    self.sub_grades.append("A")
                elif scr >= 75:
                    self.sub_grades.append("B")
                elif scr >= 50:
                    self.sub_grades.append("C")
                else:
                    self.sub_grades.append("D")
            else:
                self.pass_fail.append("Fail")
                self.sub_grades.append("E")
        self.result = "Pass"
        for i in self.pass_fail:
            if i == "Fail":
                self.result = "FAIL"
                break
        self.generate_report()
        return self.result


    def generate_report(self):
        self.calculate_marks()
        self.calculate_grades()
        self.calculate_performance()
        self.highest()
        self.lowest()

    def highest(self):
        self.subject_grade = []
        self.highest_subgrade = (min(self.sub_grades))
        for i, j in zip(self.sub_grades, self.subjects):
            if i == self.highest_subgrade:
                self.subject_grade.append(j)
        return self.subject_grade, self.highest_subgrade

    def lowest(self):
        self.subject_grade_lowest = []
        if len(set(self.sub_grades)) == 1:
            self.lowest_subgrade = "None"
            self.subject_grade_lowest = []
        else:
            self.lowest_subgrade = (max(self.sub_grades))
            for i, j in zip(self.sub_grades, self.subjects):
                if i == self.lowest_subgrade:
                    self.subject_grade_lowest.append(j)
        return self.subject_grade_lowest, self.lowest_subgrade

    def calculate_marks(self):
        self.total_marks = sum(self.marks)
        self.average_marks = self.total_marks / len(self.subjects)
        self.highest_mark = max(self.marks)
        self.highest_subject = self.subjects[self.marks.index(self.highest_mark)]
        self.lowest_mark = min(self.marks)
        self.lowest_subject = self.subjects[self.marks.index(self.lowest_mark)]
        return self.total_marks, self.average_marks, self.highest_mark, self.highest_subject, self.lowest_mark, self.lowest_subject

    def calculate_grades(self):
        if self.total_marks >= 450:
            self.grade="Grade A"
            return self.grade
        elif self.total_marks >= 400:
            self.grade = "Grade B"
            return self.grade
        elif self.total_marks >= 350:
            self.grade = "Grade C"
            return self.grade
        elif self.total_marks >= 250:
            self.grade = "Grade D"
            return self.grade
        else:
            self.grade = "Grade E"
            return self.grade

    def calculate_performance(self):
        if self.average_marks >= 90:
            self.performance="OUTSTANDING"
            return self.performance
        elif self.average_marks >= 75:
            self.performance="EXCELLENT"
            return self.performance
        elif self.average_marks >= 60:
            self.performance="GOOD"
            return self.performance
        elif self.average_marks >= 50:
            self.performance="AVERAGE"
            return self.performance
        else:
            self.performance="NEEDS IMPROVEMENT!!!"
            return self.performance

    def display_report(self):
        print("============ STUDENT MARK SHEET ============\n")
        print("NAME : ", self.name, "\n")
        for m, j, s, k in zip(self.subjects, self.marks, self.sub_grades, self.pass_fail):
            print(m.upper(), ":", j, ":", s, ":", k.upper())
        print("\n")
        print("Total Marks : ", self.total_marks)
        print("Average Marks : ", self.average_marks)
        print("Highest Mark : ", self.highest_mark, "(", self.highest_subject, ")")
        print("Lowest Mark : ", self.lowest_mark, "(", self.lowest_subject, ")")
        print("Performance : ", self.performance)
        print("Grade : ", self.grade, "\n")
        print("Highest Grade : ", self.highest_subgrade)
        print("Highest Grade Subjects : ", ", ".join(self.subject_grade), "\n")
        print("Lowest Grade : ", self.lowest_subgrade)
        print("Lowest Grade Subjects : ", ", ".join(self.subject_grade_lowest), "\n")
        print("OVERALL RESULT : ", self.result, "\n")
        print("============================================\n")