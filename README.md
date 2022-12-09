# Cash Register project abstract

On this project i will apply VOC-DTP principle and see how i can break this problem into small components and work through it.

## Problem Statement - Make Cash Register

We want to create a cash register, now let's try to imagine what our register would require. Remember whenever you shop, what happens at the checkout counter, you hand over the items to the cashier, the cashier scans the items, generates an invoice, accepts payments and hands over the product.

Now, since we are only interested in Cash Register, let's further try to refine and see what happens when the cashier scans the item -

## Phase 1 -> Visualize - Outline - Code

### Step 1 - Visualize

1. Item is added to the invoice
2. If the customer wants to change the quantity, cashier simply updates the item.
3. If customer changes mind and won't to drop an item, cashier deletes the item from invoice.
4. Item may have other components such as discount or offers.
5. Additional tax may be added to the invoice.

To help you visualize, after implementing our code this is how our `Cash Register` would finally look like -

```python
{
    "customer": {
        "first_name": "Chiko",
        "last_name": "Neutron"
    },
    "invoice_total": 86.88,
    "items": {
        "Apple": {
            "discount": 2,
            "name": "Apple",
            "quantity": 8,
            "sub_total": 43.36
        },
        "Egg": {
            "discount": 12,
            "name": "Egg",
            "quantity": 48,
            "sub_total": 35.52
        },
        "Milk": {
            "discount": 10,
            "name": "Milk",
            "quantity": 4,
            "sub_total": 8.0
        }
    },
    "purchase_date": "June 01, 2022"
}
```

I could visualize this final outcome after implementing `Step 2`, but I am mentioning it here just as a visual aid and to help me imagine.

### Step 2 - Outline

Now i have a brief idea about the expectations of the cash register, let's try to outline various objects needed to create a cash register.

1. Customer - We require a customer, one who is going to make a purchase.
2. Item - The product that the customer is purchasing.
3. Invoice Entry - Just imagine you bill, whenever you purchase different items may have different discounts or offer. Individual products may also have different taxation. In order to represent this am going to need a separate object, let's call it `Invoice Item` and only include discount for the sake of simplicity.
4. Cash Register - The place where we record all these purchase transactions, while we are not going to generate an actual invoice, but you get the idea right! To keep things simple am directly going to create register, in future i may include a invoice objects and expand the code.

Let's try to summarize all the objects we are going to need -

| Sr No | Object/Class |
| ----- | ------------ |
| 1     | Customer     |
| 2     | Item         |
| 3     | InvoiceItem  |
| 4     | CashRegister |

Now since we know which objects we require, i can start coding, let's first refine the previous step and then we can actually implement the code

1. Customer

| Sr No | Instance Variables | Type   | Methods | Description |
| ----- | ------------------ | ------ | ------- | ----------- |
| 1     | First Name         | String | ----    | ------      |
| 2     | Last Name          | String | ----    | ------      |

2. Item

| Sr No | Instance Variables | Type   | Methods | Description                                       |
| ----- | ------------------ | ------ | ------- | ------------------------------------------------- |
| 1     | ID                 | Int    | ----    | Every product needs a unique ID                   |
| 2     | Name               | String | ----    | Every product needs a name                        |
| 3     | Price              | Float  | ----    | Price of the product                              |
| 4     | Measurement Unit   | String | ----    | How do you measure? It can be kg, gms, litre, etc |

3. Invoice Item

| Sr No | Instance Variables | Type  | Methods         | Description                                                      |
| ----- | ------------------ | ----- | --------------- | ---------------------------------------------------------------- |
| 1     | Item               | Item  | ----            | The item that is bring purchased                                 |
| 2     | Discount           | Float | ----            | How much discount is being offered                               |
| 3     | Quantity           | Int   | ----            | Purchase quantity                                                |
| 4     |                    | ----- | get_sub_total() | Returns the sub total of the item after subtracting the discount |

4. Cash Register

| Sr No | Instance Variables | Type       | Methods             | Description                          |
| ----- | ------------------ | ---------- | ------------------- | ------------------------------------ |
| 1     | Customer           | Customer   | ----                | Which customer is doing the purchase |
| 2     | Items              | Dictionary |                     | List of items purchased              |
| 3     | Purchase Date      | DateTime   |                     | ---                                  |
| 4     |                    | ------     | add_item()          | Add's an Item to register            |
| 4     |                    | ------     | update_item()       | Update item details                  |
| 4     |                    | ------     | remove_item()       | Remove item from register            |
| 4     |                    | ------     | get_invoice_total() | Calculates the invoice total         |
| 4     |                    | ------     | display_invoice()   | Displays the invoice                 |

What i have created here is technically known as `Unified Modelling Language Diagram`. I am just simplifying it and representing it here in a table format for your understanding.

### Step 3 - Code

copy past the code it will run on any envinroment

```python
#!/usr/bin/env python
import contextlib as __stickytape_contextlib

@__stickytape_contextlib.contextmanager
def __stickytape_temporary_dir():
    import tempfile
    import shutil
    dir_path = tempfile.mkdtemp()
    try:
        yield dir_path
    finally:
        shutil.rmtree(dir_path)

with __stickytape_temporary_dir() as __stickytape_working_dir:
    def __stickytape_write_module(path, contents):
        import os, os.path

        def make_package(path):
            parts = path.split("/")
            partial_path = __stickytape_working_dir
            for part in parts:
                partial_path = os.path.join(partial_path, part)
                if not os.path.exists(partial_path):
                    os.mkdir(partial_path)
                    with open(os.path.join(partial_path, "__init__.py"), "wb") as f:
                        f.write(b"\n")

        make_package(os.path.dirname(path))

        full_path = os.path.join(__stickytape_working_dir, path)
        with open(full_path, "wb") as module_file:
            module_file.write(contents)

    import sys as __stickytape_sys
    __stickytape_sys.path.insert(0, __stickytape_working_dir)

    __stickytape_write_module('cash_register.py', b'import json\nfrom datetime import datetime\n\nfrom customer import Customer\nfrom invoice_item import InvoiceItem\nfrom item import Item\n\n\nclass CashRegister:\n    """Cash Register for each customer"""\n\n    def __init__(self, customer: Customer) -> None:\n        self.customer = customer\n        self.items: dict[str, InvoiceItem] = {}\n        self.purchase_date = datetime.now()\n        # Private Member\n        self._invoice_total: float = 0\n\n    def __repr__(self) -> str:\n        return "<class \'CashRegister\'>"\n\n    def __str__(self) -> str:\n        return f"Customer: {self.customer}, Total Items: {len(self.items)}"\n\n    def _inc_invoice_total(self, item: InvoiceItem) -> None:\n        """Increment the total invoice value each time an item is added"""\n        self._invoice_total += item.get_sub_total()\n\n    def _dec_invoice_total(self, item: InvoiceItem) -> None:\n        """Decrement the total invoice value each time when an item is removed or updated"""\n        self._invoice_total -= item.get_sub_total()\n\n    def add_item(self, item: Item, qty: int = 1, discount: float = 0) -> None:\n        """Add\'s an item to cash register"""\n        if item.name not in self.items:\n            new_item = InvoiceItem(item, qty, discount)\n            self.items[item.name] = new_item\n            self._inc_invoice_total(new_item)\n        else:\n            print(f"{item.name} already in cart, update instead?")\n\n    def update_item(self, item: Item, qty: int, discount: float) -> None:\n        """Updates an existing item"""\n        if item.name in self.items:\n            old_item = self.items[item.name]\n            self._dec_invoice_total(old_item)\n\n            new_item = InvoiceItem(item, qty, discount)\n            self.items[item.name] = new_item\n            self._inc_invoice_total(new_item)\n        else:\n            print(f"{item.name} not in cart, purchase instead?")\n\n    def remove_item(self, item: Item) -> None:\n        """Removes item from cash register"""\n        if item.name in self.items:\n            old_item = self.items[item.name]\n            self._dec_invoice_total(old_item)\n\n            del self.items[item.name]\n\n    def get_invoice_total(self) -> float:\n        """Returns invoice total"""\n        return self._invoice_total\n\n    def display_invoice(self) -> None:\n        print()\n        print("+" * 70)\n        print(self)\n        print(f"Date: {self.purchase_date.strftime(\'%B %d, %Y\')}")\n        print("-" * 70)\n        for item in self.items.values():\n            print(item)\n        print("-" * 70)\n        print(f"Total Price: ${self.get_invoice_total():.2f}")\n        print("+" * 70)\n\n    def _get_items_as_dict(self) -> dict:\n        items_dict = {}\n        for item_name, invoice_item in self.items.items():\n            items_dict[item_name] = invoice_item.dict()\n        return items_dict\n\n    def dict(self) -> dict:\n        """Returns dictionary representation of Cash Register"""\n        cash_register = {\n            "customer": self.customer.dict(),\n            "items": self._get_items_as_dict(),\n            "purchase_date": self.purchase_date.strftime("%B %d, %Y"),\n            "invoice_total": self.get_invoice_total(),\n        }\n        return cash_register\n\n    def toJSON(self) -> str:\n        """Returns JSON formatted string of Cash Register"""\n        return json.dumps(self.dict(), indent=4, sort_keys=True)\n')
    __stickytape_write_module('customer.py', b'class Customer:\n    """Customer Details"""\n\n    def __init__(self, first_name: str, last_name: str) -> None:\n        self.first_name = first_name\n        self.last_name = last_name\n\n    def __repr__(self) -> str:\n        return "<class \'Customer\'>"\n\n    def __str__(self) -> str:\n        return f"{self.first_name} {self.last_name}"\n\n    def dict(self) -> dict:\n        return {"first_name": self.first_name, "last_name": self.last_name}\n')
    __stickytape_write_module('invoice_item.py', b'from item import Item\n\n\nclass InvoiceItem:\n    """Line Item for cash register with purchase quantity & discount"""\n\n    def __init__(self, item: Item, qty: int, discount: float = 0) -> None:\n        self.item = item\n        self.qty = qty\n        self.discount = discount\n        # Private Member\n        self._sub_total = (item.price * qty) - discount\n\n    def __repr__(self) -> str:\n        return "<class \'InvoiceItem\'>"\n\n    def __str__(self) -> str:\n        return (\n            f"Item => {self.item}, Qty: {self.qty}, Discount: ${self.discount},"\n            f" Sub Total: {self.get_sub_total():.2f}"\n        )\n\n    def get_sub_total(self) -> float:\n        """Returns the sub-total"""\n        return self._sub_total\n\n    def dict(self) -> dict:\n        """Return dictionary representation of the instance"""\n        return {\n            "name": self.item.name,\n            "quantity": self.qty,\n            "discount": self.discount,\n            "sub_total": self.get_sub_total(),\n        }\n')
    __stickytape_write_module('item.py', b'class Item:\n    """Simple Item for cash register"""\n\n    def __init__(self, id: int, name: str, price: float, measurement_unit: str) -> None:\n        self.id = id\n        self.name = name\n        self.price = price\n        self.measurement_unit = measurement_unit  # E.g -> Kg or ml\n\n    def __repr__(self) -> str:\n        return "<class \'Item\'>"\n\n    def __str__(self):\n        return f"{self.name}: ${self.price}/{self.measurement_unit}"\n\n    def dict(self) -> dict:\n        """Return dictionary representation of the instance"""\n        return self.__dict__\n')
    from cash_register import CashRegister
    from customer import Customer
    from item import Item

    milk = Item(100, "Milk", 4.5, "Litre")
    egg = Item(101, "Egg", 0.99, "Piece")
    rice = Item(102, "Rice", 4, "Kg")
    apple = Item(103, "Apple", 5.67, "Kg")

    customer1 = Customer("Louis", "Zappa")

    cr1 = CashRegister(customer1)

    cr1.add_item(milk)
    cr1.add_item(egg, 12, 0.5)
    cr1.update_item(egg, 10, 1)
    cr1.add_item(rice, 3, 0.75)
    cr1.add_item(rice, 3, 0.75)
    cr1.update_item(apple, 10, 0)

    cr1.display_invoice()

    cr1.remove_item(egg)
    cr1.display_invoice()

    customer2 = Customer("Chiko", "Neutron")
    cr2 = CashRegister(customer2)
    cr2.add_item(milk, qty=4, discount=10)
    cr2.add_item(egg, qty=25)
    cr2.update_item(egg, qty=48, discount=12)
    cr2.add_item(apple, qty=8, discount=2)
    cr2.display_invoice()

    print(cr2.toJSON())



```

As mentioned earlier, this is how our final outcome would look like -

```python
{
    "customer": {
        "first_name": "Chiko",
        "last_name": "Neutron"
    },
    "invoice_total": 86.88,
    "items": {
        "Apple": {
            "discount": 2,
            "name": "Apple",
            "quantity": 8,
            "sub_total": 43.36
        },
        "Egg": {
            "discount": 12,
            "name": "Egg",
            "quantity": 48,
            "sub_total": 35.52
        },
        "Milk": {
            "discount": 10,
            "name": "Milk",
            "quantity": 4,
            "sub_total": 8.0
        }
    },
    "purchase_date": "June 01, 2022"
}
```

What i have created a `Data Structure` which represents a `Cash Register`.

## Challange and Future development

### Challange

#### How to structure the code for scalability

My main goal on the project was to apply the knowledge learn to build a scalable code. I used OOP and create module for each class.This allowed easy testing and debugging.

#### Bundling the code together as a single source code.

After creating all module bundling the code was a challenge in to a single file.Luckly i used `stickytape` pip package to share a bundled code the full code is on the github link below ready for download.

[github project code](https://github.com/Samkiroko/Cash_register_with_python/tree/main)

## Future development:

This is just a single module for a point of sale (saas) project.

Looking to add fontend, hardware integration eg bar code scanner and more.

The project is geared to small scale business that don't have enough capital to purchase POS software.

The project will be open source.
