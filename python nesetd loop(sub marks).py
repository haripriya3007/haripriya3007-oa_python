##print pass if all the marks are above 40,else print fail:
tamil=int(input("enter the tamil marks"))
english=int(input("enter the english marks"))
maths=int(input("enter the maths marks"))
science=int(input("enter the science marks"))
social=int(input("enter the social marks"))
if tamil > 40:
    if english > 40:
        if maths > 40:
            if science > 40:
                if social > 40:
                    print("pass")
                else:  
                    print("fail")
            else:
                print("fail")
        else:
            print("fail")
    else:
        print("fail")
else:
    print("fail")
