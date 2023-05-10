import random

from data.data import Person
from faker import Faker

faker_ru = Faker('ru_RU')
faker_en = Faker()

def generated_person():
	yield Person(
		full_name=faker_ru.first_name() + " " + faker_ru.last_name() + " " + faker_ru.middle_name(),
		first_name=faker_ru.first_name(),
		last_name=faker_ru.last_name(),
		age=random.randint(10,80),
		salary=random.randint(10000, 100000),
		department=faker_ru.job(),
		first_name_bazar=faker_ru.first_name(),
		email=faker_en.email(),
		email_bazar=faker_en.email(),
		current_address=faker_ru.address(),
		permanent_address=faker_ru.address(),
		number=faker_en.phone_number(),
		second_name=faker_ru.last_name(),
		middle_name=faker_ru.middle_name(),
	)

"""def generated_person_from_viyar():
	yield Person(
		second_name=faker_ru.last_name(),
		#first_name=faker_ru.first_name(),
		#email=faker_en.email(),
		middle_name=faker_ru.middle_name(),
		number=faker_en.phone_number(),
 )"""

def generated_file():
	random_number = random.randint(0, 999)
	path = rf'C:\Users\d_onishchuk\PycharmProjects\pythonProject/testfile{random_number}.txt'
	file = open(path, "w+")
	file.write(f"Hello world{random_number}")
	file.close()
	return file.name, path