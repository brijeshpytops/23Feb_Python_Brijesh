# single inh.
# class A:
#     def a(self):
#         return "Class A function a()"
# class B(A):
#     def b(self):
#         return "Class B function b()"
    
# obj = B()
# # print(dir(obj))

# print(obj.a())
# print(obj.b())

# # Multi-level inh.
# class A:
#     def a(self):
#         return "Class A function a()"
# class B(A):
#     def b(self):
#         return "Class B function b()"
# class C(B):
#     def c(self):
#         return "Class C function c()"
    
# obj = C()
# # print(dir(obj))

# print(obj.a())
# print(obj.b())
# print(obj.c())


# Multiple inh.
# class A:
#     def a(self):
#         return "Class A function a()"
# class B:
#     def b(self):
#         return "Class B function b()"
# class C(A, B):
#     def c(self):
#         return "Class C function c()"
    
# obj = C()
# # print(dir(obj))

# print(obj.a())
# print(obj.b())
# print(obj.c())

class Shape:
    def shape(self):
        return "shape"

class Shape2D(Shape):
    def shape2d(self):
        return "shape2d"
    
class Circle(Shape2D):
    def circle(self):
        return "circle"

class Square(Shape2D):
    def square(self):
        return "square"
    
class mix(Circle, Square):
    def test(self):
        print("""hnfjhtfgmes d KeyboardInterruptdkjhdgyrjsb \n
        hgdjsgd \n
        djmbndc""")
    

class Shape3D(Shape):
    def shape3d(self):
        return "shape3d"

class Cube(Shape3D):
    def cube(self):
        return "cube"

obj = mix()
print(Cube.mro())
print(Cube.__mro__)

# print(obj.test())
# print(dir(obj))

# print(obj.cube())
# print(obj.shape())
# print(obj.shape3d())