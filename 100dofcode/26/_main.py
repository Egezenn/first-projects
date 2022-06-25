# bzzzzzzzzt = [44, 32, 456, 88, 337]
# booooooooooooooo = [bz + 234234 for bz in bzzzzzzzzt]
# print(booooooooooooooo)

# rangelist = [number * 2 for number in range(1, 5)]
# print(rangelist)

# namelist = ["blablabla", "blabla", "bla"]
# shouting_name_list = [name.upper() for name in namelist]
# print(shouting_name_list)

# numbers = [1, 1, 2, 3, 5, 8, 13, 21, 34, 55]
# squared_numbers = [number**2 for number in numbers]
# print(squared_numbers)

# numbers = [1, 1, 2, 3, 5, 8, 13, 21, 34, 55]
# even_numbers = [number for number in numbers if number % 2 == 0]
# print(even_numbers)

# with open("_file1.txt") as file1:
#     file1_list_alt = file1.readlines()
#     file1_list = [number.strip("\n") for number in file1_list_alt]
#
#     with open("_file2.txt") as file2:
#         file2_list_alt = file2.readlines()
#         file2_list = [number.strip("\n") for number in file2_list_alt]
#
#         common = [number for number in file1_list if number in file2_list]
#         print(common)

# import random
# names = ["E", "B", "C", "Y"]
# student_scores = {student: random.randint(0, 101) for student in names}
# print(student_scores)
#
# passed_students = {student: score for (student, score) in student_scores.items() if score >= 60}
# print(passed_students)

# sentence = "What is the Airspeed Velocity of an Unladen Swallow?"
# word_list = sentence.split()
# print(word_list)
# dictionary = {word: len(word) for word in word_list}
# print(dictionary)

# weather_c = {
#     "Monday": 12,
#     "Tuesday": 14,
#     "Wednesday": 15,
#     "Thursday": 14,
#     "Friday": 21,
#     "Saturday": 22,
#     "Sunday": 24,
# }
#
# weather_f = {day: celcius * 9 / 5 + 32 for (day, celcius) in weather_c.items()}
# print(weather_f)

# import pandas
#
# student_dict = {
#     "student": ["A", "B", "C"],
#     "score": [33, 44, 55]
# }
#
# student_data_frame = pandas.DataFrame(student_dict)
# for (index, row) in student_data_frame.iterrows():
#     print(row.score)





