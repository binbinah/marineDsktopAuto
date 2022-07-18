a = """
请查收下一航程出发的相关价格
SPOTON
最佳运输时间
最早到达
最早离港时间
周四, 21 7月 2022
NINGBO, CN
BOMAR RENAISSANCE
0.66 CO2(t) 每标准箱(TEU)
Service China Hong-Kong Philippines Indo Srv
周四, 28 7月 2022
JAKARTA, ID
6 天Duration information
直线
综合利率
2011
USD
/ 柜号
选择
SPOTON
周五, 22 7月 2022
NINGBO, CN
SITC ULSAN
0.76 CO2(t) 每标准箱(TEU)
Service China Vietnam Indonesia
周一, 01 8月 2022
JAKARTA, ID
9 天Duration information
直线
Spot舱位已满
SPOTON
周四, 28 7月 2022
NINGBO, CN
SITC SHEKOU
0.76 CO2(t) 每标准箱(TEU)
Service China Vietnam Indonesia
周一, 08 8月 2022
JAKARTA, ID
11 天Duration information
直线
Spot舱位已满
SPOTON
周二, 02 8月 2022
NINGBO, CN
CNC TIGER
0.66 CO2(t) 每标准箱(TEU)
Service China Hong-Kong Philippines Indo Srv
周三, 10 8月 2022
JAKARTA, ID
8 天Duration information
直线
综合利率
2011
USD
/ 柜号
选择
SPOTON
周四, 04 8月 2022
NINGBO, CN
SITC MINGCHENG
0.76 CO2(t) 每标准箱(TEU)
Service China Vietnam Indonesia
周一, 15 8月 2022
JAKARTA, ID
10 天Duration information
直线
Spot舱位已满
SPOTON
周三, 10 8月 2022
NINGBO, CN
BOMAR RENAISSANCE
0.66 CO2(t) 每标准箱(TEU)
Service China Hong-Kong Philippines Indo Srv
周四, 18 8月 2022
JAKARTA, ID
8 天Duration information
直线
综合利率
2011
USD
/ 柜号
选择
SPOTON
周四, 11 8月 2022
NINGBO, CN
SITC DECHENG
0.76 CO2(t) 每标准箱(TEU)
Service China Vietnam Indonesia
周一, 22 8月 2022
JAKARTA, ID
10 天Duration information
直线
综合利率
2011
USD
/ 柜号
选择
SPOTON
周六, 13 8月 2022
NINGBO, CN
HENG HUI 5
0.66 CO2(t) 每标准箱(TEU)
Service China Hong-Kong Philippines Indo Srv
周日, 21 8月 2022
JAKARTA, ID
8 天Duration information
直线
综合利率
2011
USD
/ 柜号
选择
© 2022 CNC
"""

print(a.split("SPOTON"))
for i in a.split("SPOTON"):
    if "综合利率" in i:
        print(i.replace("\n", ","))
