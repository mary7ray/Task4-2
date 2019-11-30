# Создайте новый класс Airplane. Создайте следующие характеристики (полей)
# объекAта:
# ● make (марка)
# ● model
# ● year
# ● max_speed
# ● odometer
# ● is_flying
# и методы имитирующих поведение самолета take off (взлет), fly (летать), land
# приземление). Метод take off должен изменить is_flying на True, а land на False. По
# умолчанию поле is_flying = False. Метод fly должен принимать расстояние полета и
# изменять показания одометра (километраж). Создайте 1 объект класса и используйте
# все методы класса.


 class Airline:
     def __init__(self,mark,model,year,max_speed,odometer,is_flying = False)
         self.mark = mark
         self.model = model
         self.year = year
         self.max_speed = max_speed
         self.odometer = odometer
         self.is_flying = is_flying

        def take_off
        def fly
        def land
