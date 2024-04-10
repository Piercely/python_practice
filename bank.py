import random


class bankUser:
    # 卡号，用户姓名，身份证号，手机，预存，密码
    Count_id = ""
    Count_Name = ""
    Count_IDCard = ""
    Count_phone = ""
    Count_Money = 0.00
    Count_password = ""
    Count_Root = True

    def __init__(self, Count_id, Count_IDCard, Count_Name, Count_phone, Count_Money, Count_password, Count_Root):
        self.Count_id = Count_id
        self.Count_IDCard = Count_IDCard
        self.Count_phone = Count_phone
        self.Count_Money = Count_Money
        self.Count_password = Count_password
        self.Count_Root = Count_Root
        self.Count_Name = Count_Name


class DaoServer:

    # 检测账号是否已经被锁
    def isLock(self, i_id):
        with open("D:\\userFile.txt", 'r') as seaFile:
            mes = seaFile.readlines()
            for index in mes:
                matchId = index.split("~")[0]
                if matchId == i_id and index.split("~")[6] is False:
                    return True
        pass
        return False

    # 作用1：开户匹配是否有同样的身份证注册这个账户，有就返回假，没有返回真。传的参数是身份证号
    # 作用2：在查询时看看是否存在这个账号
    def searchBlock(self, IdCard):
        with open("D:\\userFile.txt", 'r') as seaFile:
            mes = seaFile.readlines()
            # id~pass~idcard~name~phone~money
            for index in mes:
                matchIdcard = index.split("~")[1]
                matchId = index.split("~")[0]
                if matchIdcard == IdCard or matchId == IdCard:
                    return False
        pass
        return True

    # 注册账户
    def register(self, user):
        if self.searchBlock(user.Count_IDCard):
            # 开始开户
            a = [1, 2, 3, 4, 5, 6, 7, 8, 9, 0]
            # 产生的一个账号
            numArray = random.sample(a, 6)
            # id~pass~idcard~name~phone~money
            # Count_id, Count_IDCard, Count_phone, Count_Money, Count_password, Count_Root
            # user.Count_id = ''.join(str(k) for k in numArray)
            # 用于生成的账户是否已经存在，如果存在就重新生成
            while not self.searchBlock(user.Count_id):
                numArray = random.sample(a, 6)
                # Count_id, Count_IDCard, Count_phone, Count_Money, Count_password, Count_Root
                user.Count_id = ''.join(str(k) for k in numArray)
            line = user.Count_id + "~" + user.Count_IDCard + "~" + user.Count_Name + "~" + user.Count_phone + "~" + str(
                user.Count_Money) + "~" + user.Count_password + "~" + str(user.Count_Root) + "\n"
            with open("D:\\userFile.txt", 'a+') as writeFile:
                writeFile.writelines(line)
                pass
            return True
        else:
            return False

    # 验证密码和账号是否一致
    # 正确返回user对象，否则返回Null
    def proof(self, pId, pPassword):
        with open("D:\\userFile.txt", 'r') as proofFile:
            proofMes = proofFile.readlines()
            for pIndex in proofMes:
                fId = pIndex.split("~")[0]
                fPassword = pIndex.split("~")[5]
                if fId == pId and fPassword == pPassword:
                    f = bankUser(pIndex.split("~")[0], pIndex.split("~")[1], pIndex.split("~")[2], pIndex.split("~")[3],
                                 pIndex.split("~")[4], pIndex.split("~")[5], pIndex.split("~")[6])
                    return f
            return None

    # 锁控制函数 + 还可以进行重新数据更新后重新写入数据
    # 数据更新函数
    def Lock(self, lockU, res):
        lId = lockU.Count_id
        r_mes = []
        with open('D:\\userFile.txt', 'r') as rFile:
            r_mes = rFile.readlines()
            for r_index in r_mes:
                if r_index.split("~")[0] == lId:
                    line = lId + "~" + r_index.split("~")[1] + "~" + r_index.split("~")[2] + "~" + r_index.split("~")[
                        3] + "~" + str(lockU.Count_Money) + "~" + r_index.split("~")[5] + "~" + str(res) + "\n"
                    r_mes.remove(r_index)
                    r_mes.append(line)
                    break
        pass

        with open('D:\\userFile.txt', 'w') as file:
            pass

        with open('D:\\userFile.txt', 'w') as file:
            for i in r_mes:
                file.writelines(i)
            pass

    # 查询账户
    def search(self, sId, sPassword):
        # 看看有没有这个账户
        # 参数：账户
        if not self.searchBlock(sId):

            # 存在这个账户，然后进行账户密码验证
            # 查看是否被锁定
            if self.isLock(sId):
                print("账号有危险，程序自动退出！")
                exit(0)
            res = self.proof(sId, sPassword)
            n = 1

            while res is None and n <= 3:
                sPassword = input("密码有误，请重新输入：")
                n = n + 1
                res = self.proof(sId, sPassword)

            if res is None:
                # 锁住，返回
                self.Lock(sId, False)
                print("有危险，账号已经锁住！")
                return None
            else:
                # 打印信息
                print("=" * 50)
                print("||", " " * 13, res.Count_Name, " 先生（女士）", " " * 13, "||")
                print("||\t账户：", res.Count_id, " " * 6, "金额：", res.Count_Money, " " * 13, "||")
                print("=" * 50)
                return res
        else:
            print("本行没有这个账户！")
            return None
        pass

    # 取款 | 存款
    #   1     2
    def getOrSaveMoney(self, flag, gId, gPassword):
        getRes = self.search(gId, gPassword)
        if getRes is None:
            return None
        else:
            if flag is 1:
                money = int(input("请输入你要取的金额："))
                getRes.Count_Money = int(getRes.Count_Money) - money
                if money <= 0 or money > int(getRes.Count_Money):
                    print("输入有误")
                    return getRes
            else:
                money = int(input("请输入你要存的金额："))
                getRes.Count_Money = int(getRes.Count_Money) + money
            self.Lock(getRes, True)
            print(getRes.Count_Money)
            return getRes

    # 获取转向那个人的目标钱数
    def getGoalMoey(self, goalId):
        with open("D:\\userFile.txt", 'r') as seaFile:
            mes = seaFile.readlines()
            for index in mes:
                if index.split("~")[0] == goalId:
                    return int(index.split("~")[4])
        pass

    # 转账
    def Transfer(self, tId, tPa):
        rRes = self.search(tId, tPa)
        if rRes is not None:

            if self.isLock(tId):
                print("此账号有危险，程序自动退出！")
                exit(0)

            # 转向账号
            goalId = input("请输入你要转向的那个人的账号：")
            if self.searchBlock(goalId):
                print("本行没有 ", goalId, " 这个账户")
            else:
                much = int(input("请输入你要转的金额："))
                if much < 0 or much > int(rRes.Count_Money):
                    print("输入有误，即将退出...")
                    return None
                else:
                    u = bankUser(goalId, "", "", "", str(self.getGoalMoey(goalId) + much), "", True)
                    # def Lock(self, lockU, res):
                    self.Lock(u, True)
                    rRes.Count_Money = int(rRes.Count_Money) - much
                    self.Lock(rRes, True)
                    print("已经完成转账！")
        else:
            print("本行没有 ", tId, " 这个账户")


def welcomeView():
    print("*" * 40)
    print("***", " " * 32, "***")
    print("***", " " * 32, "***")
    print("***", " " * 7, "欢迎登录银行管理系统", " " * 7, "***")
    print("***", " " * 32, "***")
    print("***", " " * 32, "***")
    print("*" * 40)


def functionView():
    print("*" * 50)
    print("***", " " * 42, "***")

    print("***\t1.开户(1)", " " * 20, "2.查询(2)\t   ***")
    print("***\t3.取款(3)", " " * 20, "5.存款(4)\t   ***")
    print("***\t5.转账(5)", " " * 20, "6.锁定(6)\t   ***")
    print("***\t7.解锁（7）", " " * 32, "***")
    print("***", " " * 42, "***")
    print("***\t退出(Q)", " " * 35, "***")
    print("***", " " * 42, "***")
    print("*" * 50)




welcomeView()
print("欢迎管理员前来工作：")
b = True
m_id = input("请输入管理员账号：")
while b:
    if m_id == "admine":
        break
    else:
        m_id = input("请重新输入管理员账号：")
pas = input("请输入管理员密码：")
a = True
m_pas = input("请输入管理员密码：")
while a:
    if m_pas == "123":
        break
    else:
        m_pas = input("请重新输入管理员密码：")

functionView()
type = input("请输入你的操作：")
while type is not 'Q':
    if type == "1":
        u_name = input("请输入你的姓名：")
        u_phone = input("请输入你的电话：")
        u_idCard = input("请输入你的身份证号：")
        u_money = input("请输入你的预存金额：")
        u_pass = input("请输入你的密码：")
        u_user = bankUser("", u_idCard, u_name, u_phone, int(u_money), u_pass, True)
        d1 = DaoServer()
        boo = d1.register(u_user)
        if boo:
            print("注册成功！")
        else:
            print("注册失败！")
    elif type == "2":
        s_id = input("请输入你的账户：")
        s_pass = input("请输入你的密码：")
        d2 = DaoServer()
        d2.search(s_id, s_pass)
    elif type == "3":
        d3 = DaoServer()
        g_id = input("请输入你的账户：")
        g_pass = input("请输入你的密码：")
        d3.getOrSaveMoney(1, g_id, g_pass)
    elif type == "4":
        d4 = DaoServer()
        s_id = input("请输入你的账户：")
        s_pass = input("请输入你的密码：")
        d4.getOrSaveMoney(2, s_id, s_pass)
    elif type == "5":
        t_id = input("请输入你的账户：")
        t_pass = input("请输入你的密码：")
        d5 = DaoServer()
        d5.Transfer(t_id, t_pass)
    elif type == "6":
        d5 = DaoServer()
        p_id = input("请输入你的账户：")
        p_pass = input("请输入你的密码：")
        flag = d5.proof(p_id, p_pass)
        if flag is not None:
            d5.Lock(flag, False)
            print("锁定成功！")
        else:
            print("锁定失败")
    elif type == "7":
        d6 = DaoServer()
        ul_id = input("请输入你的账户：")
        ul_pass = input("请输入你的密码：")
        flag = d6.proof(ul_id, ul_pass)
        if flag is not None:
            d5.Lock(flag, True)
            print("解锁成功")
        else:
            print("解锁失败")
    elif type =="Q" or type == "q":
        exit(0)
    else:
        print("输入有误请重新输入：")
    type = input("请输入你的操作：")
    functionView()

