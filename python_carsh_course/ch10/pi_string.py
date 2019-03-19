# filename = 'pi_digits.txt'
# with open(filename) as file_objiec:
#     lines = file_objiec.readlines()
# pi_string = ''
# for line in lines:
#     pi_string += line.strip()
# print(pi_string)
# print(len(pi_string))
filename = 'pi_million_digits.txt'
with open(filename) as file_object:
    lines = file_object.readlines()
pi_string = ''
for line in lines:
    pi_string += line.strip()
while True:
    birthday = input("enter your birthday of pi")
    if birthday in pi_string:
        print("your birthday appears in the pi")
    else:
        print("not in")