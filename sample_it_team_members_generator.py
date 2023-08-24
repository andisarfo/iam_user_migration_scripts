# sample_it_team_members_generator.py
##
## This script does the following:
##
## generates a CSV file named "it_team_members.csv" that contains IT team member names along with the assigned group.
## 
## How to : python3 sample_it_team_members_generator.py
## Authur : Andy Sarfo Frimpong
########################################################################################################################################

import csv
import random

# List of IT team member names (you can replace with your own list or use a name generator)
it_team_members = ["Alice Smith", "Bob Johnson", "Charlie Brown", "David Davis", "Eve Wilson", "Frank White", "Grace Lee", "Hank Harris", "Ivy Turner", "Jack Jackson", "Katie Moore", "Liam Taylor", "Mia Clark", "Noah Lewis", "Olivia King"]

# Define the group names
groups = ["NetworkAdmin", "LinuxAdmin", "DBAdmin", "CloudAdmin", "Trainees"]

# Create an empty dictionary to hold the members of each group
group_members = {group: [] for group in groups}

# Shuffle the IT team member list randomly
random.shuffle(it_team_members)

# Distribute team members evenly into groups
for i, member in enumerate(it_team_members):
    group = groups[i % len(groups)]  # Distribute evenly based on group count
    group_members[group].append(member)

# Write the data to a CSV file
with open('it_team_members.csv', mode='w', newline='') as file:
    writer = csv.writer(file)

    # Change 'User' to 'Name' in the header row
    writer.writerow(['Name', 'Group'])  # Updated header row

    for group, members in group_members.items():
        for member in members:
            # Generate the username in the format firstname.lastname
            username = member.split()[0].lower() + '.' + member.split()[1].lower()
            writer.writerow([username, group])

print("CSV file 'it_team_members.csv' created successfully.")
