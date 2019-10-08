import os
import pandas as pd 

# add new courses to the csv 
data = pd.read_csv("courses.csv")

path = "E:\GIT\VIT-Student-Resource-Database\courses"

for course in data["Courses"] : 
	cname = '# ' + course +' '
	course = '"' + course + '"'
	os.system("mkdir " + course + " && echo " + cname + " > " + course+"/README.md")
	os.chdir(course.strip('\"'))
	os.system("mkdir YouTube PDF DOC PPT QuestionPapers" + " && echo add links >  YouTube/YouTube.md" + " && echo add PDFS >  PDF/PDF.md " + "&& echo add docs >  DOC/DOC.md"+ " && echo add ppts >  PPT/PPT.md"+ " && echo add question papers >  QuestionPapers/QuestionPapers.md ")
	os.chdir(path)


