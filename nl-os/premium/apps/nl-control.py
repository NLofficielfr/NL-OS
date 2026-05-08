#!/usr/bin/env python3
import sys
import subprocess
import time
from PyQt5.QtCore import Qt, QTimer, QRectF
from PyQt5.QtGui import QColor, QPainter, QFont, QLinearGradient, QRadialGradient, QBrush, QPen
from PyQt5.QtWidgets import QApplication, QWidget, QLabel, QPushButton, QVBoxLayout, QHBoxLayout, QGridLayout, QFrame

def run(cmd):
    subprocess.Popen(cmd, shell=True)

class Glass(QFrame):
    def __init__(self, radius=32, alpha=0.72):
        super().__init__()
        self.radius = radius
        self.alpha = alpha
        self.setAttribute(Qt.WA_TranslucentBackground)

    def paintEvent(self, event):
        p = QPainter(self)
        p.setRenderHint(QPainter.Antialiasing)

        rect = self.rect().adjusted(1, 1, -1, -1)

        bg = QColor(255, 255, 255)
        bg.setAlphaF(self.alpha)

        border = QColor(178, 214, 228)
        border.setAlphaF(0.72)

        p.setBrush(QBrush(bg))
        p.setPen(QPen(border, 1.2))
        p.drawRoundedRect(rect, self.radius, self.radius)

        shine = QColor(255, 255, 255)
        shine.setAlphaF(0.58)
        p.setPen(QPen(shine, 1))
        p.drawRoundedRect(rect.adjusted(4, 4, -4, -4), self.radius - 5, self.radius - 5)

class NLButton(QPushButton):
    def __init__(self, text, cmd=None):
        super().__init__(text)
        self.cmd = cmd
        self.setCursor(Qt.PointingHandCursor)
        self.setMinimumHeight(54)
        self.setStyleSheet("""
        QPushButton {
            background: rgba(255,255,255,232);
            color: #111922;
            border: 1px solid rgba(170,210,225,200);
            border-radius: 24px;
            padding: 10px 16px;
            font-size: 14px;
            font-weight: 700;
        }
        QPushButton:hover {
            background: rgba(236,250,255,250);
            border: 1px solid rgba(95,195,230,230);
        }
        QPushButton:pressed {
            background: rgba(210,236,246,250);
        }
        """)
        if cmd:
            self.clicked.connect(lambda: run(cmd))

class NLControl(QWidget):
    def __init__(self):
        super().__init__()
        self.setWindowTitle("NL Control")
        self.resize(1080, 700)
        self.setMinimumSize(920, 620)
        self.clock = QLabel()
        self.build()

        timer = QTimer(self)
        timer.timeout.connect(self.tick)
        timer.start(1000)
        self.tick()

    def build(self):
        root = QVBoxLayout(self)
        root.setContentsMargins(30, 26, 30, 26)
        root.setSpacing(22)

        top = Glass(radius=30, alpha=0.74)
        top.setFixedHeight(76)
        top_l = QHBoxLayout(top)
        top_l.setContentsMargins(26, 0, 26, 0)

        logo = QLabel("NL")
        logo.setStyleSheet("font-size: 32px; font-weight: 950; color: #111922; letter-spacing: -3px;")

        title = QLabel("Control")
        title.setStyleSheet("font-size: 23px; font-weight: 850; color: #111922;")

        sub = QLabel("Premium Alpha · système simple")
        sub.setStyleSheet("font-size: 13px; font-weight: 600; color: #637783;")

        self.clock.setStyleSheet("font-size: 13px; font-weight: 700; color: #637783;")

        top_l.addWidget(logo)
        top_l.addSpacing(8)
        top_l.addWidget(title)
        top_l.addSpacing(16)
        top_l.addWidget(sub)
        top_l.addStretch()
        top_l.addWidget(self.clock)

        root.addWidget(top)

        main = QHBoxLayout()
        main.setSpacing(22)

        left = Glass(radius=38, alpha=0.76)
        left.setFixedWidth(330)
        left_l = QVBoxLayout(left)
        left_l.setContentsMargins(28, 28, 28, 28)
        left_l.setSpacing(14)

        hello = QLabel("Bonjour,")
        hello.setStyleSheet("font-size: 15px; color: #6A7D88;")

        user = QLabel("NL User")
        user.setStyleSheet("font-size: 35px; font-weight: 950; color: #111922; letter-spacing: -2px;")

        pill = QLabel("● NL OS Premium actif")
        pill.setStyleSheet("""
        QLabel {
            background: rgba(255,255,255,195);
            color: #0F7252;
            border: 1px solid rgba(170,210,225,180);
            border-radius: 20px;
            padding: 10px 14px;
            font-size: 13px;
            font-weight: 850;
        }
        """)

        left_l.addWidget(hello)
        left_l.addWidget(user)
        left_l.addWidget(pill)
        left_l.addSpacing(20)

        modes = QLabel("Modes rapides")
        modes.setStyleSheet("font-size: 20px; font-weight: 900; color: #111922;")
        left_l.addWidget(modes)

        left_l.addWidget(NLButton("Performance", "konsole -e bash -lc 'sudo nl-boost performance; read'"))
        left_l.addWidget(NLButton("Gaming", "konsole -e bash -lc 'sudo nl-boost gaming; read'"))
        left_l.addWidget(NLButton("Vieille machine", "konsole -e bash -lc 'sudo nl-boost old-machine; read'"))
        left_l.addWidget(NLButton("Économie", "konsole -e bash -lc 'sudo nl-boost battery; read'"))
        left_l.addStretch()

        center = Glass(radius=46, alpha=0.80)
        center_l = QVBoxLayout(center)
        center_l.setContentsMargins(38, 38, 38, 38)
        center_l.setSpacing(18)

        big = QLabel("NL OS")
        big.setAlignment(Qt.AlignCenter)
        big.setStyleSheet("font-size: 84px; font-weight: 950; color: #111922; letter-spacing: -8px;")

        tag = QLabel("Simple, premium, rond, rapide.")
        tag.setAlignment(Qt.AlignCenter)
        tag.setStyleSheet("font-size: 19px; font-weight: 600; color: #637783;")

        center_l.addStretch()
        center_l.addWidget(big)
        center_l.addWidget(tag)
        center_l.addSpacing(24)

        grid = QGridLayout()
        grid.setSpacing(14)

        apps = [
            ("Fichiers", "dolphin"),
            ("Terminal", "konsole"),
            ("Internet", "firefox"),
            ("Réglages", "systemsettings"),
            ("Infos système", "konsole -e nl-info"),
            ("Nettoyage", "konsole -e bash -lc 'sudo apt clean; journalctl --vacuum-time=2d; read'"),
            ("Gaming run", "konsole -e bash -lc 'echo nl-game-run commande_du_jeu; read'"),
            ("Mise à jour", "konsole -e bash -lc 'sudo apt update; read'")
        ]

        for i, (name, cmd) in enumerate(apps):
            grid.addWidget(NLButton(name, cmd), i // 2, i % 2)

        center_l.addLayout(grid)
        center_l.addStretch()

        right = Glass(radius=38, alpha=0.76)
        right.setFixedWidth(310)
        right_l = QVBoxLayout(right)
        right_l.setContentsMargins(28, 28, 28, 28)
        right_l.setSpacing(14)

        sys = QLabel("Système")
        sys.setStyleSheet("font-size: 21px; font-weight: 950; color: #111922;")
        right_l.addWidget(sys)

        tiles = [
            ("Base", "Linux Debian"),
            ("Édition", "Premium"),
            ("Interface", "KDE Plasma"),
            ("Design", "Round Glass"),
            ("Gaming", "Optimisable"),
            ("Mode", "Live USB")
        ]

        for a, b in tiles:
            tile = Glass(radius=24, alpha=0.84)
            tile.setFixedHeight(72)
            tl = QVBoxLayout(tile)
            tl.setContentsMargins(16, 10, 16, 10)

            aa = QLabel(a)
            aa.setStyleSheet("font-size: 13px; font-weight: 900; color: #111922;")
            bb = QLabel(b)
            bb.setStyleSheet("font-size: 12px; font-weight: 650; color: #637783;")

            tl.addWidget(aa)
            tl.addWidget(bb)

            right_l.addWidget(tile)

        right_l.addStretch()

        main.addWidget(left)
        main.addWidget(center, 1)
        main.addWidget(right)

        root.addLayout(main, 1)

    def paintEvent(self, event):
        p = QPainter(self)
        p.setRenderHint(QPainter.Antialiasing)

        r = self.rect()

        bg = QLinearGradient(0, 0, r.width(), r.height())
        bg.setColorAt(0.0, QColor("#EAF8FF"))
        bg.setColorAt(0.45, QColor("#FBFDFF"))
        bg.setColorAt(1.0, QColor("#E8F1F6"))
        p.fillRect(r, bg)

        blue = QRadialGradient(r.width() * 0.20, r.height() * 0.18, r.width() * 0.65)
        blue.setColorAt(0.0, QColor(130, 220, 245, 145))
        blue.setColorAt(1.0, QColor(130, 220, 245, 0))
        p.fillRect(r, QBrush(blue))

        gold = QRadialGradient(r.width() * 0.84, r.height() * 0.74, r.width() * 0.55)
        gold.setColorAt(0.0, QColor(222, 194, 136, 105))
        gold.setColorAt(1.0, QColor(222, 194, 136, 0))
        p.fillRect(r, QBrush(gold))

        p.setPen(QPen(QColor(255, 255, 255, 130), 12))
        p.drawArc(QRectF(-120, r.height() * 0.53, r.width() + 240, 300), 0, 180 * 16)

        p.setPen(QPen(QColor(120, 210, 238, 90), 8))
        p.drawArc(QRectF(-90, r.height() * 0.59, r.width() + 180, 330), 0, 180 * 16)

    def tick(self):
        self.clock.setText(time.strftime("%a %d %b  %H:%M"))

app = QApplication(sys.argv)
app.setApplicationName("NL Control")
app.setFont(QFont("Sans", 10))

w = NLControl()
w.show()

sys.exit(app.exec_())
