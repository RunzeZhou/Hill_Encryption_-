# Hill_Encryption_-
希尔加密是一种密文与原文之间非一一对应的一种加密方式。其具有保密性高的特点。但是只依靠人力运算进行加密或解密很难对大量的文本进行处理，引入计算机程序可以解决这个问题。本程序允许用户输入一个3阶的加密矩阵，并使用这个矩阵进行加密与解密。 本程序依赖python3.10进行编写，可以通过直接运行可执行文件使用。

# 程序实现方法与说明
使用三阶矩阵进行希尔加密的基本方法为：
1、建立明文字母与表值的关系：
为便于读写，增大加密矩阵使用的灵活度（后续将说明原因），本程序拟采用共有37个字符的字符—编码对照表，包含字母a~z（大小写自动转换，统一为大写），数字0~9，空格
注：为便于阅读，防止空格出现在句首时无法被看见，故“-”字符用来替代空格。

2、构造一个加密矩阵：
本程序的加密矩阵为3阶方阵，方阵为该加密系统的密钥，任何的加密与解密均通过他的运算实现。
加密矩阵并不可以随机选取，而是有一定条件的：其行列式的值不能够为0，也不能够是37的质因数的倍数（即37的倍数）。具体证明将在  步骤中给出。
因为37是质数，对加密矩阵的行列式的要求就相对简单。如果明文共有26个，则所有行列式为2的倍数的矩阵均不能够作为加密矩阵。这对于使用者十分不利。而且由于电脑算力的实际限制，如果使用元素过大的矩阵进行加密，会缩短加密与解密的时间，造成效率降低。因此使用有质数个明文的编码方式更具有优势。

3、将输入的明文分组，3个一组，不足3个的填入“-”以补充。计算出对应的表值并写成向量的形式，将该向量与加密矩阵相乘，将大于等于37的元素模37，得到密文的向量值。

4、将密文的向量值按照编码表，找出相应的密文。

使用三阶矩阵进行希尔加密的基本方法为：
1、将输入的密文分组，3个一组，因加密后的密文位数必定为3的倍数，故此处不需要补充。计算出对应的表值并写成向量的形式，

2、求解密的“类逆矩阵”：
类逆矩阵与对加密矩阵求逆的过程类似：
由克莱姆法则可以得到：A^(-1)=1/det⁡(A)  adj(A)。我们希望得到的类逆矩阵是由整数组成的矩阵。对于一个又整数组成的矩阵，易得adj(A)也是由整数组成的矩阵。而1/det⁡(A) 可能产生分数，故A^(-1)中也可能产生分数。因此我们可以将1/det⁡(A) 变换一下：因为1/det⁡(A)   det⁡(A)=1，故若1/det⁡(A) 为分数时，将1变为满足模37为1的数m，且使得该数为det⁡(A)的倍数。此时将得到的d=m/det⁡(A) 作为系数与adj(A)数乘，即可得到类逆矩阵。

3、将第1步的向量与第2步的类逆矩阵相乘，再将乘积模37，得到明文对应的向量。注意，在相乘过程中，类逆矩阵与向量的两个元素的积超过36，也应模37。

4、将得到的向量按照编码表翻译成明文并输出。

# 不足之处与可能的优化方向
本程序实现了一种运用希尔加密的方法进行文段加密和解密，但仍存在一些问题：首先，运行速度不够快，在对较长的语段进行加密与解密时可能需要一段时间；其次，本程序遇到输入错误则大多直接终止，且在输入加密矩阵时多输或少输空格会导致程序错误，对输入不友好；同时，未进行任何外观优化，可读性与操作性并不强。以上可作为可能的优化方向。
