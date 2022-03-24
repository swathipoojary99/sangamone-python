list1=input("enter keys list:").split()
list2=list(map(int,input("enter values list:").split()))
if(len(list1)==len(list2)):
    dict1={}
    j=0
    for key in list1:
        val=list2[j]
        j+=1
        dict1[key]=val
    print(f"result dictionary {dict1}")
else:
    print("length of two lists must be same to create a dictionary")
