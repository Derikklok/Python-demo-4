with open("demo.txt","a") as f:
    f.write("\nNow the file has more content!")

with open ("demo.txt") as f:
    print(f.read())