# def get_budgets(lst):
#     sum = 0
#     for i in range(len(lst)):
#         sum += lst[i]["budget"]
#     return sum
#
# lst = [
#   { "name": "John", "age": 21, "budget": 23000 },
#   { "name": "Steve",  "age": 32, "budget": 40000 },
#   { "name": "Martin",  "age": 16, "budget": 2700 }
# ]
# print(get_budgets(lst))

# txt = "hello"
# lst = [i for i in txt]
# lst.sort()
# print("".join(lst))
list1=['abc']
list2=['123']
l = [list1[i] for i in range(len(list1))]
print(l)

