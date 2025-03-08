import pickle

# Example data (a dictionary)
data = {'name': 'John', 'age': 25, 'city': 'New York'}

# Serialize (pickling)
with open('data.pkl', 'wb') as file:
    pickle.dump(data, file)

# Deserialize (unpickling)
with open('data.pkl', 'rb') as file:
    loaded_data = pickle.load(file)

# Print the loaded data
print(loaded_data)