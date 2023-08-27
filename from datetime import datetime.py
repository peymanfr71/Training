from datetime import datetime

byy = int(input("Enter birth date(year): "))
bmm = int(input("Enter birth date(month): "))
bdd = int(input("Enter birth date(day): "))
cyy = int(input("Enter current date(year): "))
cmm = int(input("Enter current date(month): "))
cdd = int(input("Enter current date(day): "))

birth_date = datetime(byy, bmm, bdd)
current_date = datetime(cyy, cmm, cdd)
age = current_date - birth_date

years = age.days // 365
months = (age.days % 365) // 30
days = (age.days % 365) % 30

print(f"Old is: {years}/{months}/{days}")

