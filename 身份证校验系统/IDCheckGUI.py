from tkinter import *
from CheckIDC import *
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
IDCheckGUI()

