#!/usr/bin/env python
import boto3

s3 = boto3.resource('s3')

def get_list_of_buckets():
    buckets = []
    for bucket in s3.buckets.all():
        buckets.append(bucket.name)
    return buckets

def print_all_buckets():
    buckets = get_list_of_buckets()
    print("Here are your buckets")
    j = 0
    while j < len(buckets):
        for i in buckets:
            print("bucket:  " + str(j) + "  " + i)
            j = j + 1
    print("--------------------------------------")
    bucketlength = len(buckets)
    print("You have " + str(bucketlength) + " Buckets")
    print("-------------------------------------")

def get_user_input(user_input, buckets):
    buckets = get_list_of_buckets()
    bucket_number = int(user_input)
    bucketchoice = (buckets[bucket_number])
    return bucketchoice

def main_func():
    print_all_buckets()
    buckets = get_list_of_buckets()
    users_input = raw_input("Please input the number of the bucket you would like to upload your file into:  ")
    users_bucket = get_user_input(users_input, buckets)
    print("You have selected the following bucket to upload file(s) to:  " + users_bucket)

    print("###########################")
    user_choice = raw_input("Do you want to go ahead and upload a file to your chossen S3 bucket?:   ")
    if user_choice == "yes":
        users_file_path = raw_input("Please input the path of the file that you want to upload e.g. /home/ec2-user/mew/    ")
        users_file = raw_input("Please input the name of the file that you wish to upload:  ")
        file_and_path = str(users_file_path) + "/" + str(users_file)
        print("You have chosen to upload the following file:   ")
        print(file_and_path)
        s3.meta.client.upload_file(file_and_path, users_bucket, users_file,ExtraArgs={'ACL':'public-read'})
    else:
        print("You have chosen not to upload a file")

    return ""


print(main_func())
