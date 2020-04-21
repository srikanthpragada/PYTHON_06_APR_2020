class A:
    def m1(self):
        print("A")


class B:
    def m1(self):
        print("B")


class C(B, A):
    pass
    # def m1(self):
    #     print("C")


obj = C()
obj.m1()
