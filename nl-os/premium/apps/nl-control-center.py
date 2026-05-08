#!/usr/bin/env python3
import sys
import subprocess
from PyQt5.QtCore import Qt, QRectF
from PyQt5.QtGui import QColor, QPainter, QFont, QBrush, QPen
from PyQt5.QtWidgets import QApplication, QWidget, QLabel, QPushButton, QVBoxLayout, QHBoxLayout, QGridLayout, QFrame, QSlider

def run(cmd):
    subprocess.Popen(cmd, shell=True)

class GlassCard(QFrame):
    def __init__(self, radius=34, alpha=0.34):
        super().__init__()
        self.radius = radius
        self.alpha = alpha
        self.setAttribute(Qt.WA_TranslucentBackground)

    def paintEvent(self, event):
        p = QPainter(self)
        p.setRenderHint(QPainter.Antialiasing)
        r = self.rect().adjusted(1, 1, -1, -1)

        bg = QColor(255, 255, 255)
        bg.setAlphaF(self.alpha)

        border = QColor(255, 255, 255)
        border.setAlphaF(0.56)

        p.setBrush(QBrush(bg))
        p.setPen(QPen(border, 1.2))
        p.drawRoundedRect(r, self.radius, self.radius)

        inner = QColor(130, 210, 238)
        inner.setAlphaF(0.22)
        p.setPen(QPen(inner, 1))
        p.drawRoundedRect(r.adjusted(5, 5, -5, -5), self.radius - 7, self.radius - 7)

class Tile(QPushButton):
    def __init__(self, title, subtitle="", icon="•", cmd=None):
        super().__init__()
        self.cmd = cmd
        self.setCursor(Qt.PointingHandCursor)
        self.setMinimumHeight(82)
        self.setStyleSheet("""
        QPushButton {
            background: rgba(255,255,255,86);
            border: 1px solid rgba(255,255,255,125);
            border-radius: 28px;
            color: #101820;
            text-align: left;
            padding: 12px 16px;
            font-size: 14px;
            font-weight: 800;
        }
        QPushButton:hover {
            background: rgba(255,255,255,130);
            border: 1px solid rgba(135,210,235,150);
        }
        """)
        self.setText(f"{icon}   {title}\n     {subtitle}")
        if cmd:
            self.clicked.connect(lambda: run(cmd))

class NLControlCenter(QWidget):
    def __init__(self):
        super().__init__()
        self.setWindowTitle("NL Control Center")
        self.setWindowFlags(Qt.FramelessWindowHint | Qt.WindowStaysOnTopHint)
        self.setAttribute(Qt.WA_TranslucentBackground)
        self.resize(440, 680)
        self.build()

    def build(self):
        root = QVBoxLayout(self)
        root.setContentsMargins(0, 0, 0, 0)

        panel = GlassCard(radius=42, alpha=0.30)
        layout = QVBoxLayout(panel)
        layout.setContentsMargins(24, 22, 24, 22)
        layout.setSpacing(14)

        header = QHBoxLayout()
        title = QLabel("NL Control")
        title.setStyleSheet("font-size: 22px; font-weight: 900; color: #101820;")
        close = QPushButton("×")
        close.setFixedSize(36, 36)
        close.setCursor(Qt.PointingHandCursor)
        close.setStyleSheet("""
        QPushButton {
            background: rgba(255,255,255,90);
            border-radius: 18px;
            border: 1px solid rgba(255,255,255,120);
            font-size: 20px;
            font-weight: 900;
        }
        QPushButton:hover { background: rgba(255,255,255,150); }
        """)
        close.clicked.connect(self.close)
        header.addWidget(title)
        header.addStretch()
        header.addWidget(close)
        layout.addLayout(header)

        grid = QGridLayout()
        grid.setSpacing(12)

        tiles = [
            ("Wi-Fi", "NL Home", "◉", "nm-connection-editor"),
            ("Bluetooth", "Activé", "◇", "blueman-manager || true"),
            ("Focus", "Silence", "◌", ""),
            ("Performance", "Boost", "⚡", "konsole -e bash -lc 'sudo nl-boost performance; read'"),
            ("Gaming", "Mode jeu", "▣", "konsole -e bash -lc 'sudo nl-boost gaming; read'"),
            ("Réglages", "Système", "⚙", "systemsettings")
        ]

        for i, (a,b,c,d) in enumerate(tiles):
            grid.addWidget(Tile(a,b,c,d), i//2, i%2)

        layout.addLayout(grid)

        b1 = QLabel("Luminosité")
        b1.setStyleSheet("font-weight: 800; color: #101820; margin-top: 8px;")
        layout.addWidget(b1)

        brightness = QSlider(Qt.Horizontal)
        brightness.setValue(72)
        brightness.setStyleSheet("""
        QSlider::groove:horizontal {
            height: 8px;
            background: rgba(255,255,255,90);
            border-radius: 4px;
        }
        QSlider::handle:horizontal {
            background: rgba(255,255,255,220);
            border: 1px solid rgba(255,255,255,180);
            width: 22px;
            margin: -8px 0;
            border-radius: 11px;
        }
        """)
        layout.addWidget(brightness)

        b2 = QLabel("Son")
        b2.setStyleSheet("font-weight: 800; color: #101820; margin-top: 8px;")
        layout.addWidget(b2)

        sound = QSlider(Qt.Horizontal)
        sound.setValue(58)
        sound.setStyleSheet(brightness.styleSheet())
        layout.addWidget(sound)

        media = GlassCard(radius=30, alpha=0.24)
        media_l = QVBoxLayout(media)
        media_l.setContentsMargins(18, 16, 18, 16)

        song = QLabel("À l’arrêt")
        song.setStyleSheet("font-size: 18px; font-weight: 900; color: #101820;")
        artist = QLabel("NL Media")
        artist.setStyleSheet("font-size: 12px; font-weight: 600; color: rgba(16,24,32,150);")

        controls = QHBoxLayout()
        for x in ["◀", "▶", "▶▶"]:
            btn = QPushButton(x)
            btn.setFixedSize(46, 46)
            btn.setCursor(Qt.PointingHandCursor)
            btn.setStyleSheet("""
            QPushButton {
                background: rgba(255,255,255,70);
                border: 1px solid rgba(255,255,255,115);
                border-radius: 23px;
                font-size: 15px;
                font-weight: 900;
            }
            QPushButton:hover { background: rgba(255,255,255,135); }
            """)
            controls.addWidget(btn)
        controls.addStretch()

        media_l.addWidget(song)
        media_l.addWidget(artist)
        media_l.addSpacing(8)
        media_l.addLayout(controls)

        layout.addWidget(media)
        layout.addStretch()

        root.addWidget(panel)

    def paintEvent(self, event):
        pass

app = QApplication(sys.argv)
app.setFont(QFont("Sans", 10))
w = NLControlCenter()
w.show()
sys.exit(app.exec_())
