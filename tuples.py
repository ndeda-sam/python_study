days_of_the_week=('sun','mon','tue','Wed','THur','fri','sat')

print(type(days_of_the_week))
print(days_of_the_week[1])
print(days_of_the_week[2:4])
# diplay sat
print(days_of_the_week[6])
# thu to sat
print(days_of_the_week[4:7])

#  convrt tuple tolist()
days_of_the_week=list(days_of_the_week)
print(type(days_of_the_week))

# modify
days_of_the_week[2]='Tuesday'
# convert back to tuple tuple()
days_of_the_week=tuple(days_of_the_week)
print(days_of_the_week)

# sun to sunday

# add jan to tuple
days_of_the_week.append('Jan')
# tuple methods
#  index
# 