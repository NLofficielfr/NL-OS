#!/usr/bin/env python3
import os
import sys
import math
import time
import subprocess
from PyQt5.QtCore import Qt, QTimer, QPoint, QRectF, QEasingCurve, QPropertyAnimation
from PyQt5.QtGui import QColor, QPainter, QFont, QLinearGradient, QRadialGradient, QBrush, QPen
from PyQt5.QtWidgets import (
    QApplication, QWidget, QLabel, QPushButton, QFrame,
    QVBoxLayout, QHBoxLayout, QGridLayout, QSizePolicy
)

HOME = os.path.expanduser("~")

def run(cmd):
    try:
        subprocess.Popen(cmd, shell=True)
    except Exception as e:
        print(e)

class GlassCard(QFrame):
    def __init__(self, radius=28, opacity=0.68, parent=None):
        super().__init__(parent)
        self.radius = radius
        self.opacity = opacity
        self.setAttribute(Qt.WA_TranslucentBackground)
        self.setStyleSheet("background: transparent;")

    def paintEvent(self, event):
        painter = QPainter(self)
        painter.setRenderHint(QPainter.Antialiasing)

        rect = self.rect().adjusted(1, 1, -1, -1)

        color = QColor(255, 255, 255)
        color.setAlphaF(self.opacity)

        border = QColor(180, 215, 228)
        border.setAlphaF(0.65)

        painter.setBrush(QBrush(color))
        painter.setPen(QPen(border, 1.0))
        painter.drawRoundedRect(rect, self.radius, self.radius)

        highlight = QColor(255, 255, 255)
        highlight.setAlphaF(0.55)
        painter.setPen(QPen(highlight, 1))
        painter.drawRoundedRect(rect.adjusted(3, 3, -3, -3), self.radius - 4, self.radius - 4)

class NLButton(QPushButton):
    def __init__(self, text, command=None, parent=None):
        super().__init__(text, parent)
        self.command = command
        self.setCursor(Qt.PointingHandCursor)
        self.setMinimumHeight(48)
        self.setStyleSheet("""
        QPushButton {
            background: rgba(255,255,255,210);
            color: #14202A;
            border: 1px solid rgba(180,215,228,170);
            border-radius: 18px;
            font-size: 14px;
            font-weight: 600;
            padding: 10px 16px;
        }
        QPushButton:hover {
            background: rgba(245,252,255,240);
            border: 1px solid rgba(130,200,230,220);
        }
        QPushButton:pressed {
            background: rgba(220,240,248,240);
        }
        """)
        if command:
            self.clicked.connect(lambda: run(command))

class DockIcon(QPushButton):
    def __init__(self, icon, label, command=None, parent=None):
        super().__init__(icon, parent)
        self.label = label
        self.command = command
        self.setCursor(Qt.PointingHandCursor)
        self.setFixedSize(58, 58)
        self.setStyleSheet("""
        QPushButton {
            background: qlineargradient(x1:0,y1:0,x2:1,y2:1,
                stop:0 rgba(255,255,255,245),
                stop:1 rgba(205,235,245,230));
            color: #14202A;
            border: 1px solid rgba(180,215,228,180);
            border-radius: 18px;
            font-size: 23px;
            font-weight: 800;
        }
        QPushButton:hover {
            background: qlineargradient(x1:0,y1:0,x2:1,y2:1,
                stop:0 rgba(255,255,255,255),
                stop:1 rgba(180,228,245,245));
        }
        """)
        if command:
            self.clicked.connect(lambda: run(command))

class NLShell(QWidget):
    def __init__(self):
        super().__init__()
        self.setWindowTitle("NL Shell")
        self.setWindowFlags(Qt.FramelessWindowHint | Qt.Window)
        self.setAttribute(Qt.WA_TranslucentBackground, False)

        self.showFullScreen()

        self.clock = QLabel()
        self.clock.setAlignment(Qt.AlignRight | Qt.AlignVCenter)

        self.build_ui()

        timer = QTimer(self)
        timer.timeout.connect(self.update_clock)
        timer.start(1000)
        self.update_clock()

    def build_ui(self):
        root = QVBoxLayout(self)
        root.setContentsMargins(28, 24, 28, 26)
        root.setSpacing(22)

        topbar = GlassCard(radius=24, opacity=0.62)
        topbar.setFixedHeight(58)
        top_layout = QHBoxLayout(topbar)
        top_layout.setContentsMargins(22, 0, 22, 0)

        brand = QLabel("NL OS")
        brand.setStyleSheet("color:#121A22; font-size:22px; font-weight:800; letter-spacing:-1px;")

        status = QLabel("Lite Shell Alpha · Native Interface")
        status.setStyleSheet("color:#5D7280; font-size:13px; font-weight:500;")

        self.clock.setStyleSheet("color:#5D7280; font-size:13px; font-weight:600;")

        top_layout.addWidget(brand)
        top_layout.addSpacing(14)
        top_layout.addWidget(status)
        top_layout.addStretch()
        top_layout.addWidget(self.clock)

        root.addWidget(topbar)

        main = QHBoxLayout()
        main.setSpacing(22)

        left = self.identity_panel()
        center = self.hero_panel()
        right = self.control_panel()

        main.addWidget(left, 0)
        main.addWidget(center, 1)
        main.addWidget(right, 0)

        root.addLayout(main, 1)

        dock = self.dock_panel()
        dock_wrap = QHBoxLayout()
        dock_wrap.addStretch()
        dock_wrap.addWidget(dock)
        dock_wrap.addStretch()

        root.addLayout(dock_wrap)

    def identity_panel(self):
        card = GlassCard(radius=34, opacity=0.66)
        card.setFixedWidth(320)

        layout = QVBoxLayout(card)
        layout.setContentsMargins(28, 28, 28, 28)
        layout.setSpacing(14)

        hello = QLabel("Bonjour,")
        hello.setStyleSheet("color:#6A7D88; font-size:15px;")

        user = QLabel("NL User")
        user.setStyleSheet("color:#121A22; font-size:34px; font-weight:850; letter-spacing:-2px;")

        live = QLabel("Session Live · NL Shell actif")
        live.setStyleSheet("color:#5D7280; font-size:13px; font-weight:500;")

        pill = QLabel("● Mode clair premium")
        pill.setStyleSheet("""
        QLabel {
            color:#107252;
            background:rgba(255,255,255,170);
            border:1px solid rgba(180,215,228,150);
            border-radius:16px;
            padding:9px 12px;
            font-size:13px;
            font-weight:700;
        }
        """)

        layout.addWidget(hello)
        layout.addWidget(user)
        layout.addWidget(live)
        layout.addSpacing(8)
        layout.addWidget(pill)
        layout.addSpacing(18)

        title = QLabel("Applications")
        title.setStyleSheet("color:#121A22; font-size:19px; font-weight:800;")
        layout.addWidget(title)

        grid = QGridLayout()
        grid.setSpacing(12)

        apps = [
            ("Fichiers", "exo-open --launch FileManager"),
            ("Terminal", "xfce4-terminal"),
            ("Internet", "firefox-esr"),
            ("Réglages", "xfce4-settings-manager"),
            ("Infos", "xfce4-terminal -e nlos-info"),
            ("Gaming", "xfce4-terminal -e 'bash -lc \"sudo nlos-boost gaming; read\"'")
        ]

        for i, (name, cmd) in enumerate(apps):
            b = NLButton(name, cmd)
            grid.addWidget(b, i // 2, i % 2)

        layout.addLayout(grid)
        layout.addStretch()

        shutdown = NLButton("Quitter NL Shell", None)
        shutdown.clicked.connect(self.close)
        layout.addWidget(shutdown)

        return card

    def hero_panel(self):
        card = GlassCard(radius=42, opacity=0.72)

        layout = QVBoxLayout(card)
        layout.setContentsMargins(44, 38, 44, 38)
        layout.setSpacing(18)
        layout.setAlignment(Qt.AlignCenter)

        logo = QLabel("NL OS")
        logo.setAlignment(Qt.AlignCenter)
        logo.setStyleSheet("color:#121A22; font-size:92px; font-weight:900; letter-spacing:-8px;")

        tagline = QLabel("A light, clean and adaptive Linux experience.")
        tagline.setAlignment(Qt.AlignCenter)
        tagline.setStyleSheet("color:#607684; font-size:19px; font-weight:500;")

        search = QLabel("  Rechercher dans NL OS                                      ↵")
        search.setFixedHeight(58)
        search.setAlignment(Qt.AlignVCenter)
        search.setStyleSheet("""
        QLabel {
            background:rgba(242,250,253,210);
            color:#70848F;
            border:1px solid rgba(180,215,228,170);
            border-radius:29px;
            font-size:15px;
            font-weight:500;
        }
        """)

        actions = QHBoxLayout()
        actions.setSpacing(12)

        action_data = [
            ("Performance", "xfce4-terminal -e 'bash -lc \"sudo nlos-boost performance; read\"'"),
            ("Gaming", "xfce4-terminal -e 'bash -lc \"sudo nlos-boost gaming; read\"'"),
            ("Old Mac", "xfce4-terminal -e 'bash -lc \"sudo nlos-boost oldmac; read\"'"),
            ("Diagnostic", "xfce4-terminal -e nlos-info")
        ]

        for name, cmd in action_data:
            actions.addWidget(NLButton(name, cmd))

        note = QLabel("Linux reste le moteur. NL Shell devient l’expérience visible.")
        note.setAlignment(Qt.AlignCenter)
        note.setStyleSheet("color:#6D808A; font-size:12px;")

        layout.addStretch()
        layout.addWidget(logo)
        layout.addWidget(tagline)
        layout.addSpacing(16)
        layout.addWidget(search)
        layout.addSpacing(8)
        layout.addLayout(actions)
        layout.addStretch()
        layout.addWidget(note)

        return card

    def control_panel(self):
        card = GlassCard(radius=34, opacity=0.66)
        card.setFixedWidth(340)

        layout = QVBoxLayout(card)
        layout.setContentsMargins(28, 28, 28, 28)
        layout.setSpacing(16)

        title = QLabel("Centre de contrôle")
        title.setStyleSheet("color:#121A22; font-size:20px; font-weight:850;")
        layout.addWidget(title)

        grid = QGridLayout()
        grid.setSpacing(12)

        tiles = [
            ("Wi-Fi", "Actif"),
            ("Son", "72%"),
            ("Énergie", "Équilibré"),
            ("Système", "Live USB"),
            ("Gaming", "Disponible"),
            ("Old Mac", "Optimisable")
        ]

        for i, (a, b) in enumerate(tiles):
            tile = GlassCard(radius=22, opacity=0.78)
            tile.setFixedHeight(84)
            tl = QVBoxLayout(tile)
            tl.setContentsMargins(14, 12, 14, 12)
            name = QLabel(a)
            name.setStyleSheet("color:#121A22; font-size:13px; font-weight:800;")
            val = QLabel(b)
            val.setStyleSheet("color:#687C87; font-size:12px; font-weight:500;")
            tl.addWidget(name)
            tl.addWidget(val)
            tl.addStretch()
            grid.addWidget(tile, i // 2, i % 2)

        layout.addLayout(grid)

        layout.addSpacing(12)

        bright = QLabel("Luminosité")
        bright.setStyleSheet("color:#121A22; font-size:13px; font-weight:700;")
        layout.addWidget(bright)

        bar = QFrame()
        bar.setFixedHeight(8)
        bar.setStyleSheet("""
        QFrame {
            background:qlineargradient(x1:0,y1:0,x2:1,y2:0,
                stop:0 #92D8EF,
                stop:0.72 #D8C28A,
                stop:0.73 rgba(190,215,228,120),
                stop:1 rgba(190,215,228,120));
            border-radius:4px;
        }
        """)
        layout.addWidget(bar)

        layout.addStretch()

        layout.addWidget(NLButton("Ouvrir terminal", "xfce4-terminal"))
        layout.addWidget(NLButton("Relancer bureau", "xfce4-panel --restart"))

        return card

    def dock_panel(self):
        dock = GlassCard(radius=36, opacity=0.70)
        dock.setFixedSize(560, 82)

        layout = QHBoxLayout(dock)
        layout.setContentsMargins(18, 12, 18, 12)
        layout.setSpacing(14)

        icons = [
            ("N", "NL Shell", "python3 /opt/nl-os/nl-shell/nl-shell.py"),
            ("⌂", "Fichiers", "exo-open --launch FileManager"),
            (">", "Terminal", "xfce4-terminal"),
            ("◎", "Web", "firefox-esr"),
            ("⚙", "Réglages", "xfce4-settings-manager"),
            ("↯", "Gaming", "xfce4-terminal -e 'bash -lc \"sudo nlos-boost gaming; read\"'")
        ]

        for icon, label, cmd in icons:
            layout.addWidget(DockIcon(icon, label, cmd))

        return dock

    def paintEvent(self, event):
        painter = QPainter(self)
        painter.setRenderHint(QPainter.Antialiasing)

        rect = self.rect()

        base = QLinearGradient(0, 0, rect.width(), rect.height())
        base.setColorAt(0.0, QColor("#EAF8FF"))
        base.setColorAt(0.45, QColor("#F8FCFF"))
        base.setColorAt(1.0, QColor("#E8F2F6"))
        painter.fillRect(rect, base)

        radial1 = QRadialGradient(rect.width() * 0.20, rect.height() * 0.18, rect.width() * 0.55)
        radial1.setColorAt(0.0, QColor(140, 220, 245, 150))
        radial1.setColorAt(1.0, QColor(140, 220, 245, 0))
        painter.fillRect(rect, QBrush(radial1))

        radial2 = QRadialGradient(rect.width() * 0.82, rect.height() * 0.68, rect.width() * 0.50)
        radial2.setColorAt(0.0, QColor(230, 205, 150, 120))
        radial2.setColorAt(1.0, QColor(230, 205, 150, 0))
        painter.fillRect(rect, QBrush(radial2))

        pen1 = QPen(QColor(255, 255, 255, 120), 10)
        painter.setPen(pen1)
        painter.drawArc(QRectF(-100, rect.height()*0.52, rect.width()+200, 260), 0, 180 * 16)

        pen2 = QPen(QColor(130, 210, 235, 90), 7)
        painter.setPen(pen2)
        painter.drawArc(QRectF(-80, rect.height()*0.55, rect.width()+160, 300), 0, 180 * 16)

    def update_clock(self):
        self.clock.setText(time.strftime("%a %d %b  %H:%M"))

def main():
    app = QApplication(sys.argv)
    app.setApplicationName("NL Shell")
    app.setFont(QFont("Sans", 10))

    shell = NLShell()
    shell.show()

    sys.exit(app.exec_())

if __name__ == "__main__":
    main()
