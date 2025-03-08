import json

l = [1,2,4,5]
with open('dummy.json', 'w') as f:
    json.dump(l, f)  # Serialization

with open('dummy.json', 'r') as f:
    print(json.load(f)) # Deserialization


# For dictionay
d = {
    'name' : 'arbaz',
    'rollno' : 32,
    'l' : [1, 2, 4]
}

with open('dummy.json', 'w') as f:
    json.dump(d, f, indent=4)

with open('dummy.json', 'r') as f:
    print(json.load(f))

class person:

    def __init__(self, n, a, p):
        self.name = n
        self.age = a
        self.place = p

obj = person('Arbaz', 33, 'Pune')

def obj_show(obj):
    if isinstance(obj, person):
        # return "Name: {} -> Age: {} -> Place: {}".format(obj.name, obj.age, obj.place) #as string
        return {'Name': obj.name, 'Age': obj.age, 'Place': obj.place}
    
with open('dummy.json', 'w') as f:
    json.dump(obj, f, default=obj_show)
