# Cria instancia na AWS

aws ec2 run-instances --image-id ami-0fc5d935ebf8bc3bc --instance-type t2.micro --count 1 --key-name vockey --security-group-ids sg-05d93882058e402ce --region us-east-1