class A:
    def m1(self):
        print("A")


class B(A):
    def m1(self):
        print("B")


class C(A, B):
    pass


print(C.mro())
