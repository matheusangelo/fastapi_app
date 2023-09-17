from app.models import Item


fake_items_db = [{"item_name": "Foo"}, {
    "item_name": "Bar"}, {"item_name": "Baz"}]


def get_all_items() -> list:
    return fake_items_db


def create_item(item: Item) -> list:
    fake_items_db.append(
        {
            "item_name": item.name
        }
    )
    return fake_items_db
