# user_group_create.sh
##
## This script does the following:
##
## Creates the specified user groups: NetworkAdmin, LinuxAdmin, DBAdmin, CloudAdmin, and Trainees.
## We attach the following AWS managed policies to the respective groups:
## "NetworkAdmin" group: AmazonVPCFullAccess (for network-related resources)
## "LinuxAdmin" group: AmazonEC2FullAccess (for EC2 instances)
## "DBAdmin" group: AmazonRDSFullAccess (for database-related resources)
## "CloudAdmin" group: AdministratorAccess (admin access)
## "Trainees" group: "ReadOnlyAccess" policy attached.
## 
## 
## How to : ./user_group_create.sh
## Authur : Andy Sarfo Frimpong
########################################################################################################################################

#!/bin/bash

# AWS region where you want to create the groups
AWS_REGION="us-east-1"

# Create the User Groups
for group_name in "NetworkAdmin" "LinuxAdmin" "DBAdmin" "CloudAdmin" "Trainees"; do
  aws iam create-group --group-name "$group_name" --region "$AWS_REGION"
done

# Attach policies to each group
aws iam attach-group-policy --policy-arn arn:aws:iam::aws:policy/AmazonVPCFullAccess --group-name "NetworkAdmin" --region "$AWS_REGION"
aws iam attach-group-policy --policy-arn arn:aws:iam::aws:policy/AmazonEC2FullAccess --group-name "LinuxAdmin" --region "$AWS_REGION"
aws iam attach-group-policy --policy-arn arn:aws:iam::aws:policy/AmazonRDSFullAccess --group-name "DBAdmin" --region "$AWS_REGION"
aws iam attach-group-policy --policy-arn arn:aws:iam::aws:policy/AdministratorAccess --group-name "CloudAdmin" --region "$AWS_REGION"

# Attach ReadOnlyAccess policy to Trainees group
aws iam attach-group-policy --policy-arn arn:aws:iam::aws:policy/ReadOnlyAccess --group-name "Trainees" --region "$AWS_REGION"

echo "User groups created successfully with policies attached."
