import random

import pymysql as p
import sys
from PyQt5.QtWidgets import *
from PyQt5 import uic



conn = p.connect(host='localhost', port=3306, user='root', password='1234',
                              db='ham', charset='utf8')
cursor = conn.cursor()

# cursor.execute("SELECT menu FROM bom")
# m = cursor.fetchall()
#
# # 메뉴
# mm=[]
# for i in range(0,len(m)):
#     mm.append(m[i][0])
# print(mm)
# print(len(m))
#
#
# # 수량, 메뉴선택
# am=random.randint(1,5)
# me=random.randint(0,13)
#
# cursor.execute(f"select * from bom inner join inven2 on menu='{mm[me]}'")
# d = cursor.fetchall()
#
# # 재고에서 재료 빼기
# f=[]
# for i in range(0,22):
#     e=d[0][25+i] - am*(d[0][3+i])
#     f.append(e)
# print(f)
# print(am,"^^^")
# print(len(f))
# print(d[0][3])
# # element=['beef','chic','shirimp','hashbrown','egg','hub','pepper','bun','onion','tomato','yang','cheese','pic','mayo','stake_sauce','chechap','sugar','tartar_sauce','derry_sauce','potato','cola','sprite']
# # print(len(element))
# # print(element[21])
# print(f[0])
# cursor.execute("select * from el")
# element = cursor.fetchall()
# print(element[21][0])
#
# nn = []
# cc = []
# cursor.execute("select * from inven2")
# bb = cursor.fetchall()
# for i in range(0, 22):
#     nn.append(bb[0][i])
#     if nn[i]<30:
#         print("재고가 소진됨")
#         break
#
# print(nn,"@#@#@#!@#")
# print(nn[0])
#
# cursor.execute("select menu_price from bom")
# ho = cursor.fetchall()
# print(ho[13][0])
#
# cursor.execute("select * from sell")
# ha = cursor.fetchall()
# print(ha[0][1])
#
# cursor.execute("select * from sell")
# hg = cursor.fetchall()
# print(hg)
# print(hg[0][0],hg[0][2])
#
# cursor.execute("SELECT * FROM mae")
# mu = cursor.fetchall()
# print(mu)
# print(mu[0][1])
#
#
#
#
#
# cursor.execute("SELECT * FROM sell2")
# ma = cursor.fetchall()
# print(ma)
# k=len(ma)
# # 원래수치,
# print(ma[k-1],ma[k-2],ma[k-3])
# print(ma[2][2])
# a=[ma[k-1][0],ma[k-2][0]]

# f=[]
#     for i in range(0, 22):
#         e = hp[0][25 + i]-hp[0][3 + i]
#         f.append(e)
# print(a)
cursor.execute("select * from bom inner join inven2 on menu='해쉬브라운버거'")
hp = cursor.fetchall()
f=[]
for i in range(0, 22):
    e = hp[0][25 + i]-hp[0][3 + i]
    f.append(e)
print(len(f),'!!')
print(hp[0])
print(hp[0][25])
# while True:
#     f=[]
#     for i in range(0, 22):
#         e = hp[0][25 + i]-hp[0][3 + i]
#         f.append(e)





# (d[0][3+i])==0: break
# name은 테스트 / 상품은 mm[me] / 수량은 am / insertinto

# conn = p.connect(host='localhost', port=3306, user='root', password='1234',
#                               db='ham', charset='utf8')
# cursor = conn.cursor()
#
# cursor.execute("SELECT menu FROM bom")
# m = cursor.fetchall()
#
# 메뉴
# mm=[]
# for i in range(0,len(m)):
#     mm.append(m[i][0])
# print(mm)
# print(len(m))


# 수량, 메뉴선택
# am=random.randint(1,5)
# me=random.randint(0,13)
#
# cursor.execute(f"select * from bom inner join inven2 on menu='{mm[me]}'")
# d = cursor.fetchall()
#
# 재고에서 재료 빼기
# f=[]
# for i in range(0,22):
#     e=d[0][25+i] - am*(d[0][3+i])
#     f.append(e)
# print(f)
# print(am,"^^^")
# print(len(f))
# (d[0][3+i])==0: break
# name은 테스트 / 상품은 mm[me] / 수량은 am / insertinto

