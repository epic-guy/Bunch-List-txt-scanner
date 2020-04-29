data={}
with open('105K_YAHOO_MAIL_ACCESS by ThaNos.txt','r') as f:
    for i in f.readlines():
        txt=i.split(':')
        data[txt[0].split('@')[0]]=(txt[0],txt[1])

a=input('Enter name:')

for i in data.keys():
    if a in i:
        print("Email ID:",data[i][0])
        print("Password:",data[i][1])
