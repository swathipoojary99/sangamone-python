hour=int(input("Enter the Hour"))
minute=int(input("Enter the Minutes"))
hrangle=hour*30+minute*(30/60)
minangle=minute*6
result=0.0
if(hrangle>minangle):
    result=hrangle-minangle
else:
    result=minangle-hrangle
if(result>180):
    print("the least angle is",360-result)
else:
    print("the angle is",result)
