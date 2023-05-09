from time import time
from storage import car_table, park_table, park_record_table
from utils.Clogging import ColoredLogger
from tinydb import Query

logger = ColoredLogger('Database')


def car_entry(car_id: str, car_type: str, car_image: str, car_park: str):
    logger.debug(f'car_entry handle: {car_id}, {car_type}, {car_image}')

    # 1. change car status
    Car = Query()

    car_table.upsert({
        "car_id": car_id,
        "car_type": car_type,
        "car_status": "在场",
        "car_park": car_park
    }, Car.car_id == car_id)

    # 2. add park record
    park_record_table.insert({
        "car_id": car_id,
        "park_id": car_park,
        "park_entry_time": time(),
        "park_leave_time": 0,
        "park_fee": 0,
        "park_status": "在场",
        "park_image": car_image
    })

    # 3. change park status
    Park = Query()
    park = park_table.get(Park.park_id == car_park)

    park_table.update({
        "park_id": park["park_id"],
        "park_total": park["park_total"],
        "park_used": park["park_used"] + 1,
        "park_empty": park["park_empty"] - 1
    }, Park.park_id == car_park)

    logger.info(f'car_entry success: {car_id}, {car_type}, {car_image} done')


def car_leave(car_id: str, car_image: str):
    logger.debug(f'car_leave handle: {car_id}, {car_image}')

    # 1. change car status
    Car = Query()

    car_table.update({
        "car_status": "离场",
    }, Car.car_id == car_id)

    # 2. change park record
    ParkRecord = Query()
    # 寻找最后一条记录
    park_record = park_record_table.search(ParkRecord.car_id == car_id)[-1]

    park_record_table.insert({
        "car_id": park_record["car_id"],
        "park_id": park_record["park_id"],
        "park_entry_time": park_record["park_entry_time"],
        "park_leave_time": time(),
        "park_fee": (time() - park_record["park_entry_time"]) / 60,  # 1 rmb / min
        "park_status": "离场",
        "park_image": car_image
    })

    # 3. change park status
    Park = Query()
    park = park_table.get(Park.park_id == park_record["park_id"])

    park_table.update({
        "park_id": park["park_id"],
        "park_total": park["park_total"],
        "park_used": park["park_used"] - 1,
        "park_empty": park["park_empty"] + 1
    }, Park.park_id == park_record["park_id"])

    logger.info(f'car_leave success: {car_id}, {car_image} done')
