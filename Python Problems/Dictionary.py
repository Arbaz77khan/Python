MyDict = {
            "apple": "fruit",
            "criket": "game",
            "marks_list": [1,44,55],
            "tuple": (33,),
            "mydict2": {
                            "pen": "paper"
                        },
             1: 34           
          }
print(type(MyDict))
print(MyDict['apple'])
print(MyDict["marks_list"])
print(MyDict['tuple'])
print(MyDict[1])

print(MyDict['mydict2']['pen'])

print(MyDict.keys())
print(MyDict.values())
print(MyDict.items()) #key value pair

print(type(MyDict.values()))
print(list(MyDict.values()))


#update dictionary

updateDict = {
    "book" : "bag",
    "arbaz" : "khan",
    "apple": "plant",   #also updates previous key-value sets.
}

MyDict.update(updateDict)

print(MyDict)

print(MyDict.get('apple')) 

print(MyDict['apple'])

s = 'apple'
if s in MyDict:
    print(True)
else:
    print(False)

print(MyDict['bag'])