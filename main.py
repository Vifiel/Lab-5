import re
import csv

data1 = open("task1-en.txt", mode="r", encoding="utf-8")
data2 = open("task2.html", encoding="utf-8")
data3 = open("task3.txt", encoding="utf-8")
s1 = ""
s2 = ""
s3 = ""

if __name__ == "__main__":
    for i in data1:
        s1 += i
    res1 = re.findall(r"\b[A-Z][a-zA-Z]+", s1)
    res2 = re.findall(r"\b[a-zA-Z]+[:]", s1)
    print(f"Task 1:\nAmount of words, starting with capital letter: {len(res1)}\nAmount of words, on the end of which there are colon: {len(res2)}")

    for i in data2:
        s2 += i
    res3 = set(re.findall(r"[<][/]\w+[>]", s2))
    print(f"Task 2:\nAmount of unique closing tags: {len(res3)}")

    for i in data3:
        s3 += i

    date = re.findall(r"[ ]\d{4}[-]\d{2}[-]\d{2}", s3)
    mail = re.findall(r"[ ][-a-zA-z0-9]+[@][-a-zA-Z0-9]+[.][-a-zA-Z0-9]+[ ]", s3)
    ident = re.findall(r"[ ][0-9]+[ ]", s3)
    secondname = re.findall(r"[ ][a-zA-Z]+[ ]", s3)
    site = re.findall(r"[ ]h[a-zA-Z0-9._:\/-]+[ ]", s3)
    #Я не знаю почему, но количество данных разное, т.е., наприме, 241 дата и 245 сайтов
    m = len(min((date, mail, site, secondname, ident), key=len))
    
    with open("task3.csv", "w", newline="") as file:
        writer = csv.writer(file, delimiter=" ",
                            quotechar="|", quoting=csv.QUOTE_MINIMAL)
        for i in range(m):
            writer.writerow(ident[i:i+1] + secondname[i:i+1] + mail[i:i+1]
                            + date[i:i+1] + site[i:i+1])

        
