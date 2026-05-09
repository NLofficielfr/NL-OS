import QtQuick 2.15
import QtQuick.Controls 2.15
import QtQuick.Layouts 1.15
import SddmComponents 2.0

Rectangle {
    id: root
    width: 1920
    height: 1080
    color: "black"

    property string passwordText: ""

    Image {
        id: bg
        anchors.fill: parent
        source: "background.png"
        fillMode: Image.PreserveAspectCrop
        opacity: 0.0

        Behavior on opacity {
            NumberAnimation { duration: 1200; easing.type: Easing.OutCubic }
        }
    }

    Rectangle {
        anchors.fill: parent
        color: "black"
        opacity: 0.25
    }

    Image {
        id: logo
        source: "logo.png"
        width: 180
        height: 180
        fillMode: Image.PreserveAspectFit
        anchors.horizontalCenter: parent.horizontalCenter
        anchors.top: parent.top
        anchors.topMargin: 70
        opacity: 0.0

        Behavior on opacity {
            NumberAnimation { duration: 900; easing.type: Easing.OutCubic }
        }
    }

    Column {
        id: timeBlock
        spacing: 6
        anchors.horizontalCenter: parent.horizontalCenter
        anchors.top: parent.top
        anchors.topMargin: 285
        opacity: 0.0
        y: 300

        Behavior on opacity {
            NumberAnimation { duration: 1100; easing.type: Easing.OutCubic }
        }

        Behavior on y {
            NumberAnimation { duration: 1100; easing.type: Easing.OutCubic }
        }

        Text {
            id: clock
            text: Qt.formatTime(new Date(), "hh:mm")
            color: "white"
            font.pixelSize: 92
            font.weight: Font.DemiBold
            horizontalAlignment: Text.AlignHCenter
            anchors.horizontalCenter: parent.horizontalCenter
        }

        Text {
            id: dateText
            text: Qt.formatDate(new Date(), "dddd d MMMM")
            color: Qt.rgba(1,1,1,0.72)
            font.pixelSize: 22
            font.weight: Font.Medium
            horizontalAlignment: Text.AlignHCenter
            anchors.horizontalCenter: parent.horizontalCenter
        }
    }

    Timer {
        interval: 1000
        running: true
        repeat: true
        onTriggered: {
            clock.text = Qt.formatTime(new Date(), "hh:mm")
            dateText.text = Qt.formatDate(new Date(), "dddd d MMMM")
        }
    }

    Rectangle {
        id: loginCard
        width: 420
        height: 170
        radius: 38
        color: Qt.rgba(1,1,1,0.18)
        border.color: Qt.rgba(1,1,1,0.30)
        border.width: 1
        anchors.horizontalCenter: parent.horizontalCenter
        anchors.bottom: parent.bottom
        anchors.bottomMargin: 70
        opacity: 0.0

        Behavior on opacity {
            NumberAnimation { duration: 1300; easing.type: Easing.OutCubic }
        }

        Column {
            anchors.fill: parent
            anchors.margins: 22
            spacing: 14

            Text {
                text: "Session"
                color: Qt.rgba(1,1,1,0.62)
                font.pixelSize: 13
                font.weight: Font.Medium
            }

            Text {
                text: userModel.lastUser.length > 0 ? userModel.lastUser : "NL User"
                color: "white"
                font.pixelSize: 24
                font.weight: Font.DemiBold
            }

            TextField {
                id: passwordBox
                width: parent.width
                height: 48
                placeholderText: "Mot de passe"
                echoMode: TextInput.Password
                color: "white"
                placeholderTextColor: Qt.rgba(1,1,1,0.55)
                font.pixelSize: 16
                background: Rectangle {
                    radius: 24
                    color: Qt.rgba(1,1,1,0.18)
                    border.color: Qt.rgba(1,1,1,0.28)
                    border.width: 1
                }

                Keys.onReturnPressed: {
                    sddm.login(userModel.lastUser, passwordBox.text, sessionModel.lastIndex)
                }
            }
        }
    }

    Timer {
        interval: 250
        running: true
        repeat: false
        onTriggered: {
            bg.opacity = 1.0
            logo.opacity = 1.0
            timeBlock.opacity = 1.0
            timeBlock.y = 285
            loginCard.opacity = 1.0
        }
    }

    Component.onCompleted: {
        passwordBox.forceActiveFocus()
    }
}
