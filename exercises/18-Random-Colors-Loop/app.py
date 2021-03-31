import random

def get_color(color_number=4):
    # making sure is a number and not a string
    color_number = int(color_number)

    switcher={
                  0:'red',
                  1:'yellow',
                  2:'blue',
                  3:'green',
                  4:'black'
              }
    return switcher.get(color_number,"Invalid Color Number")


def get_allStudentColors():

    example_color = 1
    students_array = []
    findColor = false
    #your loop here
    for number in range(1,11):
        print(number)
        example_color = random.randint(1,4)
        for students in students_array
            if students == example_color:
                findColor = true
        students_array.append(get_color(example_color))
    return students_array
       
        

print(get_allStudentColors())