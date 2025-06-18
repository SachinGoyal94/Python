#in c++ it's switch   case _ is default case no need of break here
x=int(input("Enter age:"))
match x:
    case 0:
        print("You are a baby")
    case 18:
        print('''you are an adult''')
    case _ if(x<35):
        print("You are a young person ")
    case _ if(x>=35):
        print("You are an experienced person")
    case _ :
        print("Invalid age")