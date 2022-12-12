#Creator CS 12/2/2022 

def write_invitations(names): # Use a for loop to iterate over the names in the list
    for name in names:
        # create invitation 
        invitation = f"Hi {name}, You're invited to my party on Friday!"

        # Print invitation 
        print(invitation)

# Create a list of names
names = ["Joe", "Preston", "Colin"]

# Call the function 
write_invitations(names)
