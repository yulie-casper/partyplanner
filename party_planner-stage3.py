# === Stage 3: Хранилище в памяти ===
# Project: PartyPlanner
from datetime import datetime


class Guest:
    def __init__(self, name, restrictions, confirmed, phone):
        self.id = None
        self.name = name
        self.restrictions = restrictions
        self.confirmed = confirmed
        self.phone = phone

    def __repr__(self):
        return f"Guest(id={self.id!r}, name={self.name!r}, " \
               f"restrictions={self.restrictions!r}, " \
               f"confirmed={self.confirmed!r}, phone={self.phone!r})"


GuestStore = type("GuestStore", (), {
    "instance": None,
    "store": {},
    "counter": 0,
})()


def get_guest_store():
    if GuestStore.instance is None:
        GuestStore.instance = GuestStore()
    return GuestStore.instance


class GuestStore:
    def __init__(self):
        self._store = {}
        self._counter = 0

    def add_guest(self, name, restrictions, confirmed, phone):
        self._counter += 1
        guest = Guest(self._counter, name, restrictions, confirmed, phone)
        self._store[guest.id] = guest
        return guest

    def get_guest(self, guest_id):
        return self._store.get(guest_id)

    def list_guests(self):
        return list(self._store.values())


def create_guest(name, restrictions, confirmed, phone):
    store = get_guest_store()
    return store.add_guest(name, restrictions, confirmed, phone)


def fetch_guest(guest_id):
    store = get_guest_store()
    return store.get_guest(guest_id)


def list_all_guests():
    store = get_guest_store()
    return store.list_guests()


def demo():
    alice = create_guest("Алиса", ["нет глютена"], True, "+79001112233")
    bob = create_guest("Боб", [], False, "+79004445566")
    print("Добавлено гостей:", list_all_guests())
    print("Гость по id 1:", fetch_guest(alice.id))
    print("Гость по id 999:", fetch_guest(999))


if __name__ == "__main__":
    demo()
