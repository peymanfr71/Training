from datetime import datetime

birth_date_str = input("Enter birth date (YYYY-MM-DD): ")
current_date_str = input("Enter current date (YYYY-MM-DD): ")

birth_date = datetime.strptime(birth_date_str, '%Y-%m-%d')
current_date = datetime.strptime(current_date_str, '%Y-%m-%d')
age = current_date - birth_date

years = age.days // 365
months = (age.days % 365) // 30
days = (age.days % 365) % 30

print(f"Old is: {years}/{months}/{days}")
