#hash table is linear data structure 
#To perform using hash we need to follow some steps

#Step-1
#creating empty list

l=[None,None,None,None,None,None,None,None,None]

#Step=2
#creating Hash function
def hash_function(value):
    sum=0
    for ch in value:
        sum+=ord(ch)
    return sum%10


#step-3
#inserting elements using hashcode
# def add(name):
#     index=hash_function(name)
#     l[index]=name

# add('ranjan')
# add('hota')
# add('Laxmipriya')
# add('das')

print(l)


#step-4
#avoid collision
new_l=[[],[],[],[],[],[],[],[],[]]
def add(name):
    index=hash_function(name)
    new_l[index].append(name)
add('ranjan')
add('hota')
add('Laxmipriya')
add('das')
add("Manas")

print(new_l)


#search name
def contain(name):
    index=hash_function(name)
    return new_l[index]==[name]

print(contain('hota'))