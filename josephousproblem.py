"""
JOSEPHOUS PROBLEM---Given N people standing in a circle, 1st person has a sword and killed the 2nd person and give a sword to the 3rd personand so on...
The challenge is to determine the position of the survivor at the end.
"""


n = int(input("Enter number of persons:"))
power = 1
while(power*2<=n):
        power *=2
result = (n-power)*2+1    #compute the final surviors position
print(f"{result}th person will survive at the end")
