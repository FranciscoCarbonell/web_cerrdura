from flask import render_template
from flask_appbuilder.models.sqla.interface import SQLAInterface
from flask_appbuilder import ModelView
from flask_appbuilder.widgets import ListWidget, ListThumbnail, ListBlock

from . import appbuilder, db
from . models import Application, UserApplication, Device

"""
    Create your Model based REST API::

    class MyModelApi(ModelRestApi):
        datamodel = SQLAInterface(MyModel)

    appbuilder.add_api(MyModelApi)


    Create your Views::


    class MyModelView(ModelView):
        datamodel = SQLAInterface(MyModel)


    Next, register your Views::


    appbuilder.add_view(
        MyModelView,
        "My View",
        icon="fa-folder-open-o",
        category="My Category",
        category_icon='fa-envelope'
    )
"""

"""
    Application wide 404 error handler
"""


class DeviceView(ModelView):
    datamodel = SQLAInterface(Device)
    list_columns = ['name']


class UserApplicationView(ModelView):
    datamodel = SQLAInterface(UserApplication)
    related_view = [DeviceView]
    list_columns = ['name', 'user']


class ApplicationView(ModelView):
    datamodel = SQLAInterface(Application)
    related_view = [UserApplicationView]
    list_columns = ['name']

appbuilder.add_view(
    ApplicationView,
    "Application",
    category = "application",
    category_label = "Application"
)

appbuilder.add_view(
    UserApplicationView,
    "User Applicationn",
    category = "application",
)

appbuilder.add_view(
    DeviceView,
    "Device application",
    category = "application",
)


@appbuilder.app.errorhandler(404)
def page_not_found(e):
    return (
        render_template(
            "404.html", base_template=appbuilder.base_template, appbuilder=appbuilder
        ),
        404,
    )


db.create_all()
