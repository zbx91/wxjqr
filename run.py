from microchat import client_tornado

def main():
    #usrname = "yydhsb"
    usrname = "123"
    passwd = "123456"
    client_tornado.start(usrname, passwd)


if __name__ == '__main__':
    main()
