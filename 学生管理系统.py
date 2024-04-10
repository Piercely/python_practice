# 导入模块
import os
import re

# 建立一个名为student.text的文本用于保存文件

fileName = 'student.txt'


# 定义函数main()
def main():
    while True:
        menu()
        choice = int(input('请输入您的程序指令：'))
        if choice in [0, 1, 2, 3, 4, 5, 6]:
            if choice == 0:
                print("您确定要退出吗？yes/no")
                answer = input()
                if answer == 'yes':
                    print('感谢您的使用！！！')
                    break  # 终止
                else:
                    continue  # 中止
            elif choice == 1:
                insert()
            elif choice == 2:
                delete()
            elif choice == 3:
                search()
            elif choice == 4:
                total()
            elif choice == 5:
                show()
            elif choice == 6:
                sort()
        else:
            print('输入的指令不在范围内，请重新输入！！！')


def menu():
    print('==============================学生信息管理系统==============================')
    print('︽︽︽︽︽︽︽︽︽︽︽︽︽︽︽︽︽功能菜单︽︽︽︽︽︽︽︽︽︽︽︽︽︽︽︽')
    print("*" * 74)
    print("******", " " * 60, "******")
    print("******\t    1.添加学生信息", " " * 18, "4.统计学生总人数\t    ******")
    print("******\t    2.删除学生信息", " " * 18, "5.显示所有学生信息    ******")
    print("******\t    3.查询学生信息", " " * 18, "6.排序(以总成绩分数)  ******")
    print("******\t    0.退出学生信息管理系统", " " * 32, "******")
    print("******", " " * 60, "******")
    print("*" * 74)
    print('︾︾︾︾︾︾︾︾︾︾︾︾︾︾︾︾︾︾︾︾︾︾︾︾︾︾︾︾︾︾︾︾︾︾︾︾︾')


def save(lst):
    stu_txt = open(fileName, 'a', encoding='utf-8')
    for item in lst:
        stu_txt.write(str(item) + '\n')
    stu_txt.close()


# 录入学生信息
def insert():
    global phone
    student_list = []
    while True:
        id = input('请输入学号: ')
        if not id:
            break
        name = input('请输入姓名: ')
        if not name:
            break
        sex = input('请输入性别: ')
        if not sex:
            break
        # phone = input('请输入手机号: ')
        # if not phone:
        count = 0
        for i in range(1, 4):
            phone = input("请输入你的手机号： ")
            # 利用正则表达式进行限定
            tel = re.match(r"^1[3456789]\d{9}$", phone)
            if tel:
                print("输入成功!")
                break
            if tel != phone:
                count += 1
            if (count == 3):
                print("录入失败,请30秒后重试！")
            if (count != 3):
                print("录入错误，请核对你的手机号！")
        try:
            # 智育分满分70分，德育分满分20分，体育分满分10分
            zyf = int(input('请输入你的智育分：'))
            dyf = int(input('请输入你的德育分：'))
            tyf = int(input('请输入你的体育分：'))
        except:
            print('请您输入数字成绩！')
            continue
        # 将录入的学生信息保存到字典中
        student = {'id': id, 'name': name, 'sex': sex, 'phone': phone, 'zyf': zyf, 'dyf': dyf, 'tyf': tyf}
        # 将学生信息添加到列表中
        # 可删！！！！！
        student_list.append(student)
        answer = input('是否继续添加？yes/no\n')
        if answer == 'yes':
            continue
        else:
            break
    # 保存学生信息
    save(student_list)  # 封装
    print('学生信息录入完毕!!!')


def show_student(lst):
    # 传过来空列表
    if len(lst) == 0:
        print('没有查找到该生信息！')
        return
    # 定义标题显示格式
    format_title = '{:^5}\t{:^23}{:^5}\t{:^11}\t{:^12}\t{:^10}\t{:^10}\t{:^6}\t{:^6}\t'
    print(format_title.format('学号', '姓名', '性别', '手机号', '智育分', '德育分', '体育分', '总成绩', '分数等级'))
    # 定义内容的显示格式
    format_data = '{:^6}\t{:^6}\t{:^6}\t{:^31}{:^3}\t{:^10}\t{:^9}\t{:^12}\t{:^12}\t'
    for item in lst:
        sum = int(item['zyf']) + int(item['dyf']) + int(item['tyf'])
        # grade等级的使用
        grade = ''
        if sum >= 85:
            grade = 'A'
        if 75 <= sum < 85:
            grade = 'B'
        if 65 <= sum < 75:
            grade = 'C'
        if 60 <= sum < 65:
            grade = 'D'
        if sum < 60:
            grade = 'error'
        # sum,grade的输出格式不同
        # format_data.format(sum,grade))
        print(format_data.format(item['id'], item['name'], item['sex'], item['phone'],
                                 item['zyf'], item['dyf'], item['tyf'],
                                 sum, grade))
        print('全部学生信息显示完毕!!!')


# 查询学生信息
def search():
    while True:
        stu_query = []
        id = ''
        # 判断文件是否存在
        if os.path.exists(fileName):
            # if的使用
            if id == '':
                id = input('请输入要查找的学生学号：')
            else:
                print('您的输入有误，请重新输入!')
                continue
            # 如果文件存在，并且用户输入了正确的查询标号，则打开文件
            with open(fileName, 'r', encoding='utf-8') as rfile:
                students = rfile.readlines()
            # 转换为字典类型
            for item in students:
                d = dict(eval(item))
                if id != '':
                    if id == d['id']:
                        stu_query.append(d)  # 追加
            # 显示查询结果
            show_student(stu_query)
            # 是否继续查询其他学生信息
            answer = input('还要查询其他学生吗？yes/no\n')
            if answer == 'yes':
                continue
            else:
                break
        else:
            print('学生信息不存在！')
            return
    print('学生信息查询结束,请进行下一步操作!!!')


# 删除学生信息
def delete():
    while True:
        student_id = input('请输入要删除学生的学号:')
        if student_id != '':
            if os.path.exists(fileName):
                with open(fileName, 'r', encoding='utf-8') as file:
                    student_old = file.readlines()
            else:
                student_old = []
            flag = False  # 标记是否删除
            if student_old:
                with open(fileName, 'w', encoding='utf-8') as wfile:
                    d = {}
                    for item in student_old:
                        d = dict(eval(item))  # 将字符串转换为字典
                        if d['id'] != student_id:
                            wfile.write(str(d) + '\n')
                        else:
                            flag = True
                    if flag:
                        print(f'学号为{student_id}的学生信息已经删除')
                    else:
                        print(f'学生表中没有找到学号为{student_id}的学生')
            else:
                print('学生表已中无任何学生个人信息')
                break
            show()  # 重新显示所有学生信息
            answer = input('是否继续删除？yes/no\n')
            if answer == 'yes':
                continue
            else:
                break
    print('删除学生信息已结束,请你进行下一步操作!!!')


# 统计学生总人数
def total():
    # 判断文件是否存在，如果存在则打开文件，读取信息
    if os.path.exists(fileName):
        with open(fileName, 'r', encoding='utf-8') as rfile:
            students = rfile.readlines()
            # 判断读取到的学生信息是否为空
            if students:
                print('一共有{}名学生'.format(len(students)))
            else:
                print('学生系统中还没有录入学生信息！')
    else:
        print('学生信息不存在！')
        return
    print('学生总人数统计完毕，请进行下一步操作!!!')


# 显示所有学生信息
def show():
    student_list = []
    # 判断文件是否存在，如果存在则打开文件，读取信息
    if os.path.exists(fileName):
        with open(fileName, 'r', encoding='utf-8') as rfile:
            students = rfile.readlines()
            # 判断读取到的学生信息是否为空
            if students:
                for item in students:
                    student_list.append(eval(item))
                # 展示学生信息
                show_student(student_list)
            else:
                print('学生文件中还没有录入学生信息！')
    else:
        print('学生文件不存在！')
        return
    print('学生信息已成功显示，请你进行下一步操作!!!')


# 对总学生成绩进行排序
def sort():
    # 判断文件是否存在，如果存在则打开文件，读取信息
    if os.path.exists(fileName):
        with open(fileName, 'r', encoding='utf-8') as rfile:
            students_list = rfile.readlines()
        students_new = []
        # 判断读取到的学生信息是否为空
        if students_list:
            # 将所有的item加入到students_new中
            for item in students_list:
                d = dict(eval(item))
                students_new.append(d)
                # 利用匿名函数与sort方法进行排序
                # True为降序，False升序
                students_new.sort(key=lambda x: int(x['zyf']) + int(x['dyf']) + int(x['tyf']),
                                  reverse=True)
            # 将排序后的成绩进行输出
            show_student(students_new)
    print('学生信息排序完成并成功显示，请你进行下一步操作!!!')


if __name__ == '__main__':
    main()
