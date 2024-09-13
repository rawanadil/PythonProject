# Write a Python function that takes a dictionary (dic) as an argument.
# The dictionary has student names as keys and lists of three numerical grades as values:
# die = {"Hiba": [100,90,86],"'Noor":|70,66,86]}
# The function should calculate the average of the three grades for each student, print this average,
# and store it in a new dictionary (new _dic) with the student's name as the key and the calculated average as the value?

def my_fun():
    new_dic={}
    for h,k in dic.items():
        r = sum(k) /len(k)
        new_dic[h]=r
    return new_dic
dic={"Hiba": [100, 90,86],"Noor":[70,66,86]}
e = my_fun()
print(e)