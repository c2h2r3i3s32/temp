import math
s1 = int(input("Enter the one side of trangle"))
s2 = int(input("Enter the one side of trangle"))
s3 = int(input("Enter the one side of trangle"))
s = (s1 + s2 + s3)/2
area = math.sqrt(s * (s - s1) * (s - s2) * (s - s3))
print(area)
