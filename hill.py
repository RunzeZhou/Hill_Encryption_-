import re       # 添加库
import os       # 添加库


class Matrix:
    """设计矩阵类，用以储存加密矩阵，加密与解密"""
    def __init__(self):
        """初始化类"""
        self.mat = [[0, 0, 0], [0, 0, 0], [0, 0, 0]]        # 初始化加密矩阵
        self.in_mat = [[0, 0, 0], [0, 0, 0], [0, 0, 0]]     # 初始化类逆矩阵
        self.det = 0                                        # 初始化行列式

    def get_in_mat(self):
        """求加密矩阵的类逆矩阵"""
        p = 1
        while p % self.det != 0:
            p += 37                                                                         # 计算可以整除行列式的值
        m = int(p / self.det)                                                               # 计算出伴随矩阵前的系数
        for i in range(0, 3):                                                               # 求伴随矩阵
            for j in range(0, 3):
                trans1 = self.mat[(i+1) % 3][(j+1) % 3] * self.mat[(i+2) % 3][(j+2) % 3]    # 计算aij子矩阵的行列式
                trans2 = self.mat[(i+2) % 3][(j+1) % 3] * self.mat[(i+1) % 3][(j+2) % 3]
                trans = trans1 - trans2
                self.in_mat[j][i] = trans * m                                               # 填充伴随矩阵

    def set_mat(self, re_mat, det):
        """重设矩阵参数"""
        self.det = det                              # 重新设置行列式
        for i in range(0, 3):                       # 重新设置加密矩阵
            for j in range(0, 3):
                self.mat[i][j] = re_mat[i][j]
        self.get_in_mat()                           # 重新设置类逆矩阵

    def encrypt(self, d_letters):
        """对数值进行加密"""
        e_letters = []                              # 初始化存放密文编码的列表
        for i in range(0, 3):                       # 计算密文编码
            x = 0
            for j in range(0, 3):                   # 计算加密矩阵与向量的积
                x += self.mat[i][j] * d_letters[j]
            e_letters.append(x % 37)                # 对算得的向量的元素模37
        return e_letters                            # 返回密文编码矩阵

    def decrypt(self, e_letters):
        """对数值进行解密"""
        d_letters = []                              # 初始化存放明文编码的矩阵
        for i in range(0, 3):                       # 计算明文编码
            x = 0
            for j in range(0, 3):                   # 计算类逆矩阵与密文向量的积
                x += (self.in_mat[i][j] * e_letters[j]) % 37
            d_letters.append(x % 37)                # 对算得的向量元素模37
        return d_letters                            # 返回密文编码矩阵


def determinant(mat):
    """计算一个3阶矩阵的行列式。"""
    mult = 0
    for i in range(0, 3):                                   # 使用拉普拉斯展开计算行列式
        sub_det = mat[(i+1) % 3][1] * mat[(i+2) % 3][2]     # 计算2阶矩阵行列式
        sub_det -= mat[(i+2) % 3][1] * mat[(i+1) % 3][1]
        mult += sub_det * mat[i][0]
    return mult                                             # 返回行列式的值


def transform(ch):
    """将字符转化为编码"""
    o = ord(ch)                     # 将字符转换为ascii码
    if o == 45:                     # 转换“-”
        o = 0
    elif (o < 58) and (o > 48):     # 转换数字1~9
        o -= 48
    elif o == 48:                   # 转换数字0
        o = 10
    elif (o < 91) and (o > 64):     # 转换大写字母
        o -= 54
    elif (o < 123) and (o > 96):    # 转换小写字母
        o -= 86
    return o                        # 返回转换值


def in_transform(n):
    """将编码转换为字符"""
    if n == 0:                      # 转换“-”
        n += 45
    elif (0 < n) and (n < 10):      # 转换数字1~9
        n += 48
    elif n == 10:                   # 转换数字0
        n = 48
    elif 10 < n:                    # 转换大写字母
        n += 54
    c = chr(n)                      # 将ascii码转换为字符
    return c                        # 返回字符


def char_to_int(strings):
    """将输入的字符串转化为可运算的矩阵"""
    n_list = re.split('(...)', strings)             # 字符分组
    nums = []                                       # 初始化编码存放列表
    for i in range(0, len(n_list)):                 # 将分组字符转换为编码
        if len(n_list[i]) == 3:
            t = []                                  # 创建临时列表
            for j in range(0, 3):
                t.append(transform(n_list[i][j]))   # 将编码放入临时列表
            nums.append(t)                          # 将临时列表放入编码存放列表
        elif (len(n_list[i]) < 3) and (len(n_list[i]) != 0):
            t = [0, 0, 0]                           # 初始化临时列表
            for j in range(len(n_list[i])):
                t[j] = transform(n_list[i][j])      # 将编码放入临时列表
            nums.append(t)                          # 将临时列表放入编码存放列表
    return nums                                     # 返回编码存放列表


def int_to_char(ints):
    """将矩阵转换为字符串"""
    chs = []                                # 初始化字符存放矩阵
    for i in range(len(ints)):              # 将编码转换为字符
        for j in range(3):
            chs.append(in_transform(ints[i][j]))
    chas = "".join(chs)                     # 合并为字符串
    return chas                             # 返回字符串


def content():
    """目录页面"""
    print("1、设置密钥")
    print("2、文段加密")
    print("3、文段解密")
    print("4、退出系统")


print("希尔加密系统。")
content()               # 显示目录
x_mat = Matrix()        # 创建加密矩阵类
set_m = False           # 初始化矩阵填充检测
con = True              # 初始化系统退出检测

s = input("\n请输入所需任务对应的数字：")
s = int(s)

while con:

    if s == 1:
        # 设置加密矩阵
        os.system("cls")                                                    # 清屏，保证界面整洁
        e_mat = [[0, 0, 0], [0, 0, 0], [0, 0, 0]]                           # 初始化加密矩阵的接受矩阵

        for nu in range(0, 3):
            numbers = input(f"请输入第{nu+1}行的数字(用空格隔开不同的数字)")       # 接受加密矩阵的数字
            num_list = re.split(" ", numbers)                               # 将字符串分割为数字填入列表
            if len(num_list) != 3:                                          # 判断输入是否合规
                print("输入错误！")
                break
            for q in range(0, 3):                                           # 将列表填入接受矩阵
                e_mat[nu][q] = int(num_list[q])
        d = determinant(e_mat)                                              # 计算矩阵行列式

        if d % 37 == 0:                                                     # 判断矩阵是否满足加密矩阵的条件
            print("输入错误！")
            break
        x_mat.set_mat(e_mat, d)                                             # 重设加密矩阵类
        set_m = True                                                        # 将矩阵填充设置为真
        print("设置成功")

        os.system("pause")                                                  # 程序暂停，允许用户进行记录
        os.system("cls")                                                    # 清屏，保证界面整洁
        content()                                                           # 接受下一步指令
        s = input("\n请输入所需任务对应的数字：")
        s = int(s)

    elif s == 2:
        # 进行加密并输出密文
        os.system("cls")                                    # 清屏，保证界面整洁
        if not set_m:                                       # 检测是否已经输入加密矩阵
            print("未输入加密矩阵！")
            break

        o_sentence1 = input("请输入需要加密的文字：")           # 接受需要加密的文字
        o_mat1 = char_to_int(o_sentence1)                   # 将明文文字转换为明文编码
        s_mat1 = []                                         # 初始化存放密文编码的矩阵
        for tu in range(len(o_mat1)):                       # 将明文编码转化为密文编码并存入矩阵
            s_mat1.append(x_mat.encrypt(o_mat1[tu]))
        s_sentence1 = int_to_char(s_mat1)                   # 将密文编码转化为密文并以字符串形式保存
        print(s_sentence1)                                  # 输出密文

        os.system("pause")                                  # 程序暂停，允许用户进行记录
        os.system("cls")                                    # 清屏，保证界面整洁
        content()                                           # 接受下一步指令
        s = input("\n请输入所需任务对应的数字：")
        s = int(s)

    elif s == 3:
        os.system("cls")                                    # 清屏，保证界面整洁
        if not set_m:                                       # 检测是否已经输入加密矩阵
            print("未输入加密矩阵！")
            break

        s_sentence2 = input("请输入需要解密的文字：")           # 接受需要解密的文字
        s_mat2 = char_to_int(s_sentence2)                   # 将密文文字转换为密文编码
        o_mat2 = []                                         # 初始化存放明文编码的矩阵
        for tu in range(len(s_mat2)):                       # 将密文编码转化为明文编码并存入矩阵
            o_mat2.append((x_mat.decrypt(s_mat2[tu])))
        o_sentence2 = int_to_char(o_mat2)                   # 将密文编码转化为密文并以字符串形式保存
        print(o_sentence2)                                  # 输出密文

        os.system("pause")                                  # 程序暂停，允许用户进行记录
        os.system("cls")                                    # 清屏，保证界面整洁
        content()                                           # 接受下一步指令
        s = input("\n请输入所需任务对应的数字：")
        s = int(s)

    elif s == 4:
        con = False                             # 设置系统退出检测，退出程序

    else:
        # 错误示警
        os.system("cls")                        # 清屏，保证界面整洁
        print("输入错误！")
        content()                               # 重新显示目录界面并允许用户重新选择
        s = input("请输入所需任务对应的数字：")
        s = int(s)

print("程序结束！")
os.system("pause")          # 程序暂停，允许用户进行记录
