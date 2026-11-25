
n = int(input("Enter number of subjects: "))

subjects = []
exam1 = []
exam2 = []

for i in range(n):
    name = input("\nEnter subject name: ")
    subjects.append(name)

    m1 = float(input("Enter first exam marks: "))
    m2 = float(input("Enter second exam marks: "))

    exam1.append(m1)
    exam2.append(m2)

print("\n----- PERFORMANCE REPORT -----")

total1 = 0
total2 = 0

for i in range(n):
    print("\nSubject:", subjects[i])
    print("First exam:", exam1[i])
    print("Second exam:", exam2[i])

    difference = exam2[i] - exam1[i]

    if difference > 0:
        print("Performance: Improved")
    elif difference < 0:
        print("Performance: Declined")
    else:
        print("Performance: No change")

    total1 = total1 + exam1[i]
    total2 = total2 + exam2[i]

if n > 0:
    avg1 = total1 / n
    avg2 = total2 / n

    print("\nFirst exam average:", avg1)
    print("Second exam average:", avg2)

    if avg2 > avg1:
        print("Overall performance improved")
    elif avg2 < avg1:
        print("Overall performance declined")
    else:
        print("Overall performance remained the same")
