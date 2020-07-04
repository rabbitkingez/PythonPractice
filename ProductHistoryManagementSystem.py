# -*- coding: utf-8 -*-
"""
Created on Sat Jul  4 09:26:18 2020

@author: Rabbitking
"""

Mode = ['생산Data','기준정보']
Type = ['제품','설비']

def Select(item):
    while True:
        print("다음 중에서 선택하세요.", item)
        UserInput = input()
        if UserInput in item:
            break
        else:
            continue
    print(UserInput, "을 선택하였습니다.")    

    
#시스템의 시작
#입력 모드의 진행
print("생산 이력 관리 시스템에 오신 것을 환영합니다.")

Select(Mode)
Select(Type)

print(Type,"에 대한",Mode,"입력을 진행합니다.")

