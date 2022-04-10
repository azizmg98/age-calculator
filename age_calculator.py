from datetime import date

def get_dob():
    # write code here
	year = int(input("Enter your birth year: "))
	month = int(input("Enter your birth month: "))
	day = int(input("Enter your birth day: "))

	global dob
	dob = date(year,month,day)
	return dob
	...


def get_age(dob):
    # write code here

	today = date.today()

	age = today - dob
	print(age.days / 365)
	return age.days / 365
	...


def main():
	# write code here

	get_dob()
	if dob > date.today():
		print("la tchathib")
	else:
		get_age(dob)
	...


if __name__ == '__main__':
    main()
