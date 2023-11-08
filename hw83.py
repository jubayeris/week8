# Initialize variables
senders = set()
count = 0

# Open the mbox file
with open('mbox-short.txt', 'r') as mbox:
    # Read each line in the file
    for line in mbox:
        # Check if the line starts with "From "
        if line.startswith('From '):
            # Extract the sender's email address
            sender = line.split()[1]
            # Add the sender's email address to the set
            senders.add(sender)
            # Increment the count of lines starting with "From "
            count += 1

# Print the senders
for sender in senders:
    print(sender)

# Print the number of lines starting with "From "
print(f'Total {count} lines were printed')

