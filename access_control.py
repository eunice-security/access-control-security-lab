import math

users = []

file_handle = open("authorized_users.txt", "r")
data = file_handle.readlines()
file_handle.close()

for d in data:
    d = d.strip()
    tmp = d.split(",")

    user = {}
    user["username"] = tmp[0]
    user["pass"] = tmp[1]
    user["level"] = int(tmp[2])

    users.append(user)

username = input("Please enter your username: ")
password = input("Please enter your password: ")

authorized = False

for user in users:
    if username == user["username"] and password == user["pass"]:
        authorized = True

if authorized:
    print("Welcome to the Fertilizer Calculator! I will ask you for the length and width of four rectangular sections. Please enter your measurements in feet (numbers only, please). If you do not have a particular section, simply enter zero (0) for those dimensions! ")

    front_length = float(input("What is the length of the front section? "))
    front_width = float(input("What is the width of the front section? "))

    rear_length = float(input("What is the length of the rear section? "))
    rear_width = float(input("What is the width of the rear section? "))

    left_length = float(input("What is the length of the left section? "))
    left_width = float(input("What is the width of the left section? "))

    right_length = float(input("What is the length of the right section? "))
    right_width = float(input("What is the width of the right section? "))

    front_area = front_length * front_width
    rear_area = rear_length * rear_width
    left_area = left_length * left_width
    right_area = right_length * right_width

    total_area = front_area + rear_area + left_area + right_area

    fertilizer_cost = total_area * 0.015
    bags_required = math.ceil(total_area / 2000)
    hours_required = math.ceil(total_area / 1800)
    labor_cost = hours_required * 20
    total_cost = fertilizer_cost + labor_cost
    nitrogen = (total_area / 1000) * 0.5
    potassium = (total_area / 1000) * 0.0625

    print()
    print(f"Total area: {int(total_area)} sq. feet")
    print()
    print(f"Cost of fertilizer: ${int(fertilizer_cost)}")
    print()
    print(f"Bags of fertilizer required: {bags_required}")
    print()
    print(f"Minimum hours required: {hours_required}")
    print()
    print(f"Cost of labor: ${int(labor_cost)}")
    print()
    print(f"Total cost: ${int(total_cost)}")
    print()
    print(f"Nitrogen applied to soil: {nitrogen:.3f} pounds")
    print()
    print(f"Potassium applied to soil: {potassium:.3f} pounds")

else:
    print("You have entered invalid credentials, please find your password and start over")
