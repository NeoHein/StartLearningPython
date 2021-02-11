from deftest import Name_
UsrName = input("Enter Your Name!")
print(Name_(UsrName))
UserName_logs = open("User.log", "a")
UserName_logs.write("UserNames: " + UsrName + "\n")
UserName_logs.close()
