# -*- coding: utf-8 -*-
"""
Created on Sat Jul  4 09:26:18 2020

@author: Rabbitking
"""

Mode = ['생산Data','검사Data','기준정보']
Type = ['제품','설비']
ProductList = ['myProductA','myProductB']

# 메뉴 선택
def MenuSelectByUser(item):
    while True:
        print("다음 중에서 선택하세요.", item)
        UserInput = input()
        if UserInput in item:
            break
        else:
            continue
    print(UserInput,"을 선택하였습니다.")
    return UserInput #UserInput으로 받은 Data를 함수의 최종값으로 반환

# 제품 Class의 생성
class Product:
    def __init__(self):
        self.productionAmount = input("생산량을 입력하세요.")
        self.defectAmount = input("불량량을 입력하세요.")
        self.productionStartTime = input("생산시작시간을 입력하세요.")
        self.productionEndTime = input("생산종료시간을 입력하세요.")


# 제품군의 생성 : ProductList로부터 Loop를 통한 Class 생성이 필요함
class myProductA(Product):
    name = "myProductA"
    pass

class myProductB(Product):
    name = "myProductB"
    pass




#시스템의 시작
# User Interaction
print("생산 이력 관리 시스템에 오신 것을 환영합니다.")

InputMode = MenuSelectByUser(Mode)
InputType = MenuSelectByUser(Type)

print(InputMode,InputType)

print(InputType,"에 대한",InputMode,"입력을 진행합니다.")

if InputMode == '생산Data' and InputType == '제품':
    print("제품을 선택해주세요.", ProductList)
    InputProductName = input("제품명을 입력하세요")
    print(InputProductName,"을 선택하였습니다.")
    InputProductLot = input("제품 Lot를 입력하세요.")
    if InputProductName == 'myProductA':
        InputProductLot = myProductA()
    else:
        print("미지원 기능으로 시스템을 종료합니다.")
else:
    print("미지원 기능으로 시스템을 종료합니다.")