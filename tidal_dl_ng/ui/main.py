################################################################################
## Form generated from reading UI file 'main.ui'
##
## Created by: Qt User Interface Compiler version 6.6.1
##
## WARNING! All changes made in this file will be lost when recompiling UI file!
################################################################################

from PySide6.QtCore import QCoreApplication, QLocale, QMetaObject, QRect, QSize, Qt
from PySide6.QtGui import QAction, QFont, QPixmap
from PySide6.QtWidgets import (
    QAbstractItemView,
    QComboBox,
    QFrame,
    QHBoxLayout,
    QLabel,
    QLineEdit,
    QMenu,
    QMenuBar,
    QPlainTextEdit,
    QPushButton,
    QSizePolicy,
    QStatusBar,
    QTableWidget,
    QTableWidgetItem,
    QTreeWidget,
    QTreeWidgetItem,
    QVBoxLayout,
    QWidget,
)


class Ui_MainWindow:
    def setupUi(self, MainWindow):
        if not MainWindow.objectName():
            MainWindow.setObjectName("MainWindow")
        MainWindow.resize(1200, 800)
        self.a_preferences = QAction(MainWindow)
        self.a_preferences.setObjectName("a_preferences")
        self.a_preferences.setEnabled(True)
        self.a_preferences.setText("Preferences...")
        self.a_preferences.setIconText("Preferences...")
        # if QT_CONFIG(tooltip)
        self.a_preferences.setToolTip("Preferences...")
        # endif // QT_CONFIG(tooltip)
        # if QT_CONFIG(statustip)
        self.a_preferences.setStatusTip("")
        # endif // QT_CONFIG(statustip)
        # if QT_CONFIG(whatsthis)
        self.a_preferences.setWhatsThis("")
        # endif // QT_CONFIG(whatsthis)
        self.a_version = QAction(MainWindow)
        self.a_version.setObjectName("a_version")
        self.a_exit = QAction(MainWindow)
        self.a_exit.setObjectName("a_exit")
        self.a_logout = QAction(MainWindow)
        self.a_logout.setObjectName("a_logout")
        self.a_updates_check = QAction(MainWindow)
        self.a_updates_check.setObjectName("a_updates_check")
        self.w_central = QWidget(MainWindow)
        self.w_central.setObjectName("w_central")
        self.w_central.setEnabled(True)
        sizePolicy = QSizePolicy(QSizePolicy.Preferred, QSizePolicy.Expanding)
        sizePolicy.setHorizontalStretch(100)
        sizePolicy.setVerticalStretch(100)
        sizePolicy.setHeightForWidth(self.w_central.sizePolicy().hasHeightForWidth())
        self.w_central.setSizePolicy(sizePolicy)
        # if QT_CONFIG(tooltip)
        self.w_central.setToolTip("")
        # endif // QT_CONFIG(tooltip)
        # if QT_CONFIG(statustip)
        self.w_central.setStatusTip("")
        # endif // QT_CONFIG(statustip)
        # if QT_CONFIG(whatsthis)
        self.w_central.setWhatsThis("")
        # endif // QT_CONFIG(whatsthis)
        # if QT_CONFIG(accessibility)
        self.w_central.setAccessibleName("")
        # endif // QT_CONFIG(accessibility)
        # if QT_CONFIG(accessibility)
        self.w_central.setAccessibleDescription("")
        # endif // QT_CONFIG(accessibility)
        self.horizontalLayout = QHBoxLayout(self.w_central)
        self.horizontalLayout.setObjectName("horizontalLayout")
        self.lv_list_user = QVBoxLayout()
        self.lv_list_user.setObjectName("lv_list_user")
        self.tr_lists_user = QTreeWidget(self.w_central)
        __qtreewidgetitem = QTreeWidgetItem()
        __qtreewidgetitem.setText(2, "Info")
        __qtreewidgetitem.setText(0, "Name")
        self.tr_lists_user.setHeaderItem(__qtreewidgetitem)
        __qtreewidgetitem1 = QTreeWidgetItem(self.tr_lists_user)
        __qtreewidgetitem1.setFlags(Qt.ItemIsEnabled)
        __qtreewidgetitem2 = QTreeWidgetItem(self.tr_lists_user)
        __qtreewidgetitem2.setFlags(Qt.ItemIsEnabled)
        __qtreewidgetitem3 = QTreeWidgetItem(self.tr_lists_user)
        __qtreewidgetitem3.setFlags(Qt.ItemIsEnabled)
        self.tr_lists_user.setObjectName("tr_lists_user")
        # if QT_CONFIG(tooltip)
        self.tr_lists_user.setToolTip("")
        # endif // QT_CONFIG(tooltip)
        # if QT_CONFIG(statustip)
        self.tr_lists_user.setStatusTip("")
        # endif // QT_CONFIG(statustip)
        # if QT_CONFIG(whatsthis)
        self.tr_lists_user.setWhatsThis("")
        # endif // QT_CONFIG(whatsthis)
        # if QT_CONFIG(accessibility)
        self.tr_lists_user.setAccessibleName("")
        # endif // QT_CONFIG(accessibility)
        # if QT_CONFIG(accessibility)
        self.tr_lists_user.setAccessibleDescription("")
        # endif // QT_CONFIG(accessibility)
        self.tr_lists_user.setEditTriggers(QAbstractItemView.NoEditTriggers)
        self.tr_lists_user.setProperty("showDropIndicator", False)
        self.tr_lists_user.setIndentation(10)
        self.tr_lists_user.setUniformRowHeights(True)
        self.tr_lists_user.setSortingEnabled(True)
        self.tr_lists_user.header().setCascadingSectionResizes(True)
        self.tr_lists_user.header().setHighlightSections(True)
        self.tr_lists_user.header().setProperty("showSortIndicator", True)

        self.lv_list_user.addWidget(self.tr_lists_user)

        self.lv_list_control = QHBoxLayout()
        self.lv_list_control.setObjectName("lv_list_control")
        self.pb_reload_user_lists = QPushButton(self.w_central)
        self.pb_reload_user_lists.setObjectName("pb_reload_user_lists")
        sizePolicy1 = QSizePolicy(QSizePolicy.Expanding, QSizePolicy.Fixed)
        sizePolicy1.setHorizontalStretch(0)
        sizePolicy1.setVerticalStretch(0)
        sizePolicy1.setHeightForWidth(self.pb_reload_user_lists.sizePolicy().hasHeightForWidth())
        self.pb_reload_user_lists.setSizePolicy(sizePolicy1)

        self.lv_list_control.addWidget(self.pb_reload_user_lists)

        self.pb_download_list = QPushButton(self.w_central)
        self.pb_download_list.setObjectName("pb_download_list")
        sizePolicy1.setHeightForWidth(self.pb_download_list.sizePolicy().hasHeightForWidth())
        self.pb_download_list.setSizePolicy(sizePolicy1)

        self.lv_list_control.addWidget(self.pb_download_list)

        self.lv_list_user.addLayout(self.lv_list_control)

        self.horizontalLayout.addLayout(self.lv_list_user)

        self.lv_search_result = QVBoxLayout()
        # ifndef Q_OS_MAC
        self.lv_search_result.setSpacing(-1)
        # endif
        self.lv_search_result.setObjectName("lv_search_result")
        self.lh_search = QHBoxLayout()
        self.lh_search.setObjectName("lh_search")
        self.l_search = QLineEdit(self.w_central)
        self.l_search.setObjectName("l_search")
        self.l_search.setAcceptDrops(False)
        # if QT_CONFIG(tooltip)
        self.l_search.setToolTip("")
        # endif // QT_CONFIG(tooltip)
        # if QT_CONFIG(statustip)
        self.l_search.setStatusTip("")
        # endif // QT_CONFIG(statustip)
        # if QT_CONFIG(whatsthis)
        self.l_search.setWhatsThis("")
        # endif // QT_CONFIG(whatsthis)
        # if QT_CONFIG(accessibility)
        self.l_search.setAccessibleName("")
        # endif // QT_CONFIG(accessibility)
        # if QT_CONFIG(accessibility)
        self.l_search.setAccessibleDescription("")
        # endif // QT_CONFIG(accessibility)
        self.l_search.setLocale(QLocale(QLocale.English, QLocale.UnitedStates))
        self.l_search.setText("")
        self.l_search.setPlaceholderText("Type and press ENTER to search...")
        self.l_search.setClearButtonEnabled(True)

        self.lh_search.addWidget(self.l_search)

        self.cb_search_type = QComboBox(self.w_central)
        self.cb_search_type.setObjectName("cb_search_type")
        # if QT_CONFIG(tooltip)
        self.cb_search_type.setToolTip("")
        # endif // QT_CONFIG(tooltip)
        # if QT_CONFIG(statustip)
        self.cb_search_type.setStatusTip("")
        # endif // QT_CONFIG(statustip)
        # if QT_CONFIG(whatsthis)
        self.cb_search_type.setWhatsThis("")
        # endif // QT_CONFIG(whatsthis)
        # if QT_CONFIG(accessibility)
        self.cb_search_type.setAccessibleName("")
        # endif // QT_CONFIG(accessibility)
        # if QT_CONFIG(accessibility)
        self.cb_search_type.setAccessibleDescription("")
        # endif // QT_CONFIG(accessibility)
        self.cb_search_type.setCurrentText("")
        self.cb_search_type.setPlaceholderText("")

        self.lh_search.addWidget(self.cb_search_type)

        self.pb_search = QPushButton(self.w_central)
        self.pb_search.setObjectName("pb_search")
        # if QT_CONFIG(statustip)
        self.pb_search.setStatusTip("")
        # endif // QT_CONFIG(statustip)
        # if QT_CONFIG(whatsthis)
        self.pb_search.setWhatsThis("")
        # endif // QT_CONFIG(whatsthis)
        # if QT_CONFIG(accessibility)
        self.pb_search.setAccessibleName("")
        # endif // QT_CONFIG(accessibility)
        # if QT_CONFIG(accessibility)
        self.pb_search.setAccessibleDescription("")
        # endif // QT_CONFIG(accessibility)
        self.pb_search.setText("Search")
        # if QT_CONFIG(shortcut)
        self.pb_search.setShortcut("")
        # endif // QT_CONFIG(shortcut)

        self.lh_search.addWidget(self.pb_search)

        self.lv_search_result.addLayout(self.lh_search)

        self.tr_results = QTreeWidget(self.w_central)
        self.tr_results.setObjectName("tr_results")
        self.tr_results.setEditTriggers(QAbstractItemView.NoEditTriggers)
        self.tr_results.setProperty("showDropIndicator", False)
        self.tr_results.setDragDropOverwriteMode(False)
        self.tr_results.setAlternatingRowColors(False)
        self.tr_results.setSelectionMode(QAbstractItemView.ExtendedSelection)
        self.tr_results.setIndentation(10)
        self.tr_results.setSortingEnabled(True)
        self.tr_results.header().setProperty("showSortIndicator", True)
        self.tr_results.header().setStretchLastSection(False)

        self.lv_search_result.addWidget(self.tr_results)

        self.lh_download = QHBoxLayout()
        self.lh_download.setObjectName("lh_download")
        self.l_quality_audio = QLabel(self.w_central)
        self.l_quality_audio.setObjectName("l_quality_audio")
        # if QT_CONFIG(tooltip)
        self.l_quality_audio.setToolTip("")
        # endif // QT_CONFIG(tooltip)
        # if QT_CONFIG(statustip)
        self.l_quality_audio.setStatusTip("")
        # endif // QT_CONFIG(statustip)
        # if QT_CONFIG(whatsthis)
        self.l_quality_audio.setWhatsThis("")
        # endif // QT_CONFIG(whatsthis)
        # if QT_CONFIG(accessibility)
        self.l_quality_audio.setAccessibleName("")
        # endif // QT_CONFIG(accessibility)
        # if QT_CONFIG(accessibility)
        self.l_quality_audio.setAccessibleDescription("")
        # endif // QT_CONFIG(accessibility)
        self.l_quality_audio.setText("Audio")
        self.l_quality_audio.setAlignment(Qt.AlignRight | Qt.AlignTrailing | Qt.AlignVCenter)

        self.lh_download.addWidget(self.l_quality_audio)

        self.cb_quality_audio = QComboBox(self.w_central)
        self.cb_quality_audio.setObjectName("cb_quality_audio")
        # if QT_CONFIG(tooltip)
        self.cb_quality_audio.setToolTip("")
        # endif // QT_CONFIG(tooltip)
        # if QT_CONFIG(statustip)
        self.cb_quality_audio.setStatusTip("")
        # endif // QT_CONFIG(statustip)
        # if QT_CONFIG(whatsthis)
        self.cb_quality_audio.setWhatsThis("")
        # endif // QT_CONFIG(whatsthis)
        # if QT_CONFIG(accessibility)
        self.cb_quality_audio.setAccessibleName("")
        # endif // QT_CONFIG(accessibility)
        # if QT_CONFIG(accessibility)
        self.cb_quality_audio.setAccessibleDescription("")
        # endif // QT_CONFIG(accessibility)
        self.cb_quality_audio.setCurrentText("")
        self.cb_quality_audio.setPlaceholderText("")
        self.cb_quality_audio.setFrame(True)

        self.lh_download.addWidget(self.cb_quality_audio)

        self.l_quality_video = QLabel(self.w_central)
        self.l_quality_video.setObjectName("l_quality_video")
        # if QT_CONFIG(tooltip)
        self.l_quality_video.setToolTip("")
        # endif // QT_CONFIG(tooltip)
        # if QT_CONFIG(statustip)
        self.l_quality_video.setStatusTip("")
        # endif // QT_CONFIG(statustip)
        # if QT_CONFIG(whatsthis)
        self.l_quality_video.setWhatsThis("")
        # endif // QT_CONFIG(whatsthis)
        # if QT_CONFIG(accessibility)
        self.l_quality_video.setAccessibleName("")
        # endif // QT_CONFIG(accessibility)
        # if QT_CONFIG(accessibility)
        self.l_quality_video.setAccessibleDescription("")
        # endif // QT_CONFIG(accessibility)
        self.l_quality_video.setText("Video")
        self.l_quality_video.setAlignment(Qt.AlignRight | Qt.AlignTrailing | Qt.AlignVCenter)

        self.lh_download.addWidget(self.l_quality_video)

        self.cb_quality_video = QComboBox(self.w_central)
        self.cb_quality_video.setObjectName("cb_quality_video")
        # if QT_CONFIG(tooltip)
        self.cb_quality_video.setToolTip("")
        # endif // QT_CONFIG(tooltip)
        # if QT_CONFIG(statustip)
        self.cb_quality_video.setStatusTip("")
        # endif // QT_CONFIG(statustip)
        # if QT_CONFIG(whatsthis)
        self.cb_quality_video.setWhatsThis("")
        # endif // QT_CONFIG(whatsthis)
        # if QT_CONFIG(accessibility)
        self.cb_quality_video.setAccessibleName("")
        # endif // QT_CONFIG(accessibility)
        # if QT_CONFIG(accessibility)
        self.cb_quality_video.setAccessibleDescription("")
        # endif // QT_CONFIG(accessibility)
        self.cb_quality_video.setCurrentText("")
        self.cb_quality_video.setPlaceholderText("")

        self.lh_download.addWidget(self.cb_quality_video)

        self.pb_download = QPushButton(self.w_central)
        self.pb_download.setObjectName("pb_download")
        # if QT_CONFIG(tooltip)
        self.pb_download.setToolTip("")
        # endif // QT_CONFIG(tooltip)
        # if QT_CONFIG(statustip)
        self.pb_download.setStatusTip("")
        # endif // QT_CONFIG(statustip)
        # if QT_CONFIG(whatsthis)
        self.pb_download.setWhatsThis("")
        # endif // QT_CONFIG(whatsthis)
        # if QT_CONFIG(accessibility)
        self.pb_download.setAccessibleName("")
        # endif // QT_CONFIG(accessibility)
        # if QT_CONFIG(accessibility)
        self.pb_download.setAccessibleDescription("")
        # endif // QT_CONFIG(accessibility)
        self.pb_download.setText("Download")
        # if QT_CONFIG(shortcut)
        self.pb_download.setShortcut("")
        # endif // QT_CONFIG(shortcut)

        self.lh_download.addWidget(self.pb_download)

        self.lh_download.setStretch(0, 5)
        self.lh_download.setStretch(2, 5)
        self.lh_download.setStretch(4, 15)

        self.lv_search_result.addLayout(self.lh_download)

        self.te_debug = QPlainTextEdit(self.w_central)
        self.te_debug.setObjectName("te_debug")
        self.te_debug.setEnabled(True)
        sizePolicy2 = QSizePolicy(QSizePolicy.Expanding, QSizePolicy.Maximum)
        sizePolicy2.setHorizontalStretch(0)
        sizePolicy2.setVerticalStretch(0)
        sizePolicy2.setHeightForWidth(self.te_debug.sizePolicy().hasHeightForWidth())
        self.te_debug.setSizePolicy(sizePolicy2)
        self.te_debug.setMaximumSize(QSize(16777215, 16777215))
        self.te_debug.setAcceptDrops(False)
        # if QT_CONFIG(tooltip)
        self.te_debug.setToolTip("")
        # endif // QT_CONFIG(tooltip)
        # if QT_CONFIG(statustip)
        self.te_debug.setStatusTip("")
        # endif // QT_CONFIG(statustip)
        # if QT_CONFIG(whatsthis)
        self.te_debug.setWhatsThis("")
        # endif // QT_CONFIG(whatsthis)
        # if QT_CONFIG(accessibility)
        self.te_debug.setAccessibleName("")
        # endif // QT_CONFIG(accessibility)
        # if QT_CONFIG(accessibility)
        self.te_debug.setAccessibleDescription("")
        # endif // QT_CONFIG(accessibility)
        self.te_debug.setUndoRedoEnabled(False)
        self.te_debug.setReadOnly(True)

        self.lv_search_result.addWidget(self.te_debug)

        self.horizontalLayout.addLayout(self.lv_search_result)

        self.lv_info = QVBoxLayout()
        self.lv_info.setObjectName("lv_info")
        self.lv_info_item = QVBoxLayout()
        self.lv_info_item.setObjectName("lv_info_item")
        self.horizontalLayout_2 = QHBoxLayout()
        self.horizontalLayout_2.setObjectName("horizontalLayout_2")
        self.l_pm_cover = QLabel(self.w_central)
        self.l_pm_cover.setObjectName("l_pm_cover")
        sizePolicy3 = QSizePolicy(QSizePolicy.Fixed, QSizePolicy.Fixed)
        sizePolicy3.setHorizontalStretch(0)
        sizePolicy3.setVerticalStretch(0)
        sizePolicy3.setHeightForWidth(self.l_pm_cover.sizePolicy().hasHeightForWidth())
        self.l_pm_cover.setSizePolicy(sizePolicy3)
        self.l_pm_cover.setMaximumSize(QSize(280, 280))
        self.l_pm_cover.setBaseSize(QSize(0, 0))
        self.l_pm_cover.setFrameShape(QFrame.NoFrame)
        self.l_pm_cover.setPixmap(QPixmap("default_album_image.png"))
        self.l_pm_cover.setScaledContents(True)
        self.l_pm_cover.setAlignment(Qt.AlignHCenter | Qt.AlignTop)

        self.horizontalLayout_2.addWidget(self.l_pm_cover)

        self.lv_info_item.addLayout(self.horizontalLayout_2)

        self.lv_info.addLayout(self.lv_info_item)

        self.lv_queue_dl = QVBoxLayout()
        self.lv_queue_dl.setObjectName("lv_queue_dl")
        self.l_h_queue_dl = QLabel(self.w_central)
        self.l_h_queue_dl.setObjectName("l_h_queue_dl")
        font = QFont()
        font.setBold(True)
        font.setItalic(False)
        font.setKerning(True)
        self.l_h_queue_dl.setFont(font)

        self.lv_queue_dl.addWidget(self.l_h_queue_dl)

        self.ta_queue_dl = QTableWidget(self.w_central)
        if self.ta_queue_dl.columnCount() < 5:
            self.ta_queue_dl.setColumnCount(5)
        __qtablewidgetitem = QTableWidgetItem()
        __qtablewidgetitem.setTextAlignment(Qt.AlignLeading | Qt.AlignVCenter)
        self.ta_queue_dl.setHorizontalHeaderItem(0, __qtablewidgetitem)
        __qtablewidgetitem1 = QTableWidgetItem()
        self.ta_queue_dl.setHorizontalHeaderItem(1, __qtablewidgetitem1)
        __qtablewidgetitem2 = QTableWidgetItem()
        __qtablewidgetitem2.setTextAlignment(Qt.AlignLeading | Qt.AlignVCenter)
        self.ta_queue_dl.setHorizontalHeaderItem(2, __qtablewidgetitem2)
        __qtablewidgetitem3 = QTableWidgetItem()
        __qtablewidgetitem3.setTextAlignment(Qt.AlignLeading | Qt.AlignVCenter)
        self.ta_queue_dl.setHorizontalHeaderItem(3, __qtablewidgetitem3)
        __qtablewidgetitem4 = QTableWidgetItem()
        __qtablewidgetitem4.setTextAlignment(Qt.AlignLeading | Qt.AlignVCenter)
        self.ta_queue_dl.setHorizontalHeaderItem(4, __qtablewidgetitem4)
        self.ta_queue_dl.setObjectName("ta_queue_dl")
        self.ta_queue_dl.setEditTriggers(QAbstractItemView.NoEditTriggers)
        self.ta_queue_dl.setTabKeyNavigation(False)
        self.ta_queue_dl.setProperty("showDropIndicator", False)
        self.ta_queue_dl.setDragDropOverwriteMode(False)
        self.ta_queue_dl.setSelectionMode(QAbstractItemView.ExtendedSelection)
        self.ta_queue_dl.setSelectionBehavior(QAbstractItemView.SelectRows)
        self.ta_queue_dl.setSortingEnabled(True)
        self.ta_queue_dl.verticalHeader().setProperty("showSortIndicator", True)

        self.lv_queue_dl.addWidget(self.ta_queue_dl)

        self.pb_queue_item_remove = QPushButton(self.w_central)
        self.pb_queue_item_remove.setObjectName("pb_queue_item_remove")
        self.pb_queue_item_remove.setEnabled(False)

        self.lv_queue_dl.addWidget(self.pb_queue_item_remove)

        self.lv_info.addLayout(self.lv_queue_dl)

        self.horizontalLayout.addLayout(self.lv_info)

        self.horizontalLayout.setStretch(1, 50)
        self.horizontalLayout.setStretch(2, 25)
        MainWindow.setCentralWidget(self.w_central)
        self.menubar = QMenuBar(MainWindow)
        self.menubar.setObjectName("menubar")
        self.menubar.setGeometry(QRect(0, 0, 1200, 24))
        # if QT_CONFIG(tooltip)
        self.menubar.setToolTip("")
        # endif // QT_CONFIG(tooltip)
        # if QT_CONFIG(statustip)
        self.menubar.setStatusTip("")
        # endif // QT_CONFIG(statustip)
        # if QT_CONFIG(whatsthis)
        self.menubar.setWhatsThis("")
        # endif // QT_CONFIG(whatsthis)
        # if QT_CONFIG(accessibility)
        self.menubar.setAccessibleName("")
        # endif // QT_CONFIG(accessibility)
        # if QT_CONFIG(accessibility)
        self.menubar.setAccessibleDescription("")
        # endif // QT_CONFIG(accessibility)
        self.m_file = QMenu(self.menubar)
        self.m_file.setObjectName("m_file")
        # if QT_CONFIG(tooltip)
        self.m_file.setToolTip("")
        # endif // QT_CONFIG(tooltip)
        # if QT_CONFIG(statustip)
        self.m_file.setStatusTip("")
        # endif // QT_CONFIG(statustip)
        # if QT_CONFIG(whatsthis)
        self.m_file.setWhatsThis("")
        # endif // QT_CONFIG(whatsthis)
        # if QT_CONFIG(accessibility)
        self.m_file.setAccessibleName("")
        # endif // QT_CONFIG(accessibility)
        # if QT_CONFIG(accessibility)
        self.m_file.setAccessibleDescription("")
        # endif // QT_CONFIG(accessibility)
        self.m_help = QMenu(self.menubar)
        self.m_help.setObjectName("m_help")
        MainWindow.setMenuBar(self.menubar)
        self.statusbar = QStatusBar(MainWindow)
        self.statusbar.setObjectName("statusbar")
        # if QT_CONFIG(tooltip)
        self.statusbar.setToolTip("")
        # endif // QT_CONFIG(tooltip)
        # if QT_CONFIG(statustip)
        self.statusbar.setStatusTip("")
        # endif // QT_CONFIG(statustip)
        # if QT_CONFIG(whatsthis)
        self.statusbar.setWhatsThis("")
        # endif // QT_CONFIG(whatsthis)
        # if QT_CONFIG(accessibility)
        self.statusbar.setAccessibleName("")
        # endif // QT_CONFIG(accessibility)
        # if QT_CONFIG(accessibility)
        self.statusbar.setAccessibleDescription("")
        # endif // QT_CONFIG(accessibility)
        self.statusbar.setLayoutDirection(Qt.LeftToRight)
        MainWindow.setStatusBar(self.statusbar)

        self.menubar.addAction(self.m_file.menuAction())
        self.menubar.addAction(self.m_help.menuAction())
        self.m_file.addAction(self.a_preferences)
        self.m_file.addAction(self.a_logout)
        self.m_file.addAction(self.a_exit)
        self.m_help.addAction(self.a_version)
        self.m_help.addAction(self.a_updates_check)

        self.retranslateUi(MainWindow)

        QMetaObject.connectSlotsByName(MainWindow)

    # setupUi

    def retranslateUi(self, MainWindow):
        MainWindow.setWindowTitle(QCoreApplication.translate("MainWindow", "MainWindow", None))
        self.a_version.setText(QCoreApplication.translate("MainWindow", "Version", None))
        self.a_exit.setText(QCoreApplication.translate("MainWindow", "Exit", None))
        self.a_logout.setText(QCoreApplication.translate("MainWindow", "Logout", None))
        self.a_updates_check.setText(QCoreApplication.translate("MainWindow", "Check for Updates", None))
        ___qtreewidgetitem = self.tr_lists_user.headerItem()
        ___qtreewidgetitem.setText(1, QCoreApplication.translate("MainWindow", "obj", None))

        __sortingEnabled = self.tr_lists_user.isSortingEnabled()
        self.tr_lists_user.setSortingEnabled(False)
        ___qtreewidgetitem1 = self.tr_lists_user.topLevelItem(0)
        ___qtreewidgetitem1.setText(0, QCoreApplication.translate("MainWindow", "Playlists", None))
        ___qtreewidgetitem2 = self.tr_lists_user.topLevelItem(1)
        ___qtreewidgetitem2.setText(0, QCoreApplication.translate("MainWindow", "Mixes", None))
        ___qtreewidgetitem3 = self.tr_lists_user.topLevelItem(2)
        ___qtreewidgetitem3.setText(0, QCoreApplication.translate("MainWindow", "Favorites", None))
        self.tr_lists_user.setSortingEnabled(__sortingEnabled)

        self.pb_reload_user_lists.setText(QCoreApplication.translate("MainWindow", "Reload", None))
        self.pb_download_list.setText(QCoreApplication.translate("MainWindow", "Download List", None))
        ___qtreewidgetitem4 = self.tr_results.headerItem()
        ___qtreewidgetitem4.setText(6, QCoreApplication.translate("MainWindow", "Quality", None))
        ___qtreewidgetitem4.setText(5, QCoreApplication.translate("MainWindow", "Duration", None))
        ___qtreewidgetitem4.setText(4, QCoreApplication.translate("MainWindow", "Album", None))
        ___qtreewidgetitem4.setText(3, QCoreApplication.translate("MainWindow", "Title", None))
        ___qtreewidgetitem4.setText(2, QCoreApplication.translate("MainWindow", "Artist", None))
        ___qtreewidgetitem4.setText(1, QCoreApplication.translate("MainWindow", "obj", None))
        ___qtreewidgetitem4.setText(0, QCoreApplication.translate("MainWindow", "#", None))
        self.te_debug.setPlaceholderText(QCoreApplication.translate("MainWindow", "Logs...", None))
        self.l_pm_cover.setText("")
        self.l_h_queue_dl.setText(QCoreApplication.translate("MainWindow", "Download Queue", None))
        ___qtablewidgetitem = self.ta_queue_dl.horizontalHeaderItem(0)
        ___qtablewidgetitem.setText(QCoreApplication.translate("MainWindow", "#", None))
        ___qtablewidgetitem1 = self.ta_queue_dl.horizontalHeaderItem(1)
        ___qtablewidgetitem1.setText(QCoreApplication.translate("MainWindow", "obj", None))
        ___qtablewidgetitem2 = self.ta_queue_dl.horizontalHeaderItem(2)
        ___qtablewidgetitem2.setText(QCoreApplication.translate("MainWindow", "Name", None))
        ___qtablewidgetitem3 = self.ta_queue_dl.horizontalHeaderItem(3)
        ___qtablewidgetitem3.setText(QCoreApplication.translate("MainWindow", "Type", None))
        ___qtablewidgetitem4 = self.ta_queue_dl.horizontalHeaderItem(4)
        ___qtablewidgetitem4.setText(QCoreApplication.translate("MainWindow", "Quality", None))
        self.pb_queue_item_remove.setText(QCoreApplication.translate("MainWindow", "Remove", None))
        self.m_file.setTitle(QCoreApplication.translate("MainWindow", "File", None))
        self.m_help.setTitle(QCoreApplication.translate("MainWindow", "Help", None))

    # retranslateUi
