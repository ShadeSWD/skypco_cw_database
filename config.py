import os

DB_CONNECTION_STRING = f"dbname=vacancies user=postgres host=localhost port=5432 password={os.getenv('pgAdmin')}"
QUERIES_PATH = os.path.normpath("src/database/queries.sql")
EMPLOYERS_VACANCY_ID = {
    "ADV": 421950,
    "МФТИ": 1008541,
    "АВСофт": 2355830,
    "Северсталь": 6041,
    "ЛАНИТ": 733,
    "ТЕНЗОР": 1266214,
    "Рексфот": 3984,
    "VK": 15478,
    "МДО": 736233,
    "точка": 2324020,
    "RAMAXGroup": 142514,
    "ASTON": 6093775,
    "HFLabs": 15589,
    "IBS": 139,
    "Крит": 1115346,
    "ПервыйБит": 3177,
    "Алгоритмика": 2657797
}
