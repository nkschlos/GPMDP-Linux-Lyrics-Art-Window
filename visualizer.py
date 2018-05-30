import json
import sys, os
import urllib3
import time
from PyQt5.QtWidgets import *
from PyQt5 import  QtCore, QtGui


#choose initial location for windows (top left corner), from left right and from top down
#(play around with these until it starts in a place you like it)
lyric_x = 0
lyric_y = 0
art_x = lyric_x+565
art_y = 0


#get home directory
home = os.path.expanduser("~")

#initialize data
data = ''
#allos urllib3 to access https without error
urllib3.disable_warnings(urllib3.exceptions.InsecureRequestWarning)

#initialize vars
lyrics = song = title = artist = album_art = ''

#stall until data is collected (in case song not selected)
while not ((lyrics) and (song) and (title) and (artist) and (album_art)):
    time.sleep(1)
    #get data from json
    try:
        with open('{}/.config/Google Play Music Desktop Player/json_store/playback.json'.format(home)) as f:
            data = json.load(f)
    except:
        print('error')
    lyrics = data.get("songLyrics")
    song = data.get('song')
    title = song.get('title')
    artist = song.get('artist')
    album_art = song.get('albumArt')


#generate text for lyrics box
text = title + ' by ' + artist + '\n\n\n' + lyrics

#download art
http = urllib3.PoolManager()
r = http.request('GET', album_art)
r = r.data

#create lyric box widget
class Lyrics(QWidget):
    resized=QtCore.pyqtSignal()
    def __init__(self):
        super().__init__()

        self.initUI()

    def initUI(self):
        self.lbl = QLabel(self)
        self.setWindowTitle('Lyrics')
        self.show()
        self.lbl.setText(text)
        self.lbl.setAlignment(QtCore.Qt.AlignCenter)
        #set default size
        self.resize(QtCore.QSize(390,990))
        self.lbl.adjustSize()
        self.setStyleSheet("background-color: #333333; color: #999999")

        self.scrl = QScrollArea()
        #start continuous updating ever 500 ms
        self.update = QtCore.QTimer(self)
        self.update.setSingleShot(False)
        #create refresher
        self.update.timeout.connect(self.refresh)
        #set refresh time to 500ms
        self.update.start(500)
        #self.resized.connect(self.realign)

        #make scrollbar
        widget = QWidget()
        layout = QVBoxLayout(self)
        layout.addWidget(self.lbl)
        layout.setAlignment(QtCore.Qt.AlignHCenter)
        widget.setLayout(layout)
        # Scroll Area Properties
        scroll = QScrollArea()
        scroll.setAlignment(QtCore.Qt.AlignCenter)
        scroll.setVerticalScrollBarPolicy(QtCore.Qt.ScrollBarAlwaysOn)
        scroll.setHorizontalScrollBarPolicy(QtCore.Qt.ScrollBarAlwaysOff)
        scroll.setStyleSheet('''
        QScrollBar:vertical
        {
            border-color: #272727;
            border-width: 1px;
            border-style: solid;
        }
        QScrollBar::handle:vertical
        {
            background-color: #3a3a3a;
        } 
        QScrollBar::up-arrow:vertical
        {
            image: url(Resources/ComboBox_Right1.png);
        }
        QScrollBar::down-arrow:vertical
        {
            image: url(Resources/ComboBox_Right1.png);
        }
        QScrollBar::sub-line:vertical{
            border: 1px;
            border-color: #ffffff
        }
        QScrollBar::add-line:vertical{
            border:1px;
            border-color: #ffffff
        }
        ''')
        scroll.setWidget(widget)

        # Scroll Area Layer add
        vLayout = QVBoxLayout(self)
        vLayout.addWidget(scroll)
        self.setLayout(vLayout)
        #set initial position
        self.move(lyric_x,lyric_y)
        self.setWindowIcon(QtGui.QIcon(os.path.dirname(os.path.realpath(__file__)) + os.path.sep + 'icon.png'))

    def refresh(self):
        try:
            with open('{}/.config/Google Play Music Desktop Player/json_store/playback.json'.format(home)) as f:
                data = json.load(f)
            #get metadeta
            lyrics = data.get("songLyrics")
            song = data.get('song')
            title = song.get('title')
            artist = song.get('artist')
            if (lyrics):
                text = title + '\nby ' + artist + '\n\n\n' + lyrics


                self.lbl.setText(text)
                self.lbl.setAlignment(QtCore.Qt.AlignCenter)
                self.lbl.adjustSize()
                #self.adjustSize()
            else:
                time.sleep(1)
                self.refresh
        except:
            time.sleep(1)
            self.refresh


# create album art widget
class Art(QWidget):

    def __init__(self):
        super().__init__()

        self.initUI()

    def initUI(self):
        self.lbl = QLabel(self)
        self.setWindowTitle('Album Art')
        self.lbl.setPixmap(pixmap)
        self.show()
        self.lbl.adjustSize()
        self.adjustSize()
        self.setStyleSheet("background-color: #333333; color: #999999")
        self.update2 = QtCore.QTimer(self)
        self.update2.setSingleShot(False)
        #create refresher
        self.update2.timeout.connect(self.refresh)
        #set refresh time to 500ms
        self.update2.start(500)
        #set initial position
        self.move(art_x,art_y)
        self.setWindowIcon(QtGui.QIcon(os.path.dirname(os.path.realpath(__file__)) + os.path.sep + 'icon.png'))
    def refresh(self):
        data=''
        try:
            with open('{}/.config/Google Play Music Desktop Player/json_store/playback.json'.format(home)) as f:
                data = json.load(f)

            song = data.get('song')
            album_art = song.get('albumArt')
            if (album_art):
                http = urllib3.PoolManager()
                r = http.request('GET', album_art)
                r = r.data
                pixmap = QtGui.QPixmap()
                pixmap.loadFromData(r)
                self.lbl.setPixmap(pixmap)
                #self.lbl.setAlignment(QtCore.Qt.AlignCenter)
                self.lbl.adjustSize()
            else:
                time.sleep(1)
                self.refresh
                print('wait')
        except:
            time.sleep(1)
            self.refresh

if __name__ == '__main__':
    #start application
    app = QApplication(sys.argv)

    pixmap = QtGui.QPixmap()
    pixmap.loadFromData(r)
    #start lyric and art widgets
    lyrics = Lyrics()
    art = Art()
    #close when exited
    sys.exit(app.exec_())
