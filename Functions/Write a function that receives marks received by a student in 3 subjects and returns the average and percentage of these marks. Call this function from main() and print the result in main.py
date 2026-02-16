def AP(m1, m2, m3):
    tot = m1 + m2 + m3
    avg = tot / 3
    per = (tot / 150) * 100
    print("Average = %0.2f  Percentage = %0.2f" % (avg, per))
def main():
    i = int(input("Enter sub1 marks out of 50 : "))
    j = int(input("Enter sub2 marks out of 50 : "))
    k = int(input("Enter sub3 marks out of 50 : "))
    AP(i, j, k)
main()

O/P:
Enter sub1 marks out of 50 : 48
Enter sub2 marks out of 50 : 45
Enter sub3 marks out of 50 : 47
Average = 46.67  Percentage = 93.33
