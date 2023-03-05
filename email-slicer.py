# Python 3.10.1
# Encoding UTF-8
# This program takes an email address and matches the domain name to
# the email service provider

# The strip function removes whitespaces
email = input("Please provide your email address ").strip()

username = email[:email.index("@")]
domain_name = email[email.index("@")+1:]

# format_ = f"Your user name is '{username}' and your domain is '{domain_name}'"
# print(format_)

if domain_name == "gmail.com":
    print("Hey " + username + " I see that you are registered with Google. That's brilliant.")

elif domain_name == "yahoo.com":
    print(f"Hey {username} I see that you are registered with Yahoo. That's excellent.")

else:
    print("Hey " + username + " looks like you've got your own custom setup at " + domain_name + ". Impressive!!!")
