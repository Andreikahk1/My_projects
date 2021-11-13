beatles = []
beatles.append("John Lennon")
beatles.append("Paul McCartney")
beatles.append("George Harrison")
print(beatles)
stu = "Stu Sutcliffe"
pete = "Pete Best"
for i in (stu,pete):
    txt = "Please add '"+i+"' to the list: "
    user_choice = input(txt)
    beatles.append(user_choice)
print(beatles)
del beatles[len(beatles)-1]
del beatles[len(beatles)-1]
print(beatles)
beatles.insert(0,"Ringo Star")
print(beatles)
