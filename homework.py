import random

poker = [0, 0, 1, 1, 1, 1, 2, 2, 2, 2, 3, 3, 3, 3, 4, 4, 4, 4, 5, 5, 5, 5, 6, 6, 6, 6, 7, 7, 7, 7, 8, 8, 8, 8, 9, 9, 9,
         9, 10, 10, 10, 10, 11, 11, 11, 11, 12, 12, 12, 12, 13, 13, 13, 13]


# poker = [0, 0, 1, 2, 3, 4, 5, 6, 7, 8, 9, 10, 11, 12, 13]
# poker = [7,8,9,10,12]
# poker = [4,5,7,6,8]
# poker = [0, 0, 0, 0, 0]
# 随机抽牌
def get_list():
    poker1 = random.choice(poker)  # 从poker随机抽一张牌
    poker.remove(poker1)  # 移除数组中被抽取到的牌
    poker2 = random.choice(poker)  # 从poker随机抽一张牌
    poker.remove(poker2)  # 移除数组中被抽取到的牌
    poker3 = random.choice(poker)  # 从poker随机抽一张牌
    poker.remove(poker3)  # 移除数组中被抽取到的牌
    poker4 = random.choice(poker)  # 从poker随机抽一张牌
    poker.remove(poker4)  # 移除数组中被抽取到的牌
    poker5 = random.choice(poker)  # 从poker随机抽一张牌
    poker.remove(poker5)  # 移除数组中被抽取到的牌
    my_list = [poker1, poker2, poker3, poker4, poker5]
    return my_list


# 对我已经抽取的5张牌进行排序(从小到大)
def sort_list(my_list):
    for i in range(len(my_list) - 1):  # 这个循环负责设置冒泡排序进行的次数
        for j in range(len(my_list) - i - 1):  # ｊ为列表下标
            if my_list[j] > my_list[j + 1]:
                my_list[j], my_list[j + 1] = my_list[j + 1], my_list[j]
    print(my_list)
    return my_list


def isStraight(nums):
    if nums.count(0) == 5:
        print(True)
    else:
        cards = [x for x in nums if x != 0]
        # print(cards)
        # print(max(cards) - min(cards))
        return len(cards) == len(set(cards)) and max(cards) - min(cards) < 5


print(isStraight(sort_list(get_list())))
#
#
# # 逻辑运算，判断这5张牌是不是顺子
# def is_shunzi(sorted_list):
#     print(sorted_list)
#     for i in range(len(sorted_list)):
#         if len(sorted_list) - i == 1:
#             break
#         a = sorted_list[i + 1] - sorted_list[i]
#         if sorted_list[i] == 0:
#             sorted_list.remove(0)
#             print(sorted_list)
#             if len(sorted_list) == 2 and a in (1, 4):
#                 print(True, '是顺子')
#             if len(sorted_list) == 3 and a in (1, 2):
#                 print(False, '不是顺子')
#         if len(sorted_list) == 1 or len(sorted_list) == 0:
#             print('大小王0是自由数，是顺子')
#
#         if a != 1:
#             print(False, '不是顺子')
#             break
#         else:
#             print(True, '是顺子')
#
#     # print(b)
#     # for l in range(len(sorted_list)):
#     #     if len(sorted_list) - l == 1:
#     #         break
#     #     if 0 not in sorted_list and a == 4:  # 不存在大小王时
#     #         print(True, '是顺子')
#     #         break
#     #     if sorted_list.count(0) == 1 and b == 3:  # 存在一个大小王时
#     #         print(True, '5张牌中出现一张大小王，其他四张牌是由大到小排序的，0是自由数，是顺子')
#     #         break
#     #     if sorted_list.count(0) == 2 and c == 2:  # 存在两个大小王时
#     #         print(True, '5张牌中出现两张大小王，其他三张牌是由大到小排序的，0是自由数，是顺子')
#     #         break
#     #     if sorted_list.count(0) == 3 and d == 1:  # 存在一个大小王时
#     #         print(True, '5张牌中出现三张大小王，其他牌是由大到小排序的，0是自由数，是顺子')
#     #         break
#     #     if sorted_list.count(0) == 4 or sorted_list.count(0) == 5:  # 存在四个或五个大小王时
#     #         print(True, '5张牌中出现四张或五张大小王，0是自由数，是顺子')
#     #         break
#
#
# def main():
#     is_shunzi(sort_list(get_list()))
#
#
# main()
