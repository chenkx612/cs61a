class A:
    x, y = 0, 0
    def __init__(self):
        return
class B(A):
    def __init__(self):
        return
class C(A):
    def __init__(self):
        return
print(A.x, B.x, C.x)