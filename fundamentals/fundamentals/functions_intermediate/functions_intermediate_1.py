# update values in dictionaries and lists
x = [ [5,2,3], [10,8,9] ]
x[1][0] = 15
print(x)
students = [
    {'first_name':  'Michael', 'last_name' : 'Jordan'},
    {'first_name' : 'John', 'last_name' : 'Rosales'}
]
students[0]['last_name'] = 'Bryant'
print(students)
sports_directory = {
    'basketball' : ['Kobe', 'Jordan', 'James', 'Curry'],
    'soccer' : ['Messi', 'Ronaldo', 'Rooney']
}
sports_directory['soccer'][0] = 'Andres'
print(sports_directory)
z = [ {'x': 10, 'y': 20} ]
z[0]['y'] = '30'
print(z)


# iterate through a list of dictionaries
def iterateDictionary(lst):
    for dict in lst:
        first_name = ""
        last_name = ""
        for key, value in dict.items():
            if key == "first_name":
                first_name = value
            if key == "last_name":
                last_name = value
        print(f"first_name - {first_name}, last_name - {last_name}")

students = [
        {'first_name':  'Michael', 'last_name' : 'Jordan'},
        {'first_name' : 'John', 'last_name' : 'Rosales'},
        {'first_name' : 'Mark', 'last_name' : 'Guillen'},
        {'first_name' : 'KB', 'last_name' : 'Tonel'}
    ]
iterateDictionary(students)


# get values from a list of dictionaries
def iterateDictionary2(key_name, lst):
    for dict in lst:
        for key, value in dict.items():
            if key == key_name:
                print(value)

iterateDictionary2("first_name", students)
iterateDictionary2("last_name", students)

# iterate through a dictionary with list values
def printInfo(some_dict):
    for key, value in some_dict.items():
        print(f"\n{str(len(value))}", key)
        for item in value:
            print(item)

dojo = {
    'locations': ['San Jose', 'Seattle', 'Dallas', 'Chicago', 'Tulsa', 'DC', 'Burbank'],
    'instructors': ['Michael', 'Amy', 'Eduardo', 'Josh', 'Graham', 'Patrick', 'Minh', 'Devon']
}
printInfo(dojo)