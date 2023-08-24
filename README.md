# iam_user_migration_scripts

Automated user migration and management of AWS Identity and Access Management (IAM) resources.
Project Overview:
Migrate a substantial user base from an on-premises system to AWS by automating the migration process, ensuring data integrity, and efficiently managing AWS Identity and Access Management (IAM) resources. I utilized both Python and Bash scripts to facilitate this automation process.
Project Goals:
Migrate 100+ users from an on-premises system to AWS.
Automate the migration process to reduce manual intervention and potential errors.
Ensure secure and controlled access to AWS resources using IAM best practices.

Project Phases:
Discovery & Planning
AWS Setup
Data Migration
IAM Management
Testing & Validation
Full Migration
Monitoring & Maintenance

Phase 1: Discovery & Planning

Gather detailed information about the existing user data in the on-premises CVS file.
Identify the AWS services and resources that need to be provisioned for the users' access.
Plan the migration strategy, considering user roles, permissions, and group structures.
Define the IAM policies and permissions required for each user group.

Phase 2: AWS Setup
Set up an AWS account if not already established.
Configure the AWS Management Console and AWS Command Line Interface (CLI) access.
Create the necessary AWS services, such as Amazon S3 buckets for data storage and Amazon RDS for databases if needed.

I will utilize an IT team composed of various groups, including Database Administrators, Linux Administrators, Network Administrators, and Cloud Administrators, alongside a separate group dedicated to new Trainees. These Trainees will be granted ReadOnlyAccess permissions.
DBA
LinuxAdmin
NetworkAdmin
CloudAdmin
Trainees

Creating user groups in AWS IAM (Identity and Access Management) is an important step for organizing users and managing permissions efficiently.

## user_group_create.sh
Here's a breakdown of what the first script user_group_create.sh does:
i. AWS Region Configuration: It sets the AWS_REGION variable to specify the AWS region where the IAM users and groups will be created. In this case, it's set to "us-east-1."
ii. Create User Groups: It uses a for loop to create IAM groups with the following names: "NetworkAdmin," "LinuxAdmin," "DBAdmin," "CloudAdmin," and "Trainees." These groups are created in the specified AWS region.
iii. Attach Policies to Groups: It uses aws iam attach-group-policy commands to attach AWS managed policies to the respective IAM groups:

"NetworkAdmin" group gets AmazonVPCFullAccess.
"LinuxAdmin" group gets AmazonEC2FullAccess.
"DBAdmin" group gets AmazonRDSFullAccess.
"CloudAdmin" group gets AdministratorAccess.

By attaching these policies, I'm following the principle of least privilege, ensuring that users have only the necessary permissions for their specific roles. This enhances security and prevents unauthorized or accidental modifications to critical resources.
iv. Attach ReadOnlyAccess Policy: It attaches the ReadOnlyAccess policy to the "Trainees" group. Users in this group can view and analyze resources but cannot make any changes. This policy is suitable for individuals who are still learning and should not have the ability to modify resources.
v. Print Success Message: After creating the groups and attaching policies, it prints a message indicating that the user groups have been created with the specified policies attached.
This script is essentially a part of an AWS IAM setup process. It creates groups with different levels of access (full access for some groups, read-only access for others) and associates these groups with AWS managed policies. The "Trainees" group is given read-only access, while other groups receive more extensive permissions.
Before running this script, you should ensure that you have the AWS CLI installed and configured on your system with the necessary IAM permissions to create groups and attach policies. Additionally, review and adjust the policies to meet your organization's security requirements and access control policies.


Phase 3: Data Migration
Part 1
I utilized a Python script for generating a sample CSV file that contains information about IT team members and their assigned groups. 
Here's a breakdown of what the second script sample_it_team_members_generator.py does:
1. IT Team Member Names: 

The script starts by defining a list named it_team_members containing the names of IT team members. You can customize this list to include the actual names of your team members or use a name generator.
2. Group Names: 
The script defines a list named groups containing the names of the groups: "NetworkAdmin", "LinuxAdmin", "DBAdmin", "CloudAdmin", and "Trainees".
3. Group Assignment and Distribution:
 The script initializes an empty dictionary named group_members to hold the members of each group. It then shuffles the list of IT team members randomly using the random.shuffle function.The script distributes team members evenly into groups by iterating through the shuffled list of team members. The % operator is used to distribute members evenly based on the number of groups.
4. CSV File Creation: 
The script writes the generated data into the "it_team_members.csv" file. It uses the csv.writer class to create and write the CSV file.The header row is written as ['Name', 'Group'], and for each group, the script writes the username (constructed from the first and last name) and the corresponding group name.
5. Output: 
After the data is written to the CSV file, the script prints a success message.
The resulting CSV file will contain a list of team members with their names and the groups they belong to. This script can be helpful for organizing and managing IT team members' information in a structured format.

Part 2

