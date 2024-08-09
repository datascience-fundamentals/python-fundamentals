# set -> It means group of element
# Set is a collection whose elements can not be repeated and also
# this collections doesn't has an order. This meant that It doens't respect
# the order you are adding new elements.

numerosSet = {10, 10, 21, 21, 30, 40}
print(numerosSet)  # {40, 10, 21, 30}

# adding a new element
numerosSet.add(5)
print(numerosSet)  # {5, 40, 10, 21, 30}

# removing an element
numerosSet.remove(10)
print(numerosSet)  # {5, 40, 21, 30}

agesList = [3, 4, 5]
print(agesList)  # [3, 4, 5]

# convert list to set
agesSet = set(agesList)
print(agesSet)  # {3, 4, 5}

# If you want to join two set collection.
# You have to use '|'. Repeated elements are removed from the list.
unionSet = numerosSet | agesSet
print(unionSet)  # {3, 4, 21, 5, 40, 30}

# The operator intersection '|' returns
# the elements which both collections have in common
intersecSet = numerosSet & agesSet
print(intersecSet)  # {5}

# The operator '-' returns only the elements from the first set collection
# which doesn't exist in the second set collection
differenceSet = numerosSet - agesSet
print(differenceSet)  # {40, 21, 30}

# The operator "^" returns only the elements which both collections doesn't have in common
simetricDifference = numerosSet ^ agesSet
print(simetricDifference)  # {3, 4, 40, 21, 30}

# agesSet[0] -> You cant not to access to an elemento from a set collection
# However you can ask if this element exists on the set collection
print(5 in agesSet)  # True

# You can iterate a set collection
for age in agesSet:
    print(age)

# You can unpack a set collection
# *otros -> recieve a type list value
age1, *otros = agesSet
print(age1, otros)  # 3 [4,5]
