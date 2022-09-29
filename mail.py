import poplib

a = poplib.POP3_SSL(host="pop3s.hiworks.com", port=995)

for i in a.list()[1]:
    print(i.decode("utf-8"))
