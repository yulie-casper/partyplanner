# === Stage 2: Проверка полей ===
# Project: PartyPlanner
import re


def normalize_name(raw):
    return " ".join(raw.strip().lower().split())


def normalize_phone(raw):
    digits = re.sub(r"\D", "", raw)
    if len(digits) > 11:
        digits = digits[1:]
    return f"+7 ({digits[0:3]}) {digits[3:6]}-{digits[6:8]}-{digits[8:10]}"


def normalize_restriction(raw):
    text = raw.strip().lower()
    if not text:
        return "нет"
    return text.replace("и", ", ").strip()


def normalize_confirmation(raw):
    text = raw.strip().lower()
    if text in ("да", "yes", "y", "1", "confirm"):
        return True
    if text in ("нет", "no", "n", "0", "decline"):
        return False
    raise ValueError("Подтверждение должно быть 'да' или 'нет'")


class GuestValidation:
    MIN_NAME_LENGTH = 2
    MAX_NAME_LENGTH = 60
    PHONE_PATTERN = re.compile(r"^\+?\d{10,11}$")

    def __init__(self, name, restriction, confirmation, phone):
        self.errors = []
        self._validate_name(name)
        self._validate_restriction(restriction)
        self._validate_confirmation(confirmation)
        self._validate_phone(phone)
        return self

    def _validate_name(self, value):
        normalized = normalize_name(value)
        if not normalized:
            self.errors.append("Имя обязательно")
            return
        if len(normalized) < self.MIN_NAME_LENGTH:
            self.errors.append("Имя должно содержать не менее двух символов")
        if len(normalized) > self.MAX_NAME_LENGTH:
            self.errors.append("Имя слишком длинное")
        self.name = normalized

    def _validate_restriction(self, value):
        normalized = normalize_restriction(value)
        if not normalized:
            self.errors.append("Укажите ограничение для гостя")
            return
        self.restriction = normalized

    def _validate_confirmation(self, value):
        self.confirmation = normalize_confirmation(value)

    def _validate_phone(self, value):
        digits = re.sub(r"\D", "", value)
        if not digits:
            self.errors.append("Телефон обязателен")
            return
        if len(digits) < 10 or len(digits) > 11:
            self.errors.append("Телефон должен содержать 10 или 11 цифр")
            return
        if not self.PHONE_PATTERN.match(value.strip()):
            self.errors.append("Телефон должен начинаться с +")
        self.phone = normalize_phone(value)

    def is_valid(self):
        return not self.errors

    def get_errors(self):
        return list(self.errors)
