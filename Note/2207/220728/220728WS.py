# ### 도형 만들기

# # 아래의 명세를 읽고 Python 클래스를 활용하여  (Point)과 사각형(Rectangle)을 표현하시오.
# # 예를 들어, 좌표 (4, 3)의 점은 아래와 같이 표현할 수 있다.

# class Point:
    
#     def __init__(self, x, y) -> None:
#         self.x = x
#         self.y = y
#         pass

# class Rectangle:

#     def __init__(self, p1, p2) -> None:
#         self.p1 = p1
#         self.p2 = p2
#         self.x = abs(self.p1.x-self.p2.x) 
#         self.y = abs(self.p1.y-self.p2.y) 
        
#     def get_area(self):
#         area = self.x * self.y
#         return area

#     def get_perimeter(self):
#         perimeter = (self.x + self.y) *2
#         return perimeter

#     def is_square(self):
#         if self.x == self.y :
#             return True
#         else:
#             return False



# # p1 = Point(3, 4)

# # Rectangle 클래스에 대한 명세는 다음과 같다.
# # 예를 들어, 좌측 상단 좌표 (1, 3)과 우측 하단 좌표 (3, 1)의 점으로 만든 사각형을 그림으로 
# # 표현하면 다음과 같다

# p1 = Point(1, 3)
# p2 = Point(3, 1)
# r1 = Rectangle(p1, p2)
# print(r1.get_area())
# print(r1.get_perimeter())
# print(r1.is_square())

# p3 = Point(3, 7)
# p4 = Point(6, 4)
# r2 = Rectangle(p3, p4)
# print(r2.get_area())
# print(r2.get_perimeter())
# print(r2.is_square())


# # 위의 코드를 실행하였을 때, 아래와 같이 출력되어야 한다.

# # 4
# # 8
# # True
# # 9
# # 12
# # True


class Point:
    
    def __init__(self, x, y) -> None:
        self.x = x
        self.y = y
        pass

class Rectangle:

    def __init__(self, p1, p2) -> None:
        self.p1 = p1
        self.p2 = p2
        self.x = abs(self.p1.x-self.p2.x) 
        self.y = abs(self.p1.y-self.p2.y) 
        
    def get_area(self):
        area = self.x * self.y
        return area

    def get_perimeter(self):
        perimeter = (self.x + self.y) *2
        return perimeter

    def is_square(self):
        if self.x == self.y :
            return True
        else:
            return False
