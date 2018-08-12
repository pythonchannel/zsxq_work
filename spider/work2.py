# 星球作业2#

def work1():
    '''#  1. 将一个列表的数据复制到另一个列表中。'''
    a = [111, 222, 333]
    b = a[:]
    print(b)


def work2():
    ''' 2. 利用条件运算符的嵌套来完成此题：学习成绩=90分的同学用A表示，60-89分之间的用B表示，60分以下的用C表示。'''

    loop = True

    while (loop):
        score = input('请输入你的分数,退出请输入q：')
        if score == 'q':
            print('已经退出了！')
            break

        try:
            score = int(score)
            if score >= 90:
                print('A')
            elif score >= 60 and score <= 89:
                print('B')
            elif score < 60:
                print('C')
        except Exception as e:
            print('输入无效，请重新输入！')


def work3():
    '''#  3. 对10个数进行排序。'''
    N = 10
    # input data
    print('请输入10个数字:\n')
    l = []
    for i in range(1, N + 1):
        try:
            l.append(int(input('输入第{}个数字:'.format(i))))
        except:
            print('输入数据无效，以0替代')
            l.append(int(0))
    print()

    # 排列10个数字
    for i in range(N - 1):
        min = i
        for j in range(i + 1, N):
            if l[min] > l[j]: min = j
        l[i], l[min] = l[min], l[i]

    print('排列之后：')

    for i in range(N):
        print(l[i])


from sys import stdout


def work4():
    '''#  4. 从键盘输入一些字符，逐个把它们写到磁盘文件上，直到输入一个 # 为止。'''
    filename = input('输入文件名:\n')
    fp = open(filename, "w")
    ch = input('输入字符串:\n')
    while ch != '#':
        fp.write(ch)
        stdout.write(ch)
        ch = input('')
    fp.close()


def work5():
    '''#  5. 输出 9*9 乘法口诀表。'''
    for x in range(10):
        for y in range(1, x + 1):
            print(str(y) + '*' + str(x) + '=' + str(y * x) + '\t', end='')  # 注意这里加上end = ''是防止换行.
        print()

# 调用,调用那个方法就去掉那行注释

# work1()
# work2()
# work3()
# work4()
# work5()
