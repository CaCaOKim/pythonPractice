#모듈
import theater_module
theater_module.price(3)
theater_module.price_morning(4)
theater_module.price_soldier(5)

import theater_module as mv
mv.price(3)
mv.price_morning(4)
mv.price_soldier(5)

from theater_module import *
price(3)
price_morning(4)
price_soldier(5)

from theater_module import price, price_morning
price(3)
price_morning(4)
price_soldier(5)   #에러

from theater_module import price_soldier as price
price(3)   #군인 가격으로 계산


#페키지
import travel.thailand
trip_to = travel.thailand.ThailandPackage()
trip_to.detail()

from travel.thailand import ThailandPackage   #클래스 임포트
trip_to = ThailandPackage()
trip_to.detail()

from travel import vietnam   #모듈 임포트
trip_to = vietnam.VietnamPackage()
trip_to.detail()


#__all__: __init__.py 파일을 이용
from travel import *
trip_to = vietnam.VietnamPackage()
# trip_to = thailand.ThailandPackage()
trip_to.detail()


#페키지 모듈 위치
import inspect
import random
print(inspect.getfile(random))
print(inspect.getfile(vietnam))


#pip install: 사람들이 만든 패키지
#내장함수: 임포트 없이 사용하는 함수   (list of python builtins)
#외장함수: 임포트 해서 사용해야하는 함수   (list of python modules)





