from tkinter import *
import datetime,time
class IDCheckGUI:
    def __init__(self):
        self.frame = Tk()
        self.frame.title("身份证校验")
        self.frame.geometry("700x500")
        self.frame["bg"] = "lightblue"
        # 图片
        self.image = PhotoImage(file="C:\\Users\\Dell\\Desktop\\身份证校验系统\\身份证.png")
        self.Label_image = Label(self.frame,image=self.image,bd=0)
        self.Label_image.place(x=7,y=7)
        # 校验表单
        self.Label_is_input = Label(self.frame, text="请输入身份证号码：", font=("微软雅黑", 14, "bold"), bg="navy", fg="lightblue")
        self.Label_is_input.place(x=320, y=20)
        self.Entry_is_input = Entry(self.frame, width=21, font=("微软雅黑", 16, "bold"))
        self.Entry_is_input.place(x=320, y=58)
        self.Button_is_input = Button(self.frame, width=10, command=self.get_info, text="校验", font=("微软雅黑", 10, "bold"), bg="#eee")
        self.Button_is_input.place(x=600, y=58)
        # 显示表单
        self.Label_id_exits = Label(self.frame, text="是否有效：", font=("微软雅黑", 14, "bold"), fg="navy", bg="lightblue")
        self.Label_id_exits.place(x=320, y=150)
        self.var_exits = StringVar()
        self.Entry_id_exits = Entry(self.frame, width=8, textvariable=self.var_exits, state=DISABLED, font=("微软雅黑", 14, "bold"))
        self.Entry_id_exits.place(x=420, y=150)
        self.Label_id_gender = Label(self.frame, text="性别：", font=("微软雅黑", 14, "bold"), fg="navy", bg="lightblue")
        self.Label_id_gender.place(x=358, y=210)
        self.var_gender = StringVar()
        self.Entry_id_gender = Entry(self.frame, width=8, textvariable=self.var_gender, state=DISABLED, font=("微软雅黑", 14, "bold"))
        self.Entry_id_gender.place(x=420, y=210)
        self.Label_id_birthday = Label(self.frame, text="出生日期：", font=("微软雅黑", 14, "bold"), fg="navy", bg="lightblue")
        self.Label_id_birthday.place(x=320, y=270)
        self.var_birthday = StringVar()
        self.Entry_id_birthday = Entry(self.frame, width=20, textvariable=self.var_birthday, state=DISABLED, font=("微软雅黑", 14, "bold"))
        self.Entry_id_birthday.place(x=420, y=270)
        self.Label_id_area = Label(self.frame, text="所在地：", font=("微软雅黑", 14, "bold"), fg="navy", bg="lightblue")
        self.Label_id_area.place(x=338, y=330)
        self.var_area = StringVar()
        self.Entry_id_area = Entry(self.frame, width=20, textvariable=self.var_area, state=DISABLED, font=("微软雅黑", 14, "bold"))
        self.Entry_id_area.place(x=420, y=330)
        self.Button_close = Button(self.frame, command=self.close, width=10, text="关闭", font=("微软雅黑", 10, "bold"), bg="#eee")
        self.Button_close.place(x=550, y=400)
        # self.frame.mainloop()
        self.show()
    def show(self):
        self.frame.mainloop()
    # 关闭
    def close(self):
        self.frame.destroy()
    # 校验按钮事件
    def get_info(self):
        # 获取身份证号码
        self.id_number = self.Entry_is_input.get()
        checkidc = CheckIDC(str(self.id_number))
        result_lists = checkidc.results()
        if result_lists[0] == False or result_lists[1] == False or result_lists[3] == False:
            self.var_exits.set('无效')
            self.var_gender.set('')
            self.var_birthday.set('')
            self.var_area.set('')
        # 设置到数据
        else:
            self.var_exits.set(result_lists[1])
            self.var_gender.set(result_lists[2])
            self.var_birthday.set(result_lists[0])
            self.var_area.set(result_lists[3])

class CheckIDC:
    def __init__(self, id_number):
        self.id_number = id_number
        # 切片身份号码
        self.area = id_number[:6]
        self.birthday = id_number[6:14]
        self.gender = id_number[14:17]
        self.exits = id_number[17:]
        self.lists = []
        self.lists.append(self.check_birthday(self.birthday))
        self.lists.append(self.validate_check_number())
        self.lists.append(self.validate_check_gender())
        self.lists.append(self.valedate_check_area())
    def results(self):
        return self.lists
    def validate_check_gender(self):
        if int(self.gender) % 2 == 0:
            return '女'
        else:
            return '男'
    def check_birthday(self, birthday):
        # 1970-1-1日期---现在的日期---进行判断
        # 获取1970-1-1时间戳
        odate = datetime.datetime(1970,1,2)
        # print(type(odate))
        otime = time.mktime(odate.timetuple())
        # 现在的时间戳
        now = time.time()
        # 身份证日期的时间戳
        year = birthday[:4]
        month = birthday[4:6]
        day = birthday[6:]
        ymd = datetime.datetime(int(year), int(month), int(day))
        yearmd = time.mktime(ymd.timetuple())
        # 判断
        if otime < yearmd and yearmd < now:
            return ymd.strftime("%Y-%m-%d")
        else:
            return False   # 返回结果
    # 验证归属地
    def valedate_check_area(self):
        # 获取到所有的归属地
        f = open(file="C:\\Users\\Dell\\Desktop\\身份证校验系统\\身份证归属地.txt", mode='r', encoding="utf-8")
        all_area = f.readlines()
        res_area = ''
        for item in all_area:
            if self.area == item[:6]:
               res_area = item[6:-1]
        if res_area == '':
            return False
        else:
            return res_area
    # 获取验证
    def get_check_number(self):
        number = self.id_number[0:17]
        # 系数
        si_list = [7, 9, 10, 5, 8, 4, 2, 1, 6, 3, 7, 9, 10, 5, 8, 4, 2]
        check_number = ['1', '0', 'X', '9', '8', '7', '6', '5', '4', '3', '2']
        # 验证
        of_number = 0
        for index in range(len(number)):
            of_number += int(number[index]) * int(si_list[index])
        yu_number = of_number % 11
        return check_number[yu_number]
    # 校验码验证
    def validate_check_number(self):
        if self.get_check_number() == self.exits:
            return '有效'
        else:
            return False
IDCheckGUI()

