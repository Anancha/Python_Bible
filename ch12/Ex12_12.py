import os

print("ไดเร็คทอรีปัจจุบัน คือ ",os.getcwd())
print("ไดเร็คทอรี ", os.getcwd() , "ประกอบด้วย ", os.listdir(os.getcwd()))

try :
    os.mkdir("c:\PyCharmProj\mypython")
except FileExistsError :
    print("ไม่สามารถสร้างไดเร็คทอรีได้ เนื่องจากมีไดเร็คทอรีนี้แล้ว")
else :
    print("ไดเร็คทอรี ", os.getcwd() , "ประกอบด้วย ", os.listdir(os.getcwd()))

    os.rename("c:\PyCharmProj\mypython","c:\PyCharmProj\python_test")
    print("ไดเร็คทอรี ", os.getcwd() , "ประกอบด้วย ", os.listdir(os.getcwd()))

    os.chdir("c:\PyCharmProj\python_test")
    with open("testfile.txt","w") as file :
        file.write("test write file")
    print("ไดเร็คทอรี ", os.getcwd() , "ประกอบด้วย ", os.listdir(os.getcwd()))

    os.remove("testfile.txt")
    print("ไดเร็คทอรี ", os.getcwd(), "ประกอบด้วย ", os.listdir(os.getcwd()))

    os.chdir("c:\PyCharmProj")
    os.rmdir("c:\PyCharmProj\python_test")
    print("ไดเร็คทอรี ", os.getcwd(), "ประกอบด้วย ", os.listdir(os.getcwd()))