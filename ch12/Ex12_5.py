player = int(input("กรอกจำนวนผู้เล่นว่ามีกี่คน : "))
i = 1

with open("score.txt", "w+") as file_score :
    while player != 0 :
        print("คนที่ ",i)
        score = input("กรอกคะแนน : ")
        data = "ผู้เล่นคนที่ " + str(i) + " คะแนน " + score
        file_score.write(data)
        file_score.write("\n")
        player = player - 1
        i = i+1
    file_score.seek(0)
    print("\nข้อมูลที่บันทึกลงไฟล์ คือ ")
    print(file_score.read())
