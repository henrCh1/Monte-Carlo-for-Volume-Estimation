# -*- coding: utf-8 -*-
"""
Created on Fri Apr 28 15:03:28 2023

@author: 86319
"""

from random import uniform

# 生成一个 [m, n] 之间的随机小数
def monte_carlo_integration(num_trials):
    count = 0  # 统计曲线下投点数
    density = 1  # 密度
    for i in range(int(num_trials)):
        x, y, z = uniform(-1, 1), uniform(-1, 1), uniform(-1, 1)  # 生成随机数
        if x ** 2 + y ** 2 + z ** 2 <= 1 and x ** 2 + y ** 2 >= 0.5 ** 2:
            count += 1
    volume = 8 * count / num_trials  # 计算体积
    return volume * density

# 调用函数并输出结果
print(monte_carlo_integration(1000000))
