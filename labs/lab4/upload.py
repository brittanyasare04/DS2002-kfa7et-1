import boto3
import requests

r = requests.get("https://upload.wikimedia.org/wikipedia/commons/1/19/Flag_of_Ghana.svg")
with open("gh_flag.png", "wb") as f:
    f.write(r.content)

s3 = boto3.client('s3', region_name='us-east-1')

file_name = "gh_flag.png"
bucket_name = "ds2002-kfa7et"
expiration_time = 604800


s3.upload_file(file_name, bucket_name, file_name, ExtraArgs={"ContentType": "image/png"})

url = s3.generate_presigned_url("get_object", Params={"Bucket": bucket_name, "Key": file_name}, ExpiresIn=604800)

print(url)
