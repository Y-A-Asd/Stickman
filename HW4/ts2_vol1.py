# class Add:
#     all_num = []
#     def __init__(self,num):
#         assert num >= 0,"Invalid number"
#         self.__class__.all_num.append(num)
#         print(sum(self.__class__.all_num))
#     def __call__(self,num):
#         global all_num
#         assert num >= 0 ,"Invalid number"
#         self.__class__.all_num.append(num)
#
# Add(10)(38)

# class Add(int):
#     def __call__(self, num):
#         return Add(self + num)


class Add():
    def __init__(self,num):
        assert num >= 0, "Invalid number"
        self.num = num
    def __call__(self, num):
        assert num >= 0, "Invalid number"
        return Add(self.num + num)
    def __repr__(self):
        return str(self.num)
print(Add(10))
print(Add(1)(9)("4"))