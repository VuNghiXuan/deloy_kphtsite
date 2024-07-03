from django.contrib.auth.models import Permission
from django.apps import apps

class UserInfo:
    def __init__(self, permissions, apps):
        self.permissions = permissions
        self.apps = apps
        self.user_apps = []
        self.user_app_verbose_names = []
        self.user_models = []
        self.user_model_verbose_names = []
        self.user_permissions_verbose_names = {}

    def get_app(self):
        models = apps.get_models()

        for permission in self.permissions:
            app_label, permission_name = permission.split('.')

            if app_label in self.apps.keys():
                if app_label not in self.user_apps:
                    self.user_apps.append(app_label)

                app_verbose_name = self.apps[app_label]
                if app_verbose_name not in self.user_app_verbose_names:
                    self.user_app_verbose_names.append(app_verbose_name)

                model_name = permission_name.split('_')[1]
                if model_name not in self.user_models:
                    self.user_models.append(model_name)

                for model in models:
                    if model._meta.app_label == app_label and model._meta.model_name == model_name:
                        model_verbose_name = model._meta.verbose_name
                        if model_verbose_name not in self.user_model_verbose_names:
                            self.user_model_verbose_names.append(model_verbose_name)

        return {
            'user_apps': self.user_apps,
            'user_models': self.user_models,
            'user_app_verbose_names': self.user_app_verbose_names,
            'user_model_verbose_names': self.user_model_verbose_names
        }
    
    def get_user_permissions_verbose_names(self):
        

        add = []
        delete = []
        change = []
        view = []
        
        for permission in self.permissions:
            app_label, permission_name = permission.split('.')
            permission_obj = Permission.objects.get(content_type__app_label=app_label, codename=permission_name)
            permissions_verbose_names = permission_obj.name
            # print('-----------------------------model_verbose_name  -----befor', permissions_verbose_names)
            if "Can change" in permissions_verbose_names:
                permissions_verbose_names = permissions_verbose_names.replace("Can change", "")
                change.append(permissions_verbose_names)

            if "Can view" in permissions_verbose_names:
                permissions_verbose_names =permissions_verbose_names.replace("Can view", "")
                view.append(permissions_verbose_names)

            if "Can delete" in permissions_verbose_names:
                permissions_verbose_names =permissions_verbose_names.replace("Can delete", "")
                delete.append(permissions_verbose_names)
            if "Can add" in permissions_verbose_names:
                permissions_verbose_names =permissions_verbose_names.replace("Can add", "")
                # print('-----------------------------permissions_verbose_names', permissions_verbose_names)
                add.append(permissions_verbose_names)

            # self.user_permissions_verbose_names.append(permissions_verbose_names)
        self.user_permissions_verbose_names['user_add'] = add
        self.user_permissions_verbose_names['user_delete'] = delete
        self.user_permissions_verbose_names['user_change'] = change
        self.user_permissions_verbose_names['user_view'] = view

        return self.user_permissions_verbose_names
    
