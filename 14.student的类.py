class Student:
    #初始化方法，用于创建Student类的实例时设置属性
    #self表示实例本身，name为学生姓名，age为学生年龄，is_single表示是否单身
    def __init__(self,name,age,is_single):
        self.name=name
        self.age=age
        self.is_single=is_single
        self.grades=[]#初始化一个空列表，用于存储学生的成绩

    #定义一个方法，用于向学生的成绩列表中添加成绩
    #self表示实例本身，grade为要添加的单个成绩
    def add_grade(self,grade):
        self.grades.append(grade)

    #定义一个方法，用于计算学生的平均成绩
    #self表示实例本身
    def average_grade(self):
        if not self.grades:#如果成绩列表为空
            return 0#返回0
        return sum(self.grades)/len(self.grades)#否则返回成绩的平均值

    #定义特殊方法__str__，用于返回对象的字符串表示形式
    #当使用print函数输出Student实例时，会调用这个方法
    def __str__(self):
        return f"姓名{self.name},平均分:{self.average_grade()}"

    #定义一个方法，用于返回学生的基本信息和单身状态
    #self表示实例本身
    def print_status(self):
        status="是" if self.is_single else"不是"#根据is_single属性确定单身状态的字符串表示
        return f"姓名:{self.name},年龄:{self.age},单身否:{status}"
