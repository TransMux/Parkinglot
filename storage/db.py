from tinydb import TinyDB


class Car:
    car_id: str  # 车牌
    car_type: str  # 临时停车，月租车，特殊车辆
    car_status: str  # 在场，离场
    car_park: str  # 停车场


car_table = TinyDB('./data/db/车辆信息.json')


class Park:
    park_id: str
    park_total: int
    park_used: int
    park_empty: int


park_table = TinyDB('./data/db/停车场信息.json')


class ParkRecord:
    car_id: str
    park_id: str
    park_entry_time: int
    park_leave_time: int
    park_fee: float
    park_status: str
    park_image: str


park_record_table = TinyDB('./data/db/停车记录.json')
