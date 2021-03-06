# -*- coding: UTF-8 -*-
from PyQt4.QtGui import *

class CssPalette(object):
    """
    Expose a Qt palette to Jinja. If one exposes an object name "palette" in
    Jinja, then it is possible to access the palette as: {{ palette.window }}
    the part after "palette." can be any Qt color role.
    """
    def __init__(self, qpalette):
        self.qpalette = qpalette

    def __getattr__(self, name):
        try:
            getter = getattr(self.qpalette, name)
        except AttributeError:
            print "No such color role '%s'" % name
            return CssColor(QColor("purple"))
        brush = getter()
        return CssColor(brush.color())

class CssColor(object):
    def __init__(self, qcolor):
        self.qcolor = qcolor

    def darker(self, percent):
        return CssColor(self.qcolor.darker(percent))

    def lighter(self, percent):
        return CssColor(self.qcolor.lighter(percent))

    def __str__(self):
        return unicode(self.qcolor.name())
