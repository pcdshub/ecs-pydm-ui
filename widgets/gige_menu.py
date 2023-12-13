import logging
import subprocess
from pathlib import Path

from pydm import Display
from qtpy.QtCore import Slot
from qtpy.QtWidgets import QComboBox, QVBoxLayout

logger = logging.getLogger()

GIGE_CFG_BASE = Path('/cds/group/pcds/pyps/config')


class GigeMenu(Display):
    def __init__(self, parent=None, args=None, macros=None):
        """
        Docs
        """
        super().__init__(parent=parent, args=args, macros=macros)

        if 'HUTCH' not in macros:
            raise ValueError('Please specify hutch macro. Ex: -m HUTCH=xpp')
        self.hutch = str(macros['HUTCH']).lower()

        self.giges = self.get_gige_list(self.hutch)
        logger.debug(f'Found giges: {self.giges}')
        self.setup_ui()
        self.combo_box.currentTextChanged.connect(self.launch_viewer)
        return

    def ui_filepath(self):
        # No UI file is being used
        return None

    def setup_ui(self):
        layout = QVBoxLayout()
        layout.setSizeConstraint(3)
        self.setLayout(layout)

        # Make combo box with gige entries
        self.combo_box = QComboBox(self)
        items = ['Select a GigE'] + self.giges
        self.combo_box.addItems(items)

        # Add combo box to layout
        layout.addWidget(self.combo_box)
        return

    @staticmethod
    def get_gige_list(hutch):
        """
        Parse the camviewer.cfg to retrieve a list of available GigE cameras
        for the given hutch.
        """
        giges = None
        cfg = GIGE_CFG_BASE / hutch / 'camviewer.cfg'
        giges = GigeMenu.parse_camviewer_cfg(cfg)
        return giges

    @staticmethod
    def parse_camviewer_cfg(cfg):
        giges = []
        with open(cfg, 'r') as f:
            lines = f.readlines()
            for line in lines:
                line = line.split(',')
                if line[0] != 'GE':
                    continue
                giges.append(line[3].split('\n')[0].strip())
        return giges

    @Slot(str)
    def launch_viewer(self, gige):
        cmd = f"camViewer -c {gige}"
        logger.info(f"Run {cmd}")
        subprocess.run(cmd, capture_output=True, shell=True)
