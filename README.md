This script is designed to be run on an EC2 instance running Amazon Linux 2, and with an IAM role to give the instance access to S3 so that the access key ID and secret access key ID details do not have to be stored locally on the instance.

On the EC2 instance run the following commands:

sudo yum install python-pip
sudo pip install boto3
