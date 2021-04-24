# get user email adress

email = input("What is your email adress?: ").strip()

# slice out user name

user = email[:email.index("@")]
print("Username: "+user)

# slice domain name

domain = email[email.index("@")+1 :]
print("Domain: "+domain)

# format message

output = "Your username is {} and your domain name is {}.".format(user,domain)

# display output message

print(output)


