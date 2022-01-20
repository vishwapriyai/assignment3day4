#assignment3day4
##first function take all 7 datatypes in a list print that in proper f string
from tokenize import Double


def list(list,tuple,dictionary,float,string,integer,):
    print(f"list is:{list},tuple is:{tuple},dictionary is:{dictionary},float is {float},string is:{string},integer is:{integer}")
list([1,2,"xy",5.3],(3,6.8,"vp"),{"name":"vish","age":18,"percent_mark":"99.9"},68.79,"ammu",100)

## second function take a dictinory print in for  with f string

a={"aim1":"ias","aim2":"datascientist"}
for each_aim in a:
    print(f"aim is:{a}")


    

##third function take two number and need to written both the number in the list

def double(number):
    return number*2
number_list=[1,2,3]
output_list=[double(i) for i in number_list]
print(output_list)



