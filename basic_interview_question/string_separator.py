'''Create and list and a Dict from below string -
  'narendra@modi.com' with first and last name as key value'''
# Given email address

email = 'narendra@modi.com'
name_part = email.split('@')[0] # this will give name
domain_part = email.split('@')[1] # this will give domain part
last_name = domain_part.split('.')[0] # this will give surname

first_name = name_part
list_name = [first_name,last_name]
Dict_name = {'first':first_name, 'last':last_name}
print(list_name)
print(Dict_name)




