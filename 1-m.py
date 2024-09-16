f = open("main/7-dars/file.vazifa/input.txt","r")
file = open("main/7-dars/file.vazifa/a.file.txt","w")

son = f.read().split()
for i in son:
    i = int(i)
    
    file.write(chr(i))


"""
Men git orqali yuklandim

"""



