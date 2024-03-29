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


def list_bucket_contents(my_bucket):
    for object_summary in my_bucket.objects.filter():
        print(object_summary.key)

def get_user_input(user_input, buckets):
    buckets = get_list_of_buckets()
    bucket_number = int(user_input)
    bucketchoice = (buckets[bucket_number])
    return bucketchoice

def main_func():
    program_running = True
    choose_bucket = True
    while program_running == True:
        while choose_bucket == True:
            print_all_buckets()
            buckets = get_list_of_buckets()
            users_input = raw_input("Please input the number of the bucket you would like to upload or delete a file from:  ")
            users_bucket = get_user_input(users_input, buckets)
            my_bucket = s3.Bucket(users_bucket)
            bucket_contents = []
            print("You have selected the following bucket:  " + users_bucket)

            print("###########################")

            print("Here is the contents of your chosen bucket")
            list_bucket_contents(my_bucket)
            choose_bucket = False

        user_choice = raw_input("Do you want to upload a file or delete a file from your chosen S3 bucket? please select upload or delete:   ")
        if user_choice == "upload":
            users_file_path = raw_input("Please input the path of the file that you want to upload e.g. /home/ec2-user/mew/    ")
            users_file = raw_input("Please input the name of the file that you wish to upload:  ")
            file_and_path = str(users_file_path) + "/" + str(users_file)
            print("You have chosen to upload the following file:   ")
            print(file_and_path)
            s3.meta.client.upload_file(file_and_path, users_bucket, users_file,ExtraArgs={'ACL':'public-read'})

            print("now your bucket contents is as follows:")
            print("--------------------------------------")
            list_bucket_contents(my_bucket)
        elif user_choice == "delete":
            print("You have chosen to delete a file from your bucket:  " + str(users_bucket))
            file_to_remove = raw_input("type the exact name of the file that you wish to delete for example gates.txt: ")
            s3.Object(users_bucket, file_to_remove).delete()
            print("Now your bucket looks as follows:  ")
            list_bucket_contents(my_bucket)

        else:
            print("You have chosen not to upload or delete a file")

        user_continue = raw_input("Would you like another transaction? (yes/no) ")
        if user_continue == "yes":
            program_running = True
            use_same_bucket = raw_input("Do you want to use the same bucket? (yes/no) ")
            if use_same_bucket == "yes":
                choose_bucket = False
            else:
                choose_bucket = True
        elif user_continue == "no":
            program_running = False

    return ""


print(main_func())
