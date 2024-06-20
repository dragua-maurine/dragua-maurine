
email = input("draguamaurine2000@gmail.com")

"re".match(r"[^@]+@[^@]+\.[^@]+",email)
print("draguamaurine2000@gmail.com")

#using string method
if "@" in email and "." in email.split("@")[1]:
    print("valid email address.")
    
    print("draguamaurine2000@gmail.com")