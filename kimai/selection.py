import gi
gi.require_version('Gtk', '4.0')
gi.require_version('Adw', '1')
from gi.repository import Gtk, Adw, Gio, GObject
from kimai.projects.projects import get_projects_for_customer_id, create_project
from kimai.customers.customers import get_customers, create_customer
from kimai.activities.activities import get_activities_for_project_id, create_activity
from kimai.timesheets.timesheets import start_timesheet

class Customer(GObject.GObject):

    name = GObject.Property(type=str)

    def __init__(self, name, id):
        GObject.GObject.__init__(self)
        self.name = name
        self.id = id

    def __str__(self):
        return str(self.name)

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
    customers = []
    customers_model = None
    customer_listbox = None
    new_customer_input = None
    projects = []
    projects_model = None
    project_listbox = None
    new_project_input = None
    activities = []
    activities_model = None
    activities_listbox = None
    new_activity_input = None
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

    def get_activities(self, project_id):
        self.activities = get_activities_for_project_id(project_id)
        self.activities_model = Gio.ListStore().new(Activity)
        for activity in self.activities:
            self.activities_model.append(Activity(
                activity["name"],
                activity["id"],
                activity["project"],
            ))
        self.activities_listbox.bind_model(self.activities_model, self.create_listbox_row)

    def on_project_selected(self, listbox, row):
        if row is not None:
            project_id = self.projects_model[row.get_index()].id
            self.get_activities(project_id)

    def on_customer_selected(self, listbox, row):
        if row is not None:
            customer_id = self.customers_model[row.get_index()].id
            self.get_projects(customer_id)

    def on_new_project_clicked(self, data):
        name = self.new_project_input.get_text()
        customer_id = self.customers_model[self.customer_listbox.get_selected_row().get_index()].id
        response = create_project(name, customer_id)
        self.get_projects(customer_id)
        self.new_project_input.set_text("")

    def on_new_activity_clicked(self, data):
        new_activity_name = self.new_activity_input.get_text()
        new_activity_project_id = self.projects_model[self.project_listbox.get_selected_row().get_index()].id
        create_activity(new_activity_name, new_activity_project_id)
        self.get_activities(new_activity_project_id)
        self.new_activity_input.set_text("")

    def on_new_customer_clicked(self, data):
        new_customer_name = self.new_customer_input.get_text()
        response = create_customer(new_customer_name)
        print(response)
        self.get_customers()
        self.new_customer_input.set_text("")

    def get_projects(self, customer_id):
        self.projects_model = Gio.ListStore().new(Project)
        self.projects = get_projects_for_customer_id(customer_id)
        for project in self.projects:
            label_text = project["name"]
            self.projects_model.append(Project(label_text, project["id"]))
        self.project_listbox.bind_model(self.projects_model, self.create_listbox_row)

    def get_customers(self):
        self.customers_model = Gio.ListStore().new(Customer)
        self.customers = get_customers()
        for customer in self.customers:
            label_text = customer["name"]
            self.customers_model.append(Customer(label_text, customer["id"]))
        self.customer_listbox.bind_model(self.customers_model, self.create_listbox_row)

    def on_activate(self, app):
        self.builder = Gtk.Builder()
        self.builder.add_from_file("./user-interface/kimai.ui")

        # Customers
        self.customer_listbox = self.builder.get_object("customer_listbox")
        self.get_customers()
        self.customer_listbox.connect('row_selected', self.on_customer_selected)

        # Projects
        self.project_listbox = self.builder.get_object("project_listbox")
        #self.get_projects()
        self.project_listbox.connect('row_selected', self.on_project_selected)

        self.new_project_input = self.builder.get_object("new_project_input")
        self.new_activity_input = self.builder.get_object("new_activity_input")
        self.new_customer_input = self.builder.get_object("new_customer_input")
        new_project_button = self.builder.get_object("new_project_button")
        new_activity_button = self.builder.get_object("new_activity_button")
        new_customer_button = self.builder.get_object("new_customer_button")

        new_project_button.connect('clicked', self.on_new_project_clicked)
        new_activity_button.connect('clicked', self.on_new_activity_clicked)
        new_customer_button.connect('clicked', self.on_new_customer_clicked)

        self.activities_listbox = self.builder.get_object("activity_listbox")
        self.activities_listbox.connect('row_selected', self.on_activity_selected)

        # Obtain and show the main window
        self.win = self.builder.get_object("main_window")
        self.win.set_application(self)  # Application will close once it no longer has active windows attached to it
        self.win.present()

def select():
    app = Selector(application_id="com.namelivia.KimaiSelector")
    app.run()
