

/*
This is a UI file (.ui.qml) that is intended to be edited in Qt Design Studio only.
It is supposed to be strictly declarative and only uses a subset of QML. If you edit
this file manually, you might introduce QML code that is not supported by Qt Design Studio.
Check out https://doc.qt.io/qtcreator/creator-quick-ui-forms.html for details on .ui.qml files.
*/
import QtQuick 6.2
import QtQuick.Controls 6.2
import UI

Rectangle {
    id: rectangle
    width: Constants.width
    height: Constants.height
    color: "#151515"


    ScrollView {
        id: scrollView
        x: 42
        y: 77
        width: 966
        height: 1621

        TextArea {
            id: textArea
            x: 0
            width: 966
            anchors.top: parent.top
            anchors.bottom: parent.bottom
            wrapMode: Text.WordWrap
            anchors.topMargin: 115
            anchors.bottomMargin: -1500
            hoverEnabled: true
            font.pointSize: 50
            placeholderText: qsTr("Text Area")
        }
    }

    Rectangle {
        id: rectangle2
        x: 40
        y: 42
        width: 956
        height: 125
        color: "#2a2a2a"
        radius: 50

        Text {
            id: text1
            x: 44
            y: 13
            width: 717
            height: 100
            text: qsTr("Talking to: PyChat")
            font.pixelSize: 70
        }
    }

    Rectangle {
        id: rectangle1
        x: 28
        y: 1743
        width: 986
        height: 111
        color: "#cbcbcb"
        radius: 40
        border.width: 0
        layer.smooth: false

        TextInput {
            id: textInput
            x: -18
            y: 21
            width: 916
            height: 70
            text: qsTr("Type to the bot here!")
            font.pixelSize: 70
            scale: 0.869
        }

        Button {
            id: button1
            x: 877
            y: 7
            width: 100
            height: 100
            text: qsTr("Button")
            icon.color: "#00ffffff"
            highlighted: false
            flat: true
            icon.height: 110
            icon.width: 110
            icon.source: "../png-transparent-computer-icons-send-miscellaneous-angle-rectangle-thumbnail-removebg-preview.png"
            display: AbstractButton.IconOnly
        }
    }


    states: [
        State {
            name: "clicked"
            when: button.checked
        }
    ]
}
