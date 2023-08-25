Authur: Andy Sarfo Frimpong

**Project Title: Automated User Migration and IAM Management in AWS**

**Project Overview:**

This project focuses on the seamless migration of a substantial user base from an on-premises system to Amazon Web Services (AWS) while ensuring efficient management of AWS Identity and Access Management (IAM) resources. The migration process is automated using a combination of Python and Bash scripts, guaranteeing data integrity and adherence to IAM best practices.

**Project Goals:**

1. Migrate over 100 users from an on-premises system to AWS.
2. Automate the migration process to reduce manual intervention and potential errors.
3. Implement secure and controlled access to AWS resources using IAM best practices.

**Project Phases:**

1. **Discovery & Planning:**
   - Gather detailed user data from the on-premises CSV file.
   - Identify required AWS services and resources for user access.
   - Devise a migration strategy based on user roles and permissions.
   - Define IAM policies for each user group.

2. **AWS Setup:**
   - Create or configure an AWS account if not already established.
   - Set up AWS Management Console and Command Line Interface (CLI) access.
   - Provision necessary AWS services like Amazon S3 buckets and Amazon RDS databases.

3. **Data Migration:**
   - Develop scripts to transform and migrate data from on-premises CSV to AWS.
   - Utilize Python script "sample_it_team_members_generator.py" to generate sample CSV data for IT team members and groups.

4. **IAM Management:**
   - Create user groups using Bash script "user_group_create.sh".
   - Attach AWS managed policies to groups based on roles:
     - NetworkAdmin: AmazonVPCFullAccess
     - LinuxAdmin: AmazonEC2FullAccess
     - DBAdmin: AmazonRDSFullAccess
     - CloudAdmin: AdministratorAccess
     - Trainees: ReadOnlyAccess

5. **Testing & Validation:**
   - Test migration and IAM processes with a subset of users.
   - Verify appropriate access based on user roles and permissions.
   - Test edge cases and error scenarios to ensure system resilience.

6. **Monitoring & Maintenance:**
   - Implement AWS CloudTrail and CloudWatch to monitor IAM activities.
   - Continuously monitor and maintain IAM resources, policies, and user groups.

**Sample Scripts:**

1. **Bash Script - user_group_create.sh:**
   - Set AWS_REGION for group creation.
   - Create IAM groups for NetworkAdmin, LinuxAdmin, DBAdmin, CloudAdmin, and Trainees.
   - Attach policies based on roles to respective groups.
   - Grant ReadOnlyAccess policy to Trainees group.
   - Print success message.

2. **Python Script - sample_it_team_members_generator.py:**
   - Generate a sample CSV file with IT team members and assigned groups.
   - Distribute team members evenly into groups.
   - Write data to "it_team_members.csv" file with Name and Group columns.

3. **Python Script - test_iam_user_create.py:**
   - Define IAM policy JSON for password change policy.
   - Check user existence using "user_exists" function.
   - Create users, assign to groups, and set up login profiles using "create_user_with_profile" function.
   - Read user details and group assignments from "it_team_members.csv".
   - Create users and assign to appropriate groups, considering policy enforcement.

**Multi-Factor Authentication (MFA):**
   - Enable MFA for users to enhance security.
   - Use Okta Authenticator app for MFA.
   - Create custom IAM policy "MFA_Required_And_Password_Actions_Policy" to enforce MFA and password-related actions.
   - Attach the policy to users, ensuring MFA activation for broader access.

**Conclusion:**

This project has provided practical insights into AWS IAM, policy creation, scripting, and security practices. By effectively automating user migration and managing IAM resources, the project demonstrates an adept understanding of IAM concepts, enforcement of least privilege, and Multi-Factor Authentication. The project's lessons learned, challenges overcome, and newfound expertise contribute to a robust skillset applicable across various cloud platforms and identity management systems.

---

Feel free to further customize and elaborate on the different sections as needed. If you have any additional details you'd like to include or any further revisions, please let me know!
