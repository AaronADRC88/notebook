__author__ = 'aferreiradominguez'
from gi.repository import Gtk

class Libreta(Gtk.Window):

    def __init__(self):
        Gtk.Window.__init__(self,title="Libreta")
        self.set_border_width(3)

        self.notebook=Gtk.Notebook()
        self.add(self.notebook)

        self.pax1=Gtk.Box()
        self.pax1.set_border_width(10)
        self.pax1.add(Gtk.Label("pax x defecto"))
        self.notebook.append_page(self.pax1,Gtk.Label("lololo"))
        self.pax2=Gtk.Box()
        self.pax2.set_border_width(10)
        self.pax2.add(Gtk.Label("pax 2"))
        self.notebook.append_page(self.pax2,Gtk.Image.new_from_icon_name("help-about",Gtk.IconSize.MENU))


ventana = Libreta()
ventana.connect("delete-event", Gtk.main_quit)
ventana.show_all()
Gtk.main()


