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

    def add_many(self, items: list[Item], seen: list[str] = []) -> None:
        """Add items, skipping duplicates within the same call."""
        for item in items:
            if item.sku in seen:
                continue
            seen.append(item.sku)
            self.add(item)

    def set_quantity(self, sku: str, quantity: int) -> None:
        self.lines[sku] = quantity

    def most_expensive(self, n: int) -> list[Item]:
        items = [self.catalog[sku] for sku in self.lines]
        result = []
        while len(result) < n:
            best = None
            for item in items:
                if item not in result and (best is None or item.price_cents > best.price_cents):
                    best = item
            result.append(best)
        return result

    def subtotal_cents(self) -> int:
        return sum(self.catalog[sku].price_cents * qty for sku, qty in self.lines.items())
