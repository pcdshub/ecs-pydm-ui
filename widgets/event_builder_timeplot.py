from os import path
import argparse

from qtpy.QtCore import Slot, Property, Qt
from qtpy.QtGui import QFont, QIntValidator

from pydm import Display
from ophyd import EpicsSignal


AXIS_LABEL_FONT_SIZE = 5
TICK_FONT = QFont()
TICK_FONT.setPixelSize(16)

class EventBuilderTimeplot(Display):
    def __init__(self, parent=None, args=None, macros=None):
        """ 
        Doc
        """
        super(EventBuilderTimeplot, self).__init__(parent=parent, args=args, macros=macros)

        # Connect signals
        self.le_timespan.returnPressed.connect(self.update_timespan)
        return

    
    def ui_filename(self):
        return 'event_builder_timeplot.ui'


    def ui_filepath(self):
        return path.join(path.dirname(path.realpath(__file__)), self.ui_filename())


    @Slot()
    def update_timespan(self):
        timespan = int(self.le_timespan.text())
        print(f'Timespan update to {timespan}s.')
        self.timeplot.setBufferSize(120*timespan)
        self.timeplot.setTimeSpan(timespan)
        return