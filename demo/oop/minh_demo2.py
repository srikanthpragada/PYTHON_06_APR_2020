class A:
    def m1(self):
        print("A")


class B(A):
    pass


class C:
    def m1(self):
        print("C")


class D(B, C):
    pass


obj = D()
obj.m1()
