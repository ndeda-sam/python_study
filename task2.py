# Convert a float to an integer with an inbuilt function in Python
# temp = 56.8926 to 57
 temp = 56.8926
temp=round(temp)
print(temp)
# Convert the float below to give the results as follows
# temp = 56.8926 to 56.89 
# Convert the float below to give the results as follows
# temp = 56.8926 to 56.893
temp=56.8926
temp=round(temp,3)
print(temp)
# Convert the float below to give the results as follows
# temp=56.8926 to 8.926
temp=56.8926
# converto string
temp=str(temp)#56.8926 
#slice
temp=temp[3:7] #8926
#8+','+926
temp=temp[0]+' '+temp[1:]
temp=float(temp)
print=(temp)

# NB: Use string  slice & concatenation, but have result as float 
