def func(time):
    if (time[2][2:4]=='am' or time[2][2:4]=='AM') and (int(time[0])<=11) and (int(time[0])>=1):
        return time
    if time[2][2:4]=='pm' or time[2][2:4]=="PM" and (int(time[0])<=11) and (int(time[0])>=1):
        time[0]=int(time[0][0:2])+12
        str(time[0])
        return time
    if (time[2][2:4] == 'am' or time[2][2:4] == 'AM') and (time[0]=='12'):
        time[0]='00'
        return time
    if time[2][2:4] == 'pm' or time[2][2:4] == "PM" and (time[0]== '12'):
        time[0]='12'
        return time
time=list(map(str,input().strip().split(":")))
lst=func(time)
print(f"{lst[0]}:{lst[1]}:{lst[2][0:2]}")
