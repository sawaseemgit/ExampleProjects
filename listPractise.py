topics = ["Math", "Physics", "Biology", "English"]
topics.append('Art')  # adds at the end!
topics.insert(0, 'Chess')  # inserts at particular index
topics.extend(['a', 'b'])
sports = ['golf', 'baseball', 'cricket']
sports[0],sports[1]=sports[1],sports[0]
# print(sorted(sports, reverse=True))# Temporary sort
# sports.sort() # Permanent sort
print(sports)

spor_length=len(sports)
# print(spor_length)
# removing elements
# elem=topics.pop(1) # removes from end always
# topics.remove('Art') # removes particular element
# del topics[2]
# print(topics)
# print(elem)
