import boto3

# Especifique a região da AWS
region = "us-est-1"

# Crie um cliente S3
client = boto3.client("s3", config=boto3.session.Config(region_name=region))

# Liste os buckets
buckets = client.list_buckets()

#Imprime os nomes dos buckets
for bucket in bucket["Buckets"]:
    nome=bucket["Name"]
    data=bucket["CreationDate"]
    print(f"Nome: {nome} - Data: {data}")