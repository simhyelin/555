import json
import os
if os.path.exists("addressbook.json"): 
    with open("addressbook.json", "r", encoding="utf-8") as f:
        addressbook = json.load(f)
else:
    addressbook=dict()

name = None
while(True):
    name = input("이름을 입력하세요:")
    if(name == '끝'):
        break
    
    phonenum = input("전화번호를 입력하세요:")
    address = input("주소를 입력하세요:")
    age = input("나이를 입력하세요:")
    birth = input("생년월일을 입력하세요:")
    
    addressbook[name] = phonenum, age, address, birth

with open("addressbook.json", "w", encoding="utf-8") as f:
    json.dump(addressbook, f, ensure_ascii=False, indent=4)
print("주소록이 저장되었습니다.")

print("현재 주소록 상태:", addressbook)
