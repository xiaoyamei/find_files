"""
功能：从指定文件夹里找出包含特定内容的文档
版本：V0.1
日期：2018/12/2
作者：肖亚梅
"""
import os


def findText(path, text):
    """
    在path目录下的文件中查找text内容，返回包含text的文档。
    :param path: 查找目录
    :param text: 要查找的内容的列表
    :return: 包含text的文件
    """
    files = []
    os.chdir(path)
    fileNames = os.listdir()
    for fileName in fileNames:
        # print(fileName)
        try:
            with open(fileName, 'r') as f:
                    content = f.read()
                    for i in text:
                        if i in content:
                            files.append(fileName)
                            break
        except:
            pass
    return files


def main():
    """
    主函数
    """
    path = "/Users/xiaoyamei/学习/Jmeter/apache-jmeter-2.11/bin"  # 要查找的文件夹
    text = ["PermSize=64m", "MaxPermSize=128m"]     # 要查找的内容
    files = findText(path, text)
    print(files)


if __name__ == "__main__":
    main()
