# Author: Cui Qiaoxu qfc5036@psu.edu
# Collaborator: John O'Toole Jbo5232@psu.edu
# Collaborator: Ching-Ju Chen cxc6001@psu.edu
# Section: 8
# Breakout: 11
def getGradePoint (str):
  if   str == "A":
    return 4.0
  elif str == "A-":
    return 3.67
  elif str == "B+":
    return 3.33
  elif str == "B":
    return 3.0
  elif str == "B-":
    return 2.67
  elif str == "C+":
   return 2.33
  elif str == "C":
    return 2.0
  elif str == "D":
    return 1.0
  else:
    return 0.0

if __name__ == "__main__":
  gradepoint=0
  credit=0
  for i in range(1,4):
    ingrade=input(f"Enter your course {i} letter grade: ")
    incredit=int(input(f"Enter your course {i} credit: "))
    gradepoint+=getGradePoint(ingrade)*incredit
    credit+=incredit
    print(f"Grade point for course {i} is: {getGradePoint(ingrade)}")
  print(f"Your GPA is: {gradepoint/credit}")