import matplotlib.pyplot as plt
import sympy as sp
import numpy as np

# 2.编程计算f(x) = 3*x^2, 在(1, 2]区间积分与精确结果的差。
# 并做出相对误差与分割分数n=100， 200， 300...之间的关系曲线

def my_Func(x):
    # 设置定积分函数
    return 3*x**2

def my_Rectangle(a, b, n_max=2000):
    """
    设定最大分割数目n_max,默认为2000；
    返回此方法与精确解之间的差的绝对值组成的数组
    :param a:积分下限
    :param b:积分上限
    :param n_max: 区间最大分割数目
    :return diff: 返回误差数组
    """
    n = range(100, n_max+100, 100)
    diff = []
    x = sp.symbols('x')
    ex = sp.integrate(my_Func(x), (x, a, b))

    for each in n:
        x_range = np.arange(a, b, (b-a) / each)
        sum = 0
        h = (b - a) / each
        for i in x_range[:-1]:
            sum += h*my_Func(i)
        # print(sum)

        diff.append(abs(sum - ex)*100/ex)
        print("正在运行矩形法：%d%%" %(each*100/n_max))

    # plt.plot(n, diff, '*')
    # plt.show()

    return diff

def my_Trapezoid(a, b, n_max=2000):
    """
    设定最大分割数目n_max,默认为2000；
    返回此方法与精确解之间的差的绝对值组成的数组
    :param a:积分下限
    :param b:积分上限
    :param n_max: 区间最大分割数目
    :return diff: 返回误差数组
    """
    n = range(100, n_max+100, 100)
    diff = []
    x = sp.symbols('x')
    ex = sp.integrate(my_Func(x), (x, a, b))

    for each in n:
        x_range = list(np.arange(a, b, (b-a) / each)) # 分割区间
        h = (b - a) / each
        sum = 0
        for i in x_range:
            if x_range.index(i) == 0 or x_range.index(i) == n:
                sum += h * my_Func(i) / 2 # 计算首尾位置
            else:
                sum += h * my_Func(i)
        # print(sum)

        diff.append(abs(sum - ex)*100/ex)
        print("正在运行梯形法：%d%%" %(each*100/n_max))

    # plt.plot(n, diff, '*')
    # plt.show()

    return diff

def my_Palabola(a, b, n_max=200):
    """
    设定最大分割数目n_max,默认为2000；
    返回此方法与精确解之间的差的绝对值组成的数组
    :param a:积分下限
    :param b:积分上限
    :param n_max: 区间最大分割数目
    :return diff: 返回误差数组
    """
    n = range(100, n_max+100, 100)
    diff = []
    x = sp.symbols('x')
    ex = sp.integrate(my_Func(x), (x, a, b))

    for each in n:
        former = 0  # 存储y值之和
        odd = 0  # 存储奇数项之和
        even = 0  # 存储偶数项之和
        h = (b-a)/(6*each)
        x_range = np.arange(a, b, (b-a) / (2 * each)) # 分割区间
        x_range_list = list(x_range)

        for i in x_range:
            if x_range_list.index(i) == 0 or x_range_list.index(i) == 2 * each:
                former += my_Func(i)
                # print(my_Func(i))
                # print(former)
            else:
                if x_range_list.index(i) % 2 == 0:
                    even += my_Func(i) # 计算偶数位置
                    continue
                else:
                    odd += my_Func(i) # 计算奇数位置
                    continue
        sum = h*(former + 4 * odd + 2 * even)
        diff.append(abs(sum - ex)*100/ex)
        print("正在运行抛物线法：%d%%" %(each*100/n_max))
        continue

    # plt.plot(n, diff, '*')
    # plt.show()

    return diff

def text_save(filename, data):  # filename为写入CSV文件的路径，data为要写入数据列表.
    file = open(filename, 'a')
    for i in range(len(data)):
        s = str(data[i]).replace('[', '').replace(']', '')  # 去除[],这两行按数据不同，可以选择
        s = s.replace("'", '').replace(',', '') + '\n'  # 去除单引号，逗号，每行末尾追加换行符
        file.write(s)
    file.close()
    print("保存文件成功")

if __name__ == "__main__":

    # 设置最大分割数目
    n_max = 10000
    n = range(100, n_max + 100, 100)

    # 设定积分区间
    a = 1
    b = 2
    
    # 矩形法
    rectangle_diff = my_Rectangle(a, b, n_max=n_max)
    print('\n')
    # 梯形法
    trapezoid_diff = my_Trapezoid(a, b, n_max=n_max)
    print('\n')
    # 抛物线法
    palabola_diff = my_Palabola(a, b, n_max=n_max)
    print('\n')

    # 保存不同方法在不同分割份数下的相对误差结果
    text_save('定积分近似计算方法相对误差(%)/矩形法.txt', rectangle_diff)
    text_save('定积分近似计算方法相对误差(%)/梯形法.txt', trapezoid_diff)
    text_save('定积分近似计算方法相对误差(%)/抛物线法.txt', palabola_diff)

    # 绘制相对误差图像
    plt.plot(n, rectangle_diff, color='b', marker='^', linestyle='dashed')
    plt.plot(n, trapezoid_diff, color='r', marker='o', linestyle='dashed')
    plt.plot(n, palabola_diff, color='g', marker='*', linestyle='dashed')
    my_x_ticks = np.arange(0, n_max+100, 1000)
    my_y_ticks = np.arange(0, 3, 0.5)
    plt.xticks(my_x_ticks)
    plt.yticks(my_y_ticks)
    curve_label = ['Method_Rectangle_Diff', 'Method_Trapezoid_Diff', 'Method_Palabola_Diff']
    plt.xlabel('Setting n')
    plt.ylabel('Relative Error(%)')
    plt.legend(curve_label, loc='upper right')
    plt.savefig('三种定积分近似计算方法的相对误差与分割份数关系曲线.png', dpi=720)
    plt.show()