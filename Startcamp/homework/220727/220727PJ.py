class Doggy:
    pass
    num_of_dogs = 0     # 현재 강아지 수
    birth_of_dogs = 0   # 태어난 강아지 수

    def __init__(self, name, type) :
        self.name = name
        self.type = type
        Doggy.num_of_dogs += 1
        Doggy.birth_of_dogs += 1
        
    def bark(self):
        print('Bow Wow!')
    
    def get_status(self):
        print(f'현재 강아지의 수는 {Doggy.num_of_dogs}, 태어난 강아지 수는 {Doggy.birth_of_dogs} 입니다.')
    
    def __del__(self):
        print("강아지가 하늘나라로 갔습니다.")
        Doggy.num_of_dogs -= 1
    


doggy1 = Doggy('우유', '말티즈' )
doggy2 = Doggy('유', '즈' )

doggy1.get_status()
print(doggy1.name)
doggy1.bark()
del doggy2
doggy1.get_status()