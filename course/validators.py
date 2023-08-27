from rest_framework.validators import ValidationError


class UrlValidate:
    def __init__(self, value):
        self.value = value

    def __call__(self, value):
        if "youtube.com" not in value["url"]:
            raise ValidationError("Недопустимая ссылка")
        return value
