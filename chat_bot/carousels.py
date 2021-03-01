import mysql.connector
from mysql.connector import Error
from . import db


my_db = mysql.connector.connect(
    host='localhost',
    user='root',
    password='',
    database='vk_chatbot_db'
)

select_db = "SELECT * from vk_chatbot_db.merchandise"
my_cursor = my_db.cursor()
products = db.execute_read_query(my_db, select_db)

categories = {
    "type": "carousel",
    "elements": [{
        "photo_id": "-202691820_457239026",
        "action": {
            "type": "open_photo"
        },
        "buttons": [{
            "action": {
                "type": "text",
                "label": products[4][0],
                "payload": "{}"
            }
        }]
    },
    {
        "photo_id": "-202691820_457239028",
        "action": {
            "type": "open_photo"
        },
        "buttons": [{
            "action": {
                "type": "text",
                "label": products[0][0],
                "payload": "{}"
            }
        }]
    },
        {
        "photo_id": "-202691820_457239027",
        "action": {
            "type": "open_photo"
        },
        "buttons": [{
            "action": {
                "type": "text",
                "label": products[2][0],
                "payload": "{}"
                }
            }]
        }
    ]
}


cat_pies = {
    "type": "carousel",
    "elements": [{
        "photo_id": "-202691820_457239026",
        "action": {
            "type": "open_photo"

        },
        "buttons": [{
            "action": {
                "type": "text",
                "label": products[5][1],
                "payload": "{}"
            }
        }]
    },
    {
        "photo_id": "-202691820_457239029",
        "action": {
            "type": "open_photo"
        },
        "buttons": [{
            "action": {
                "type": "text",
                "label": products[4][1],
                "payload": "{}"
                }
            }]
        }
    ]
}

cat_conf_products = {
    "type": "carousel",
    "elements": [{
        "photo_id": "-202691820_457239030",
        "action": {
            "type": "open_photo"

        },
        "buttons": [{
            "action": {
                "type": "text",
                "label": products[0][1],
                "payload": "{}"
            }
        }]
    },
    {
        "photo_id": "-202691820_457239028",
        "action": {
            "type": "open_photo"
        },
        "buttons": [{
            "action": {
                "type": "text",
                "label": products[1][1],
                "payload": "{}"
                }
            }]
        }
    ]
}

cat_flour_products = {
    "type": "carousel",
    "elements": [{
        "photo_id": "-202691820_457239027",
        "action": {
            "type": "open_photo"

        },
        "buttons": [{
            "action": {
                "type": "text",
                "label": products[2][1],
                "payload": "{}"
            }
        }]
    },
    {
        "photo_id": "-202691820_457239031",
        "action": {
            "type": "open_photo"
        },
        "buttons": [{
            "action": {
                "type": "text",
                "label": products[3][1],
                "payload": "{}"
                }
            }]
        }
    ]
}