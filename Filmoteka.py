#!/usr/bin/python3
# -*- coding: utf-8 -*-
#------------------------------------------------------------------------------
# Created on 20 янв. 2017 г.
# @author: fMad
#------------------------------------------------------------------------------

#------------------------------------------------------------------------------
import sys
from PyQt5.QtWidgets import QApplication, QWidget

if __name__ == '__main__':
    app = QApplication(sys.argv)
    w = QWidget()
    w.showMaximized()
    w.setWindowTitle('Filmoteka')
    w.show()
    
    sys.exit(app.exec_())