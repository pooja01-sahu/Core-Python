import shutil

source = r"C:\Users\Dell\Desktop\read\mehandi.jpg"
target = r"C:\Users\Dell\Desktop\target\mehandimine.jpg"

shutil.copyfile(source, target)
print(source + "is copied to" + target)
