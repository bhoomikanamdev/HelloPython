'''import pandas as pd

data1= [ 1, 2, 'a','a', 1, 1, 'null']
df1 = pd.DataFrame(data1,columns=['Column1'])
#print(df1)

data2 = ['b', 'a', 1, 1, 1, 2, 2, 2, 3, 'b' ,'null','null' ]
df2 = pd.DataFrame(data2,columns=['Column1'])
#print(df2)

inner =  pd.merge(df1,df2, on ='Column1', how = 'inner')
print(inner)'''

'''given_list = ['a is : False', 'b is : True', 'c is : True', 'd is : False', 'e is : True',
              'f is : False', 'g is : True', 'h is : False', 'i is : False', 'j is : True']

output = {}

for item in given_list:
    key_value_pair = item.split(' is : ')
    key = key_value_pair[0]
    value = key_value_pair[1] == 'True'  # Convert 'True'/'False' string to boolean
    output[key] = value

print(output)'''

'''str= "aaaatteeekkkmmm"
for i in str:
    output = i + str(str.count(i))
    print(output)'''

'''given_string = 'aaaattteeekkkmm'
count_dict = {}

# Count the occurrences of each character
for char in given_string:
    if char in count_dict:
        count_dict[char] += 1
    else:
        count_dict[char] = 1

# Construct the output string
output_str = ""
for char, count in count_dict.items():
    output_str += char + str(count)

print(output_str)


strings = [
    "1000_987788",
    "2000_876679",
    "3000_977899",
    "4000_987789"
]

for s in strings:
    result = s.split('_')[0]
    print(result)'''


