"""
Part I
"""

x = [ [5,2,3], [10,8,9] ]
students = [
     {'first_name':  'Michael', 'last_name' : 'Jordan'},
     {'first_name' : 'John', 'last_name' : 'Rosales'}
]
sports_directory = {
    'basketball' : ['Kobe', 'Jordan', 'James', 'Curry'],
    'soccer' : ['Messi', 'Ronaldo', 'Rooney']
}
z = [ {'x': 10, 'y': 20} ]

# Change the value 10 in x to 15. Once you're done, x should now be [ [5,2,3], [15,8,9] ].
x[1][0] = 15

# Change the last_name of the first student from 'Jordan' to 'Bryant'
students[0]['last_name'] = 'Bryant'

# In the sports_directory, change 'Messi' to 'Andres'
sports_directory['soccer'][0] = 'Andres'

# Change the value 20 in z to 30
z[0]["y"] = 30

# print(x)
# print(students)
# print(sports_directory)
# print(z)


"""
Part II
"""
def iterateDictionary(lst):
    for i in lst:
        sentence = ""
        for key, items in i.items():
            if key == "last_name":
                sentence = sentence + ", "
            sentence = sentence + key + " - " + items
        print(sentence)

def iterateDictionary2(key_name, some_list):
    for i in some_list:
        for key, items in i.items():
            if key == key_name:
                print(items)


students = [
         {'first_name':  'Michael', 'last_name' : 'Jordan'},
         {'first_name' : 'John', 'last_name' : 'Rosales'},
         {'first_name' : 'Mark', 'last_name' : 'Guillen'},
         {'first_name' : 'KB', 'last_name' : 'Tonel'}
    ]
iterateDictionary(students)
iterateDictionary2('first_name', students)
iterateDictionary2('last_name', students)


"""
Part IV
"""
def printInfo(dict):
    for key, items in dict.items():
        print(str(len(dict[key])) + " " + key.upper())
        for i in items:
            print(i)
        print()



dojo = {
   'locations': ['San Jose', 'Seattle', 'Dallas', 'Chicago', 'Tulsa', 'DC', 'Burbank'],
   'instructors': ['Michael', 'Amy', 'Eduardo', 'Josh', 'Graham', 'Patrick', 'Minh', 'Devon']
}
printInfo(dojo)
