data = [1,2,3]
copyData = data
moreData = [1,2,3]

# checks for reference equality
print(data is moreData)
print(data is copyData)

# check for value equality
print(data == moreData)
