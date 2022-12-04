class Item:
    def __init__(self, id: int, name: str, price: float, measurement_unit: str) -> None:
        self.id = id
        self.name = name
        self.price = price
        self.measurement_unit = measurement_unit

    def __repr__(self) -> str:
        return "<class 'Item'>"
