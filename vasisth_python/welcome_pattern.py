x=int(input(""))
c='.|.'
dash='-'
welcome='welcome'
thickness=x
for i in range(thickness):
    print((c*(thickness-i-1)).ljust(thickness)).rjust(thickness*6)+(c*i).rjust(thickness-1)+c+(c*i).ljust(thickness-1)+((c*(thickness-i-1)).rjust(thickness))