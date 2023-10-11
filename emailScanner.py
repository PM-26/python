# scan email 
# form a tuple 
# user name 
# domain

email=input("Enter an email->")
split=email.find("@")
username=email[:split]
domain=email[split:]
tuple=(username,domain)
print(tuple)