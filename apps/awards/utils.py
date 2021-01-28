from django.apps import apps

def get_choice_all_models(app_name):
    return tuple(apps.get_app_config(app_name).get_models())