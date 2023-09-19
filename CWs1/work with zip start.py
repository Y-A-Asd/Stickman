# # samp =((10,10,10),(81,80,39),(30,45,56),(1,2,3))
# # result = []
# # # for i in range(len(samp[0])):
# # #     result.append(sum(samp[j][i]) for j in range(len(samp)))
# # # for i in result:
# # #     print(i)
# #
# #
# # # for i in range(len(samp[0])):
# # #     column_sum = sum(samp[j][i] for j in range(len(samp)))
# # #     result.append(column_sum/len(samp))
# # a=zip(samp[0],samp[1],samp[2],samp[3])
# # result = tuple(map(lambda b: sum(b) / len(samp), a))
# # print(list(zip(*samp)))
# # print(*samp)
# # print(result)
# # result = tuple(map(lambda n: sum(n) / len(samp), zip(*samp)))
# # print(result)
#
# #https://www.geeksforgeeks.org/python-find-fibonacci-series-upto-n-using-lambda/
#
# # fib = lambda n: n if n <= 1 else fib(n-1) + fib(n-2)
# # n = int(input("n:"))
# # print(fib(n))
# # print([fib(i) for i in range(n)])
# # get_student_data = lambda: (input("name:"), int(input("score:")))
# n= 10
# get_student_data = lambda: (input("name:"), int(input("score:")))
# students = [get_student_data() for _ in range(n)]
#
# # a
# import string
# import random
# def generate_strong_password():
#     length = 12
#     num_uppercase = 2
#     num_lowercase = 6
#     num_digits = 2
#     num_special_chars = 2
#
#     uppercase_chars = ''.join(random.sample(string.ascii_uppercase, num_uppercase))
#     lowercase_chars = ''.join(random.sample(string.ascii_lowercase, num_lowercase))
#     digit_chars = ''.join(random.sample(string.digits, num_digits))
#     special_chars = ''.join(random.sample(string.punctuation, num_special_chars))
#
#     password = uppercase_chars + lowercase_chars + digit_chars + special_chars
#
#     return ''.join(random.sample(password, length))
# #TODO: This feature will
# print(generate_strong_password())
# print(generate_strong_password())
# print(generate_strong_password())
# print(generate_strong_password())
# print(generate_strong_password())
# print(generate_strong_password())
# print(generate_strong_password())
# print(generate_strong_password())
# print(generate_strong_password())
# print(generate_strong_password())
# print(generate_strong_password())
# import re
#
# def count_chars_words_lines(filename,*argu):
#     try:
#         with open(filename,"r") as file:
#             text = file.read()
#             char = len(text)
#             word1 = len(re.findall(r'\w+', text))
#             word2 = len(text.split(" "))
#             line1 = text.count('\n') + 1
#             line2 = len(text.split("\n"))
#             print(f"Character Count: {char}")
#             print(f"Word Count: {word1}")
#             print(f"Word Count: {word2}")
#             print(f"Line Count: {line1}")
#             print(f"Line Count: {line2}")
#             for i in argu:
#                 if i in text:
#                     print(f"'{i}' found!")
#                 else:
#                     print(f"'{i}' not found")
#     except Exception as error:
#         print(error)
#
# filename = input("Enter the filename: ")
# words_to_search = input("Enter words you want to search (comma-separated): ").split(',')
# count_chars_words_lines(filename, *words_to_search)

#
# def find_specific_words(filename, words_to_find):
#     try:
#         with open(filename, 'r', encoding='utf-8') as file:
#             text = file.read()
#             results = {}
#
#             for word in words_to_find:
#                 count = len(re.findall(r'\b{}\b'.format(re.escape(word)), text, re.IGNORECASE))
#                 results[word] = count
#
#             return results
#     except FileNotFoundError:
#         return None




# import re
#
# def emaill(email):
#     emails = r'^\w+@[a-zA-Z_]+\.[a-zA-Z]{2,3}$'
#     return re.search(emails, email)
# def passw(password):
#     return len(password) >= 6
# def user():
#     print("registration")
#     name = input("mame: ")
#     email = input("email: ")
#     password = input(" password: ")
#     if not emaill(email):
#         print("Invalid email format. Please use a valid email address.")
#         return
#     if not passw(password):
#         print("Password must be at least 6 characters long.")
#         return
#     user_info = {
#         "Name": name,
#         "Email": email,
#         "Password": password
#     }
#
#     print("\nsuccessful.\ninformation:")
#     for key, value in user_info.items():
#         print(f"{key}: {value}")
#
#
# user()

a = [1..100]
for i in range(a:
    print(i)