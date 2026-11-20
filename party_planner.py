# === Stage 1: Каркас модуля ===
# Project: PartyPlanner
from dataclasses import dataclass, field
from typing import List, Optional


@dataclass
class Guest:
    name: str
    restrictions: List[str] = field(default_factory=list)
    confirmed: bool = False
    phone: Optional[str] = None


def make_demo_guests() -> List[Guest]:
    return [
        Guest(name="Иван Иванов",
              restrictions=["вегетарианство"],
              confirmed=True,
              phone="+7 (900) 111-22-33"),
        Guest(name="Мария Смирнова",
              restrictions=["без глютена"],
              confirmed=False,
              phone="+7 (900) 444-55-66"),
        Guest(name="Алексей Петров",
              restrictions=[],
              confirmed=True,
              phone="+7 (900) 777-88-99"),
    ]


def main() -> None:
    guests = make_demo_guests()
    confirmed = [g for g in guests if g.confirmed]
    print("Планировщик вечеринок PartyPlanner")
    print("---------------------------------")
    print(f"Всего гостей: {len(guests)}")
    print(f"Подтвердили: {len(confirmed)}")
    for guest in confirmed:
        print(f"- {guest.name} ({guest.phone})")
        if guest.restrictions:
            print(f"    ограничения: {', '.join(guest.restrictions)}")
    print("---------------------------------")


if __name__ == "__main__":
    main()
