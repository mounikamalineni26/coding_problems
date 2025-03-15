n = int(input("Enter number of persons:"))
power = 1
while(power*2<=n):
        power *=2
result = (n-power)*2+1    #compute the final surviors position
print(f"{result}th person will survive at the end")
