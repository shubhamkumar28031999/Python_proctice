def time_convertter(s):
    hh=int(s[:2])
    mm=int(s[3:5])
    am_pm=s[6:]
    time=0
    if am_pm=="AM" and hh==12:
        hh=00
    if am_pm=="PM" and 1<=hh<=11 :
        hh+=12
    return 60*hh+mm

for _ in range(int(input())):
    time=time_convertter(input())
    ans=""
    for _ in range(int(input())):
        temp=input()
        start_time=time_convertter(temp[:8])
        end_time=time_convertter(temp[9:])
        # print(f"start_time={start_time}  end time ={end_time}   time={time}")
        if start_time<=time<=end_time:
            ans+="1"
        else:
            ans+="0"
    print(ans)

# n="12:00 PM"
# print(time_convertter(n))