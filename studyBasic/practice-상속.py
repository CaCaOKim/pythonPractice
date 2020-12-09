#상속
class Unit:
    def __init__(self, name, hp, speed):   #__init__: 생성자
        self.name = name   #맴버변수
        self.hp = hp
        self.speed = speed

    def move(self, location):
        print("[지상 유닛 이동]")
        print("{0} : {1} 방향으로 이동합니다. [속도 {2}]".format(self.name, location, self.speed))

class AttackUnit(Unit):   #Unit클래스를 상속받음
    def __init__(self, name, hp, speed, damage):   #__init__: 생성자
        Unit.__init__(self, name, hp, speed)
        self.damage = damage

    def attack(self, location):
        print("{0} : {1}방향으로 적군을 공격합니다. [공격력 {2}]".format(self.name, location, self.damage))
    
    def damaged(self, damage):
        print("{0} : {1} 데미지를 입었습니다.".format(self.name, damage))
        self.hp -= damage
        print("{0} : 현재 체력은 {1}입니다.".format(self.name, self.hp))
        if self.hp <= 0:
            print("{} : 파괴되었습니다.".format(self.name))

firebat1 = AttackUnit("파이어뱃", 50, 16, 5)
firebat1.attack("5시")

firebat1.damaged(25)
firebat1.damaged(25)  


#다중 상속 : 부모가 둘 이상
class Flyable:
    def __init__(self, flying_speed):
        self.flying_speed = flying_speed
    
    def fly(self, name, location):
        print("{0} : {1} 방향으로 날아갑니다. [속도 {2}]".format(name, location, self.flying_speed))

class FlyableAttackUnit(AttackUnit, Flyable):
    def __init__(self, name, hp, damage, flying_speed):
        AttackUnit.__init__(self, name, hp, 0, damage)
        Flyable.__init__(self, flying_speed)
    
    def move(self, location):
        print("[공중 유닛 이동]")
        self.fly(self.name, location)

valkyrie = FlyableAttackUnit("발키리", 200, 6, 5)
valkyrie.fly(valkyrie.name, "3시")


#메소드 오버라이딩
vulture = AttackUnit("벌쳐", 80, 10, 20)

battlecruiser = FlyableAttackUnit("배틀크루저", 500, 25, 3)

vulture.move("11시")
battlecruiser.move("9시")


#pass
# class BuildingUnit(Unit):
#     def __init__(self, name, hp, location):
#         pass   #일단 아무것도 정의 안하고 ㄱㄱㄱ

# supply_depot = BuildingUnit("서플라이 디폿", 500, "7시")


#super
class BuildingUnit(Unit):
    def __init__(self, name, hp, location):
        super().__init__(name, hp, 0)   #super는 다중상속일 경우 첫 번 째로 명시된 클래스에 반응
        self.location = location














