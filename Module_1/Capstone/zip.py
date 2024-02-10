'''🌎🛍️ Suppose you work for a company that sells products in different countries. You have been given two lists: one containing the names of the countries where the company sells its products, and the other containing the sales data for each country. Your task is to create a dictionary where the keys are the country names, and the values are the corresponding sales data. However, the sales data should only include values that are greater than 1000. You are not allowed to use any loops, and must use list comprehension to solve the problem.

Can you write the code to create the desired dictionary using list comprehension?

👉 Hint: You can use zip function to create pairs of country and sales data from the two lists.'''


countries = ["USA", "Canada", "Mexico", "Brazil", "UK", "France", "Germany", "China", "India"]
sales = [2500, 300, 1200, 800, 500, 2000, 4000, 1000, 1500]
dict_data= dict(zip(countries,sales))
desired_output={countries:sales for countries,sales in dict_data.items() if sales>1000}
print(desired_output)