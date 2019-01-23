




try:
    s = None
    if s is None:
        print('s是空对象')

    print(len(s))

except Exception:
    print('空对象没有长度')
    raise NameError



# conn=cx_Oracle.connect('load/123456@localhost/ora11g')    #连接数据库
# c=conn.cursor()                                           #获取cursor
# x=c.execute('select sysdate from dual')                   #使用cursor进行各种操作
# x.fetchone()
# c.close()                                                 #关闭cursor
# conn.close()                                              #关闭连接


# a=0
# b=1
# c=3
# a=random.randint(1,10)
# b=random.randint(1,10)
# c=random.randint(1,10)
# d=random.randint(1,10)
# e=random.randint(1,10)
# f=random.randint(1,10)
# g=random.randint(1,10)
# h=random.randint(1,10)
# i=random.randint(1,10)
# str_a=str(a)
# str_b=str(b)
# str_c=str(c)
# str_d=str(d)
# str_e=str(e)
# str_f=str(f)
# str_g=str(g)
# str_h=str(h)
# str_i=str(i)
# 
# str_number=str_a+str_b+str_c+str(c)+str_d+str_e+str_f+str_g+str_h+str_i
# print(str_number)