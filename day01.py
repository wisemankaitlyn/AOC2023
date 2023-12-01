# Day 01
# Kaitlyn Darst
# 12/01/2023

import csv

part1 = False

cal_doc = csv.reader(open("Input/day01input.txt", "r"))

cal_list = []

if part1:
    for line in cal_doc:
        cal_nums = []
        for c in line[0]:
            if c.isdigit():
                cal_nums.append(c)

        cal_list.append(int(cal_nums[0])*10 + int(cal_nums[-1]))

    print("Day 1, part 1 answer:")

else:
    for line in cal_doc:
        cal_nums = []
        str_num  = ""
        for c in line[0]:
            if c.isdigit():
                cal_nums.append(c)
                str_num = ""
            else:
                str_num = str_num + c
                if "one" in str_num:
                    cal_nums.append('1')
                    str_num = ""
                    str_num = str_num + c
                elif "two" in str_num:
                    cal_nums.append('2')
                    str_num = ""
                    str_num = str_num + c
                elif "three" in str_num:
                    cal_nums.append('3')
                    str_num = ""
                    str_num = str_num + c
                elif "four" in str_num:
                    cal_nums.append('4')
                    str_num = ""
                    str_num = str_num + c
                elif "five" in str_num:
                    cal_nums.append('5')
                    str_num = ""
                    str_num = str_num + c
                elif "six" in str_num:
                    cal_nums.append('6')
                    str_num = ""
                    str_num = str_num + c
                elif "seven" in str_num:
                    cal_nums.append('7')
                    str_num = ""
                    str_num = str_num + c
                elif "eight" in str_num:
                    cal_nums.append('8')
                    str_num = ""
                    str_num = str_num + c
                elif "nine" in str_num:
                    cal_nums.append('9')
                    str_num = ""
                    str_num = str_num + c

        cal_list.append(int(cal_nums[0]) * 10 + int(cal_nums[-1]))

    print("Day 1, part 2 answer:")

print(sum(cal_list))


