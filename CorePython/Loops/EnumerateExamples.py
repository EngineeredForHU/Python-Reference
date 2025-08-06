# This python file is meant to showcase the Enumerate function within python
# What is an enumerate function?
# The enumerate function helps keep track of the index in the sequence being traversed
li = ['angel','perez','GIGI']

# Notice how this for-enumerate starts at zero, there will be times when you want to start at one
print("Starting at 0")
for i,name in enumerate(li):
    print(f'{i}:{name}')

# Here is an example starting the index at 1
print("\nStarting at 1")
# The second parameter is the starting point, and if there is no explicit starting point python starts at 0
for i, name in enumerate(li, 1):
    print(f'{i}: {name}')
