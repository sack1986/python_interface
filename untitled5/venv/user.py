

def userLogin():
    zidian={}
    userInfo=open("D:\\Users\\Administrator\\PycharmProjects\\untitled\\venv\\user.txt")
    for myUser in userInfo:
        (name,password)=myUser.strip().split("、")
        zidian[name]=password

    print(zidian)

if __name__=="__main__":
    userLogin()