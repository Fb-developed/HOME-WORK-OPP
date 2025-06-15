# def string(n):
#     res = n.replace('M','W')
#     print(res)
# n = input()
# string(n)



# def string(n):
#     length = len(n)
#     if length % 2 == 0:
#         print('True')
#     else:
#         print('False')
# n = input()
# string(n)



# def string(n):
#     if n.isupper() or n.islower():
#         print('True')
#     else:
#         print('False')

# n = input()
# string(n)



# def half_quater_eighth(n):
#     print(n // 2)
#     print(n / 4)
#     print(n / 8)
# n = int(input())
# half_quater_eighth(n)




# def how_many_times(n):
#     print('ed','a'* n,'bit', sep='')
# n = int(input())
# how_many_times(n)





# def has_space(n):
#     if ' ' in n:
#         print('True')
#     else:
#         print('False')
# n = input()
# has_space(n)


# lst = [1, 2, 3, 4, 5, 6, 7, 8, 9, 10]
# def min_max(lst):
#     print('Min:', min(lst))
#     print('Max:', max(lst))
# min_max(lst)




# def count_d(n):
#     cnt = 0
#     for i in n:
#         if i == 'd':
#             cnt += 1
#     print(cnt)
# n = input()
# count_d(n)




# def accept_into_movice(age, supervised):
#     if age >= 15 or supervised == 'True':
#         print('True')
#     else:
#          print('False')
# age = int(input())
# supervised = input()
# accept_into_movice(age,supervised)





# def create_id(n,n1:str):
#     res = n[0] + n1[0].capitalize() + n1[1] + n1[2]
#     print(res)
# n = input()
# n1 = input()
# create_id(n,n1)





# def smash_factor(bs,cs):
#     print(bs / cs)
# bs = float(input())
# cs = float(input())
# smash_factor(bs,cs)





# lst = [-1,-2,-3,-4]
# def distance_home(lst):
#     sum = 0
#     for i in lst:
#         sum += i
#     res = abs(sum)
#     print(res)
# distance_home(lst)





# def yen_to_usd(n):
#     res = n * 0.00930
#     print(res)
# n = float(input())
# yen_to_usd(n)




# def is_safe_brige(str):
#     if ' ' in str:
#         print('False')
#     else:
#         print('True')
# str = input()
# is_safe_brige(str)




# def programrres(n1,n2,n3):
#     mn = min(n1, n2, n3)
#     mx = max(n1, n2, n3)
#     res = mx - mn
#     print(res)
# n1 = int(input())
# n2 = int(input())
# n3 = int(input())
# programrres(n1,n2,n3)






# def how_many_walls(n,w,h):
#     res = n // (w * h)
#     print(res)
# n = int(input())
# w = int(input())
# h = int(input())
# how_many_walls(n,w,h)




# def claculate(a,b,c):
#     match c:
#         case '+':
#             print(a + b)
#         case '-':
#             print(a - b)
#         case '*':
#             print(a * b)
#         case '/':
#             print(a / b)
# a = int(input())
# b = int(input())
# c = input()
# claculate(a,b,c)




# def accept_into_movice(age, supervised):
#     if age >= 18 or supervised == 'True':
#         print('True')
#     else:
#          print('False')
# age = int(input())
# supervised = input()
# accept_into_movice(age,supervised)






# def nth_even(n):
#     if n == 0:
#         print('0 is the first even number')
#     else:
#         res = 2 * (n - 1)
#         print(res)
# n = int(input())
# nth_even(n)





# def flip(n):
#     if n == 0:
#         print(1)
#     elif n == 1:
#         print(0)
#     else:
#         print('error input')
# n = int(input())
# flip(n)





# person = ['Annie', 'Bob', 'Charlie', 'David', 'Eve']
# job = ['Doctor', 'Engineer', 'Artist', 'Teacher', 'Scientist']
# def assign_person_to_job(person, job):
#     for i in range(len(person)):
#         print(f"{person[i]} : {job[i]}")
# assign_person_to_job(person, job)




# def potatoes(n):
#     cnt = 0
#     for i in n:
#         cnt += i.count('potato')
#     print(cnt)
# n = input().split()
# potatoes(n)






# dct = {
#     'tv': 30,
#     'skate': 20,
#     'stereo': 50
# }
# def calculate_losses(dct):
#     sum = 0
#     for value in dct.values():
#         sum += value
#     if sum > 0:
#         print(sum)
#     elif sum == 0:
#         print('Lucky you!')
# calculate_losses(dct)





# lst = ['sore', 'zebra']
# def count_unique(lst):
#     res = ''.join(lst)
#     result = len(set(res))
#     print(result)
# count_unique(lst)




# lst = [11,15,6,8,9,10]
# def odd_sum_list(lst):
#     for i in range(len(lst)-1):
#         if (lst[i] + lst[i+1]) % 2 == 0:
#             print('True')
#         else:
#             print('False')
# odd_sum_list(lst)




# lst = [2,3,4,5,6,2,5,7,9,5]
# def unique_sort(lst):
#     res = sorted(set(lst))
#     print(res)
# unique_sort(lst)





# dct = {
#     'student 1': 'Steve',
#     'student 2': 'Becky',
#     'student 3': 'John',
# }
# lst = []
# def get_student_names(dct):
#     for value in dct.values():
#         lst.append(value)
#     lst.sort()
#     print(lst)
# get_student_names(dct)





# str = '100101'
# def integer_boolean(str):
#     for i in str:
#         if i == '1':
#             print('True')
#         else:
#             print('False')
# integer_boolean(str)





# def count_all(str):
#     dct = {
#         'LETTERS' : 0,
#         'DIGITS' : 0
#     }
#     for i in str:
#         if i.isalpha():
#             dct['LETTERS'] += 1
#         else:
#             dct['DIGITS'] += 1
#     print(dct)
# str = input()
# count_all(str)




# lst = ['sept 22', 'sept 21', 'oct 15']
# def upload_count(lst):
#     n = input('Enter the month for count: ')
#     cnt = 0
#     for i in lst:
#         if i.startswith(n):
#             cnt += 1
#     print(cnt)
# upload_count(lst)




# def matrix(x,y,z):
#     res = []
#     for i in range(x):
#         res.append([z] * y)
#     print(res)
# x = int(input())
# y = int(input())
# z = input()
# matrix = matrix(x,y,z)








# def unrepeated(str):
#     res = ''
#     for i in str:
#         if i not in res:
#             res += i
#     print(res)
# str = input()
# unrepeated(str)







# def rps(p1,p2):
#     if len(p1) > len(p2):
#         print('Player 1 wins')
#     elif len(p1) < len(p2):
#         print('Player 2 wins')
#     else:
#         print('Draw')
# p1 = input()
# p2 = input()
# rps(p1,p2)





# def sum_odd_and_even(lst):
#     even_sum = 0
#     odd_sum = 0
#     for i in lst:
#         if i % 2 == 0:
#             even_sum += i
#         else:
#             odd_sum += i
#     return [even_sum, odd_sum]
# print(sum_odd_and_even([3,3,4,3,84]))
# print(sum_odd_and_even([-1,-2,-3,-4,-5,-6]))





# def common_elements(lst1, lst2):
#     res = []
#     for i in lst1:
#         if i in lst2 and i not in res:
#             res.append(i)
#     return res
# lst1 = [-1, 3, 4, 6, 7, 9]
# lst2 = [1, 3]
# print(common_elements(lst1, lst2))





# dct = {
#     'Luxury chocolate': '*****',
#     'Tasty chocolate': '***',
#     'Aunty chocolate': '*****',
#     'Generic chocolate': '**',

# }
# def filter_by_rating(dct):
#     n = int(input())
#     res = {}
#     for key, value in dct.items():
#         if len(value) == n:
#             res[key] = value
#     if res:
#         print(res)
#     else:
#         print('No results found')
# filter_by_rating(dct)




# lst = [13,True,13,None]
# def delete_occurrences(lst, n):
#     res = []
#     for i in lst:
#         if res.count(i) < n:
#             res.append(i)
#     return res
# n = int(input())
# print(delete_occurrences(lst, n))



# lst = ['1=one', '2=two', '3=three', '4=four']
# def str_to_dict(lst):
#     res = {}
#     for i in lst:
#         key, value = i.split('=')
#         res[key] = value
#     return res
# print(str_to_dict(lst))



# lst = [10,20,30,5,40,50,40,15]
# def twins(lst):
#     total = sum(lst)
#     res = 0
#     for i in range(len(lst)):
#         res += lst[i]
#         res1 = total - res
#         if res == res1:
#             return i + 1
#     return -1
# print(twins(lst))




# lst1 = [1,2,3]
# lst2 = ['one', 'two', 'three'] 
# def swap_d(lst1,lst2,n):
#     res = {}
#     if n == 'False':
#         for i in range(len(lst1)):
#             res[lst1[i]] = lst2[i]
#     else:
#         for i in range(len(lst1)):
#             res[lst2[i]] = lst1[i]
#     return res
# n = input()
# print(swap_d(lst1, lst2, n))






# lst = [['A', 'B', 'C'], [2,7,1], [3,6,7],[4,5,5]]
# def total_sales(lst,n):
#     sum = 0
#     for i in lst[0]:
#         if n == i:
#             sum += lst[1][lst[0].index(i)] + lst[2][lst[0].index(i)] + lst[3][lst[0].index(i)]
#     if sum == 0:
#         return 'Product not found'
#     return sum
# n = input()
# print(total_sales(lst,n))