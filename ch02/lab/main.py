
#Part A
weeks = 16
classes = 5
tuition = 6000
cost_per_week = ((tuition / classes) / weeks)
print("Cost per week:", cost_per_week)

classes_per_week = (10)
print("Classes per week:", classes_per_week)

cost_per_class = (cost_per_week/classes_per_week)



print("Weeks:", weeks)


print("Classes:", classes)


print("Tuition:", tuition)


print("Finished result of the cost per class:", cost_per_class)

print(weeks, type(weeks))
print(classes, type(classes))
print(tuition, type(tuition))
print(cost_per_week, type(cost_per_week))
print(classes_per_week, type(classes_per_week))
print(cost_per_class, type(cost_per_class))

#Part B
import random
numbers_first = ("mylist")
mylist = [2,3,6,7,8]
numbers_second = (random.choice(mylist))
print(numbers_second)
