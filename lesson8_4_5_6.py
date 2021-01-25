# 4. Начните работу над проектом «Склад оргтехники». Создайте класс, описывающий склад.
# А также класс «Оргтехника», который будет базовым для классов-наследников.
# Эти классы — конкретные типы оргтехники (принтер, сканер, ксерокс).
# В базовом классе определить параметры, общие для приведенных типов.
# В классах-наследниках реализовать параметры, уникальные для каждого типа оргтехники.
# 5. Продолжить работу над прошлым заданием. Разработать методы, отвечающие за приём оргтехники на склад
# и передачу в определенное подразделение компании. Для хранения данных о наименовании и количестве единиц оргтехники,
# а также других данных, можно использовать любую подходящую структуру, например словарь.
# 6. Продолжить работу над заданием. Реализуйте механизм валидации вводимых пользователем данных.
# Например, нельзя отправить принтеры в виде строки или меньше 0.


class Store:
    def __init__(self):

        self.office_equipment_in_storage = {'printers': 0, 'scanners': 0, 'MFD': 0, 'total_office_equipment': 0,
                                            'id_of_printers': [], 'id_of_scanners': [], 'id_of_MFD': []}

    def get_office_equipment(self, office_equipment):
        if isinstance(office_equipment, Printers):
            self.office_equipment_in_storage['printers'] += 1
            self.office_equipment_in_storage['id_of_printers'].append(office_equipment.id)
        elif isinstance(office_equipment, Scanners):
            self.office_equipment_in_storage['scanners'] += 1
            self.office_equipment_in_storage['id_of_scanners'].append(office_equipment.id)
        elif isinstance(office_equipment, MFD):
            self.office_equipment_in_storage['MFD'] += 1
            self.office_equipment_in_storage['id_of_MFD'].append(office_equipment.id)
        self.office_equipment_in_storage['total_office_equipment'] = self.office_equipment_in_storage['printers'] + \
                                                                     self.office_equipment_in_storage['scanners'] + \
                                                                     self.office_equipment_in_storage['MFD']
        office_equipment.location = "storage"

    def take_office_equipment(self, office_equipment):
        if isinstance(office_equipment, Printers):
            self.office_equipment_in_storage['printers'] -= 1
            self.office_equipment_in_storage['id_of_printers'].remove(office_equipment.id)
        elif isinstance(office_equipment, Scanners):
            self.office_equipment_in_storage['scanners'] -= 1
            self.office_equipment_in_storage['id_of_scanners'].remove(office_equipment.id)
        elif isinstance(office_equipment, MFD):
            self.office_equipment_in_storage['MFD'] -= 1
            self.office_equipment_in_storage['id_of_MFD'].remove(office_equipment.id)
        self.office_equipment_in_storage['total_office_equipment'] = self.office_equipment_in_storage['printers'] + \
                                                                     self.office_equipment_in_storage['scanners'] + \
                                                                     self.office_equipment_in_storage['MFD']
        office_equipment.location = "organization"


class OfficeEquipment:
    dict_of_format = {'1': 'A5', '2': 'A4', '3': 'A3', '4': 'A2', '5': 'A1', '6': 'A0'}
    dict_of_interface = {'1': 'USB', '2': 'COM', '3': 'Ethernet'}
    dict_of_voltage = {'1': '110', '2': '220', '3': '380'}

    def __init__(self):
        self.id = OfficeEquipment.get_id()
        self.format = self.dict_of_format.get(OfficeEquipment.get_param_from_dict(self.dict_of_format, 'формат'))
        self.interface = self.dict_of_interface.get(OfficeEquipment.get_param_from_dict(self.dict_of_interface, 'интерфейс'))
        self.voltage = self.dict_of_voltage.get(OfficeEquipment.get_param_from_dict(self.dict_of_voltage, 'вольтаж'))
        self.location = "Склад"

    @staticmethod
    def get_id():
        try:
            id = input("Введите id устройства. id должен состоять из строки без пробелов")
            IdException.validation_id(id)
        except IdException:
            id = OfficeEquipment.get_id()
        finally:
            return id

    @staticmethod
    def get_param_from_dict(d, name):
        output_str = ''
        for el in d:
            output_str += el + ' - ' + d.get(el) + '\t'
        param = input(f"Введите {name}. Цифра соответствует выбранному формату\n{output_str}")
        try:
            int(param)
            ParamException.validation_param(int(param), len(d))
        except ValueError:
            print("НЕВЕРНЫЙ ВВОД! для выбора параметра необходимо ввести цифру")
            param = OfficeEquipment.get_param_from_dict(d, name)
        except ParamException:
            param = OfficeEquipment.get_param_from_dict(d, name)
        return param


class Printers(OfficeEquipment):
    type_of_printers = {'1': "jet", '2': "laser"}

    def __init__(self):
        super().__init__()
        self.type = self.type_of_printers.get(OfficeEquipment.get_param_from_dict(self.type_of_printers, 'тип принтера'))
        self.device = "принтер"
        print(f'Добавлено устройство {self.device} id: {self.id}\tформат: {self.format}\tинтерфейс: {self.interface}\t'
              f'вольтаж: {self.voltage}\tтип: {self.type}\tрасположение:{self.location}')


class Scanners(OfficeEquipment):
    type_of_scanners = {'1': "drum ", '2': "flatbed", '3': "hand-held", '4': "film"}

    def __init__(self):
        super().__init__()
        self.type = self.type_of_scanners.get(OfficeEquipment.get_param_from_dict(self.type_of_scanners, 'тип сканера'))
        self.device = "сканер"
        print(f'Добавлено устройство {self.device} id: {self.id}\tформат: {self.format}\tинтерфейс: {self.interface}\t'
              f'вольтаж: {self.voltage}\tтип: {self.type}\tрасположение:{self.location}')


class MFD(OfficeEquipment):
    type_of_MFD = {'1': "color", '2': "black-white"}

    def __init__(self):
        super().__init__()
        self.type = self.type_of_MFD.get(OfficeEquipment.get_param_from_dict(self.type_of_MFD, 'тип сканера'))
        self.device = "МФУ"
        print(f'Добавлено устройство {self.device} id: {self.id}\tформат: {self.format}\tинтерфейс: {self.interface}\t'
              f'вольтаж: {self.voltage}\tтип: {self.type}\tрасположение:{self.location}')


class IdException(Exception):
    def __init__(self):
        print("НЕКОРРЕКТНЫЙ ВВОД! id должен состоять из строки без пробелов")

    @staticmethod
    def validation_id(id):
        buf_id = id.split()
        if len(buf_id) > 1:
            raise IdException


class ParamException(Exception):
    def __init__(self):
        print("НЕКОРРЕКТНЫЙ ВВОД! Введите цифру параметра в соответствии с условием: ")

    @staticmethod
    def validation_param(n, l):
        if n > l:
            raise ParamException


class ChangeException(Exception):
    def __init__(self):
        print("неверный ввод операции")

    @staticmethod
    def take_valid_change(str):
        c = (input(str))
        try:
            if int(c) > 4 or int(c) < 0:
                raise ChangeException
        except ValueError:
            print("неверный ввод операции")
            c = ChangeException.take_valid_change()
        except ChangeException:
            c = ChangeException.take_valid_change()
        finally:
            return c


a = Store()
list_storage = list()
list_not_storage = list()
while True:
    f = ChangeException.take_valid_change("Введите код действия:\n 1 - добавить\t2 - снять с учета\t3 - выйти")
    if int(f) == 3:
        break
    elif int(f) == 1:
        k = ChangeException.take_valid_change("Введите добавляемой техники:\n 1 - принтер\t2 - сканер\t3 - МФУ")
        if int(k) == 1:
            i = Printers()
            a.get_office_equipment(i)
            list_storage.append(i)
        elif int(k) == 2:
            i = Scanners()
            a.get_office_equipment(i)
            list_storage.append(i)
        elif int(k) == 3:
            i = MFD()
            a.get_office_equipment(i)
            list_storage.append(i)
        print(list_storage)
    elif int(f) == 2:
        id = input("Введите id устройства")
        flag = False
        for el in list_storage:
            if el.id == id:
                a.take_office_equipment(el)
                list_not_storage.append(el)
                del el
                flag = True
                break
        if flag:
            print("Устройство передано в организацию")
        else:
            print("Устройство не найдено")

print(a.office_equipment_in_storage)




