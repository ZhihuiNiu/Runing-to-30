a=['zhangsan','lisi','zhaowu']
b='Hello,my dear friend '
c='l would like you to have dinner with me'


for i in range(len(a)):
    print(b+  a[i]+','+c)

name_list_un=[]
b_un='The guest who can not come in time'
for i in range(len(a)-1):
    # name_list_un=name_list_un.append(a[i])不能使用此方式进行更改变量
    print(name_list_un.append(a[i]))
print(name_list_un)

new_guest=[]
new_guest.append(input('please input new guest name:'))
# print(new_guest)
a.insert(0,new_guest)
print(a)
