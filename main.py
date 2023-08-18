import pandas
#
# list_one = [1,2,3,4,5,65,32,45,78,51,89,61,38,9,67]
# list_two = [1,2,3,4,51,62,32,45,78,53,89,61,35,10,67]
#
# list_one_df = pandas.DataFrame(list_one)
# list_two_df = pandas.DataFrame(list_two)
#
# list_one_df.to_csv("list1.csv")
# list_two_df.to_csv("list2.csv")

list1 = pandas.read_csv('list1.csv')
list2 = pandas.read_csv('list2.csv')
comp1= list1.values.tolist()
print(comp1)