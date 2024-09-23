def task_1(): # Lists

    origional_list = ["Geoff", "Jeff", "Jeffrey"]
    origional_list.insert(0,"start")
    print(origional_list)
    new_list = origional_list.copy
    print(new_list)

    return new_list


def task_2(): # Dictionaries

    keys = ("name", "age", "profession")
    values = ("Geoff", 35, "technician")

    person = dict(zip(keys, values))

    carkeys = ("make", "model", "engine", "colour")
    carvalues = ("Ford", "Focus", "1.6", "blue")

    car = dict(zip(carkeys, carvalues))

    person.update({"car": car})

 
    return person


def task_3(): # Tuples
    student_1 = ("Geoff", "Maths", 80)
    student_2 = ()
    name = input("enter first name:")
    subject = input("enter subject:")
    mark = int(input("enter mark out of 100:"))

    student_2 = (name,subject,mark)

    students = list(student_1)
    students.append(student_2)

    return students


def task_4(): # Sets
    fruits_1 = {"apple", "banana", "cherry", "grape", "mango", "pineapple", "papaya","sprite", "orange", "lemon", "strawberry"}
    fruits_2 = {"raspberry", "banana", "cherry", "grape", "mango", "blueberry", "papaya", "melon", "lemon", "steak"}

    duplicate_fruits = fruits_1.intersection(fruits_2)
    individual_fruits = fruits_1.symmetric_difference(fruits_2)


    return [duplicate_fruits, individual_fruits] # Note - functions can only return one data item - so both tuples
                                                 # are contained inside a single list