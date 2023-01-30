firstname=input("Welcome to true friend power checker \n Enter your first name: ")
secondname=input("Enter your friend's first name: ")
name = firstname+secondname
lower_case_name =name.lower()
#check
t=lower_case_name.count("t")
r=lower_case_name.count("r")
u=lower_case_name.count("u")
e=lower_case_name.count("e")
true = t + r +u+e
f=lower_case_name.count("f")
r=lower_case_name.count("r")
i=lower_case_name.count("i")
e=lower_case_name.count("e")
n=lower_case_name.count("n")
d=lower_case_name.count("d")
friend = f+r+i+e+n+d
trueFriend = true+friend
if trueFriend > 8:
  print(f"You and your friend have a super fan power of {trueFriend}")
elif trueFriend > 5:
  print(f"You and your friend are normal friend with frind power of {trueFriend}")
else:
  print("You are not he or she friend ")
