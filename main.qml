import QtQuick 2.15
import QtQuick.Controls 2.15

ApplicationWindow{
    visible: true 
    width: 400
    hight: 300
    title: "Calc Memorization"

    Column{
        anchors.centerIn: parent 

        Label{
            text: "Welcome to Calc Memorization!"
            font.pixelsize: 18
            font.bold: true 
        }
    }
}