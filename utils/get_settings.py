import json

from models import Settings


def get_settings() -> Settings:
    with open('settings.json', 'r', encoding='utf-8') as settings_file:
        settings_dict: dict[str, str] = json.load(settings_file)
    return Settings.parse_obj(settings_dict)
