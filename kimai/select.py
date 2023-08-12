import gi
gi.require_version('Gtk', '4.0')
gi.require_version('Adw', '1')
from gi.repository import Gtk, Adw, Gio, GObject
from kimai.projects.projects import get_projects
from kimai.activities.activities import get_activities_for_project_id
from kimai.timesheets.timesheets import start_timesheet

class Project(GObject.GObject):

    name = GObject.Property(type=str)

    def __init__(self, name, id):
        GObject.GObject.__init__(self)
        self.name = name
        self.id = id

    def __str__(self):
        return str(self.name)

class Activity(GObject.GObject):

    name = GObject.Property(type=str)

    def __init__(self, name, id, project_id):
        GObject.GObject.__init__(self)
        self.name = name
        self.id = id
        self.project_id = project_id

    def __str__(self):
        return str(self.name)



class Selector(Adw.Application):
    projects = []
    projects_model = None
    activities = []
    activities_model = None
    activities_listbox = None
    builder = None

    def __init__(self, **kwargs):
        super().__init__(**kwargs)
        self.connect('activate', self.on_activate)

    def create_listbox_row(self, label_text):
        row = Gtk.ListBoxRow()
        label = Gtk.Label(label=label_text)
        row.set_child(label)
        return row

    def on_activity_selected(self, listbox, row):
        if row is not None:
            activity = self.activities_model[row.get_index()]
            response = start_timesheet(activity.id, activity.project_id)
            self.win.close()

    def on_project_selected(self, listbox, row):
        self.activities = get_activities_for_project_id(self.projects_model[row.get_index()].id)

        self.activities_model = Gio.ListStore().new(Activity)

        for activity in self.activities:
            self.activities_model.append(Activity(
                activity["name"],
                activity["id"],
                activity["project"],
            ))
        self.activities_listbox.bind_model(self.activities_model, self.create_listbox_row)

    def on_activate(self, app):
        self.builder = Gtk.Builder()
        self.builder.add_from_file("./user-interface/kimai.ui")

        # Projects
        project_listbox = self.builder.get_object("project_listbox")
        self.projects_model = Gio.ListStore().new(Project)
        self.projects = get_projects()

        for project in self.projects:
            label_text = project["parentTitle"] + ' > ' + project["name"]
            self.projects_model.append(Project(label_text, project["id"]))
        project_listbox.bind_model(self.projects_model, self.create_listbox_row)
        project_listbox.connect('row_selected', self.on_project_selected)

        self.activities_listbox = self.builder.get_object("activity_listbox")
        self.activities_listbox.connect('row_selected', self.on_activity_selected)

        # Obtain and show the main window
        self.win = self.builder.get_object("main_window")
        self.win.set_application(self)  # Application will close once it no longer has active windows attached to it
        self.win.present()

def select():
    app = Selector(application_id="com.namelivia.KimaiSelector")
    app.run()
