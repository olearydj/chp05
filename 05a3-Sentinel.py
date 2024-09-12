# Sentinel
# seeding the while loop
user_char = 'y'

# check for sentinel value
while user_char != 'n':
    print("doing important things")
    user_input = input("*** again? [y/n] ")
    user_char = user_input[0]

print("job's done")

# what happens if I omit line 3?