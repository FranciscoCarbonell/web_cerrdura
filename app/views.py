from flask import render_template
from flask_appbuilder.models.sqla.interface import SQLAInterface
from flask_appbuilder import ModelView, ModelRestApi

from . import appbuilder, db
from . models import Application, UserApplication

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

class UserApplicationView(ModelView):
    datamodel = SQLAInterface(UserApplication)


class ApplicationView(ModelView):
    datamodel = SQLAInterface(Application)
    related_view = [UserApplicationView]

appbuilder.add_view(
    ApplicationView,
    "Application",
    category = "application",
    category_label = "Application"
)

appbuilder.add_view(
    UserApplicationView,
    "User Application",
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
