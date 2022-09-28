str_a = "art"
str_b = "arc"

for i in range(len(str_a)):
    for j in range(i + 1, len(str_a)):
        print(i,j)
        if str_a[i:j] in str_b:
            print("yes")
            print(str_a[i:j])            