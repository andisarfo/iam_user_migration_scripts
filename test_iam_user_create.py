import csv
import subprocess
import json

# IAM policy JSON allowing ChangePassword
change_password_policy = json.dumps({
    "Version": "2012-10-17",
    "Statement": [
        {
            "Effect": "Allow",
            "Action": "iam:ChangePassword",
            "Resource": "*"
        }
    ]
})

# Function to check if a user already exists
def user_exists(username):
    try:
        subprocess.run(['aws', 'iam', 'get-user', '--user-name', username], check=True, stdout=subprocess.PIPE, stderr=subprocess.PIPE)
        return True
    except subprocess.CalledProcessError:
        return False

# Function to create a user with a login profile and set a default password
def create_user_with_profile(username, password, group):
    if not user_exists(username):
        try:
            # Create the IAM user
            subprocess.run(['aws', 'iam', 'create-user', '--user-name', username])

            # Add the user to the specified group
            subprocess.run(['aws', 'iam', 'add-user-to-group', '--user-name', username, '--group-name', group])

            # Create a login profile for the user with the default password
            subprocess.run(['aws', 'iam', 'create-login-profile', '--user-name', username, '--password', password, '--password-reset-required'])

            # Attach the ChangePassword policy to the user
            subprocess.run(['aws', 'iam', 'put-user-policy', '--user-name', username, '--policy-name', 'ChangePasswordPolicy', '--policy-document', change_password_policy])

            print(f"User '{username}' created successfully with default password '{password}' and added to group '{group}'.")
            print(f"ChangePassword policy attached to '{username}'.")

        except Exception as e:
            print(f"Error creating user '{username}': {str(e)}")
    else:
        print(f"User '{username}' already exists. Skipping.")

# Read the CSV file
with open('it_team_members.csv', mode='r') as file:
    reader = csv.DictReader(file)
    created_groups = set()  # To keep track of created groups

    for row in reader:
        username = row['Name']
        group = row['Group']

        # Check if the group is one of the groups you want to create users for
        if group in ['NetworkAdmin', 'LinuxAdmin', 'DBAdmin', 'CloudAdmin', 'Trainees']:
            # Create 1 user from each group if the group hasn't been created yet
            if group not in created_groups:
                create_user_with_profile(username, "ChangeMe1234!", group)
                created_groups.add(group)
