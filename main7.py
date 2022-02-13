import json
file = open("diction.txt", "r")
fl = file.readline()
fD = json.loads(fl)
file.close()
print('\n')
x = fD.keys()
key_list = list(x)
print("ΤΑ ΔΙΑΘΕΣΙΜΑ ΚΛΕΙΔΙΑ ΕΙΝΑΙ:")
print('\n')
print(key_list)
print('\n')

key = input("ΕΠΙΛΕΞΤΕ ΕΝΑ ΑΠΟ ΤΑ ΔΙΑΘΕΣΙΜΑ ΚΛΕΙΔΙΑ:")
kleidi = key

print('\n')
dicts_from_file = []
with open('diction.txt','r') as inf:
    for line in inf:
        dicts_from_file.append(eval(line))


values_of_key = [a_dict[kleidi] for a_dict in dicts_from_file]
list = values_of_key

print('\n')
print("Η ΜΕΓΙΣΤΗ ΤΙΜΗ ΤΟΥ KEY ΠΟΥ ΕΠΙΛΕΞΑΤΕ ΕΙΝΑΙ:")
print(max(list))
print('\n')
print("Η ΕΛΑΧΙΣΤΗ ΤΙΜΗ ΤΟΥ KEY ΠΟΥ ΕΠΙΛΕΞΑΤΕ ΕΙΝΑΙ:")
print(min(list))





















































