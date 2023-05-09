from pyrootutils import setup_root

setup_root(__file__, cwd=True, pythonpath=True)
from storage import car_table, park_table, park_record_table


def init_db():
    car_table.truncate()
    park_table.truncate()
    park_record_table.truncate()

    park_table.insert({
        "park_id": "停车场1",
        "park_total": 100,
        "park_used": 0,
        "park_empty": 100
    })

    park_table.insert({
        "park_id": "停车场2",
        "park_total": 50,
        "park_used": 0,
        "park_empty": 50
    })


if __name__ == '__main__':
    init_db()
