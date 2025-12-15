from typing import TypedDict 


class VegeSyncer():
    def __init__(self, shopping_list: list, customer_name: str):
        self.shopping_list = shopping_list
        self.customer_name = customer_name
    
    def getShoppingList(self) -> list:
        return self.shopping_list
    
    def addItem(self, item: str) -> None:
        self.shopping_list.append(item)
    
    def getSize(self) -> int:
        return len(self.shopping_list)
    
    def test(self) -> int:
        return 1
    
    def h(self) -> bool:
        if self.customer_name:
            return True
        return False
