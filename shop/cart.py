from dataclasses import dataclass, field


@dataclass(frozen=True)
class Item:
    sku: str
    name: str
    price_cents: int


@dataclass
class Cart:
    lines: dict[str, int] = field(default_factory=dict)
    catalog: dict[str, Item] = field(default_factory=dict)

    def add(self, item: Item, quantity: int = 1) -> None:
        if quantity <= 0:
            raise ValueError("quantity must be positive")
        self.catalog[item.sku] = item
        self.lines[item.sku] = self.lines.get(item.sku, 0) + quantity

    def remove(self, sku: str) -> None:
        self.lines.pop(sku, None)

    def subtotal_cents(self) -> int:
        return sum(self.catalog[sku].price_cents * qty for sku, qty in self.lines.items())
