class A:
    def m1(self):
        print("A")


class B(A):
    pass


class C(A):
    def m1(self):
        print("C")


class D(B, C):
    pass


obj = D()
obj.m1()
print(D.mro())