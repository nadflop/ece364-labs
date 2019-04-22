#######################################################
#   Author:     Nur Nadhira Aqilah Binti Mohd Shah
#   email:      mohdshah@purdue.edu
#   ID:         ee364g02
#   Date:       4/19/2019
#######################################################
import sys
from PyQt5 import QtCore, QtGui
from PyQt5.QtWidgets import QMainWindow, QApplication, QFileDialog
from Lab12.MorphingGUI import *
from Lab12.Morphing import *
from PyQt5.QtCore import Qt


class Morphing(QMainWindow, Ui_Dialog):

     def __init__(self, parent=None):
         #self.leftTriangles, self.rightTriangles = loadTriangles("~ee364/DataFolder/Lab12/TestData/points.left.txt", "~ee364/DataFolder/Lab12/TestData/points.right.txt")
         super(Morphing, self).__init__(parent)
         self.setupUi(self)
         self.lineEdit.setEnabled(False)
         self.horizontalSlider.setEnabled(False)
         self.pushButton.setEnabled(False)
         self.checkBox.setEnabled(False)
         self.horizontalSlider.setTickInterval(1)
         self.horizontalSlider.setTickPosition(10)
         self.horizontalSlider.sliderMoved.connect(self.printValue)
         self.image1Path = None
         self.image2Path = None
         self.toolButton.clicked.connect(self.leftImage)
         self.toolButton_2.clicked.connect(self.rightImage)
         self.checkBox.stateChanged.connect(self.clearTriangles)
         self.pushButton.clicked.connect(self.morpher)
         self.mousePressEvent = self.exitSelection
         self.graphicsView.mousePressEvent = self.mouseReleaseEvent
         self.graphicsView_2.mousePressEvent = self.mouseReleaseEvent2
         self.count1 = 0
         self.count2 = 0
         self.keyPressEvent = self.keyReleaseEvent
         self.hasPoints = False
         self.leftTriangles = 0
         self.rightTriangles = 0
     #def mouseReleaseEvent(self, a0: QtGui.QMouseEvent):
     #    print('(', QtGui.QMouseEvent.x(), ',', QtGui.QMouseEvent.y(), ')')
     #keyEvent.key ==

     def printValue(self):
         self.lineEdit.setText(str(self.horizontalSlider.sliderPosition() / 20))

     def mouseReleaseEvent(self, QMouseEvent):
         if self.count1 == 1 and self.count2 == 1:
             self.count1 = 0
             self.count2 = 0
             self.scene1.removeItem(self.scene1.items()[0])
             self.scene1.addEllipse(self.prevx * 1440 / 256, self.prevy * 1080 / 192, 20, 20, Qt.transparent, Qt.blue)
             self.scene2.removeItem(self.scene2.items()[0])
             self.scene2.addEllipse(self.prevx2 * 1440 / 256, self.prevy2 * 1080 / 192, 20, 20, Qt.transparent, Qt.blue)
             self.confirmPoints((self.prevx,self.prevy),(self.prevx2,self.prevy2))

         if self.count1 == self.count2:
            self.graphicsView.setMouseTracking(True)
            self.status = 'LEFT'
            x = QMouseEvent.x()
            y = QMouseEvent.y()
            self.prevx = x
            self.prevy = y
            if x <= 256 and y <= 192:
                self.scene1.addEllipse(x*1440/256,y*1080/192,20,20, Qt.transparent, Qt.green)
                self.count1 += 1

     def mouseReleaseEvent2(self, QMouseEvent):
         if self.count1 > self.count2:
            self.graphicsView.setMouseTracking(True)
            x = QMouseEvent.x()
            y = QMouseEvent.y()
            self.prevx2 = x
            self.prevy2 = y
            self.scene2.addEllipse(x*1440/256,y*1080/192,20,20, Qt.transparent, Qt.green)
            self.count2 += 1
            self.status = 'RIGHT'
            #self.mousePressEvent = self.exitSelection

     def exitSelection(self, event):
         if self.count1 == 1 and self.count2 == 1:# and self.status == 'RIGHT':
             self.count1 = 0
             self.count2 = 0
             self.scene1.removeItem(self.scene1.items()[0])
             self.scene2.removeItem(self.scene2.items()[0])
             self.scene1.addEllipse(self.prevx * 1440 / 256, self.prevy * 1080 / 192, 20, 20, Qt.transparent, Qt.blue)
             self.scene2.addEllipse(self.prevx2 * 1440 / 256, self.prevy2 * 1080 / 192, 20, 20, Qt.transparent, Qt.blue)
             self.status = 'RIGHT'
             self.confirmPoints((self.prevx,self.prevy),(self.prevx2,self.prevy2))

         #logic for allowing to add another point on the same picture
     def keyReleaseEvent(self, QKeyEvent):
        if QKeyEvent.isAutoRepeat():
            QKeyEvent.ignore()
            return
        if QKeyEvent.key() == QtCore.Qt.Key_Backspace:
            #delete the previous dot
            if self.status == 'LEFT' and self.count2 == 0 and self.count1 == 1:
                self.scene1.removeItem(self.scene1.items()[0])
                self.count1 = 0
                QKeyEvent.accept()
            elif self.status == 'RIGHT' and self.count1 == 1 and self.count2 == 1:
                self.scene2.removeItem(self.scene2.items()[0])
                self.count2 = 0
                QKeyEvent.accept()
            else:
                self.status = 'LEFT'
                QKeyEvent.ignore()

     def leftImage(self):
         filePath, _ = QFileDialog.getOpenFileName(self, caption='Open Image file ...', filter="JPG files (*.jpg)")

         if not filePath:
             return

         imageObject = QtGui.QImage(filePath)#.scaled(250, 190, QtCore.Qt.KeepAspectRatio)
         image = QtGui.QPixmap.fromImage(imageObject)

         scene = QtWidgets.QGraphicsScene(self)
         scene.addPixmap(image)

         self.graphicsView.setScene(scene)
         self.graphicsView.fitInView(self.graphicsView.sceneRect(), QtCore.Qt.KeepAspectRatio)
         self.image1Path = filePath
         self.enableBtn()
         array = []
         if os.path.isfile(self.image1Path + '.txt'):
             DataPath = os.path.expanduser(self.image1Path + '.txt')
             with open(DataPath, "r") as f:
                 data = [line.strip().split(' ') for line in f.read().splitlines()]
             for element in data:
                 array.append([np.float64(element[0]), np.float64(element[-1])])
             self.points1 = np.array(array)
             for x, y in self.points1:
                 scene.addEllipse(x, y, 20, 20, Qt.transparent, Qt.red)
         else:
             open(self.image1Path + '.txt').close()

         self.scene1 = scene

     def rightImage(self):
         filePath, _ = QFileDialog.getOpenFileName(self, caption='Open Image file ...', filter="JPG files (*.jpg)")

         if not filePath:
             return

         imageObject = QtGui.QImage(filePath)
         image = QtGui.QPixmap.fromImage(imageObject)#.scaled(251.5, 190, QtCore.Qt.KeepAspectRatio)

         scene = QtWidgets.QGraphicsScene(self)
         scene.addPixmap(image)

         self.graphicsView_2.setScene(scene)

         self.graphicsView_2.fitInView(self.graphicsView_2.sceneRect(), QtCore.Qt.KeepAspectRatio)
         self.image2Path = filePath
         self.enableBtn()

         array = []
         if os.path.isfile(self.image2Path + '.txt'):
             DataPath = os.path.expanduser(self.image2Path + '.txt')
             with open(DataPath, "r") as f:
                 data = [line.strip().split(' ') for line in f.read().splitlines()]
             for element in data:
                 array.append([np.float64(element[0]), np.float64(element[-1])])
             self.points2 = np.array(array)
             for x, y in self.points2:
                 scene.addEllipse(x, y, 20, 20, Qt.transparent, Qt.red)
         else:
             open(self.image2Path + '.txt').close()

         self.scene2 = scene

     def enableBtn(self):
         if self.image1Path != None and self.image2Path != None:
             self.lineEdit.setEnabled(True)
             self.horizontalSlider.setEnabled(True)
             self.pushButton.setEnabled(True)
             self.checkBox.setEnabled(True)

     def morpher(self):
        alpha = float(self.lineEdit.text())
        if os.path.isfile(self.image1Path) and os.path.isfile(self.image2Path):
            self.leftTriangles, self.rightTriangles = loadTriangles(
                self.image1Path + '.txt',
                self.image2Path + '.txt')
        result = Morpher(np.array(imageio.imread(self.image1Path), dtype= np.uint8),
                         self.leftTriangles,
                         np.array(imageio.imread(self.image2Path), dtype=np.uint8),
                         self.rightTriangles)
        image1 = result.getImageAtAlpha(float(alpha))
        imageObject = QtGui.QImage(image1, image1.shape[1], image1.shape[0], QtGui.QImage.Format_Grayscale8)
        image = QtGui.QPixmap.fromImage(imageObject)
        scene = QtWidgets.QGraphicsScene(self)
        scene.addPixmap(image)
        self.graphicsView_3.setScene(scene)
        self.graphicsView_3.fitInView(self.graphicsView_3.sceneRect(), True)

     def showTriangles(self):
         for element in self.leftTriangles:
             self.scene1.addLine(element.vertices[0][0], element.vertices[0][1], element.vertices[1][0], element.vertices[1][1], Qt.red)
             self.scene1.addLine(element.vertices[1][0], element.vertices[1][1], element.vertices[2][0], element.vertices[2][1], Qt.red)
             self.scene1.addLine(element.vertices[2][0], element.vertices[2][1], element.vertices[0][0], element.vertices[0][1], Qt.red)
         for element in self.rightTriangles:
             self.scene2.addLine(element.vertices[0][0], element.vertices[0][1], element.vertices[1][0], element.vertices[1][1], Qt.red)
             self.scene2.addLine(element.vertices[1][0], element.vertices[1][1], element.vertices[2][0], element.vertices[2][1], Qt.red)
             self.scene2.addLine(element.vertices[2][0], element.vertices[2][1], element.vertices[0][0], element.vertices[0][1], Qt.red)

     def clearTriangles(self):
         if self.checkBox.isChecked() == True:
             if os.path.isfile(self.image1Path + '.txt') and os.path.isfile(self.image2Path + '.txt'):
                 self.leftTriangles, self.rightTriangles = loadTriangles(
                     self.image1Path + '.txt',
                     self.image2Path + '.txt') #replace with image1 and image2 path later
             self.showTriangles()
         else:
             if self.image1Path != None and self.image2Path != None:
                 for item in self.scene1.items():
                     if type(item) is QtWidgets.QGraphicsLineItem:
                         self.scene1.removeItem(item)
                 for item in self.scene2.items():
                     if type(item) is QtWidgets.QGraphicsLineItem:
                         self.scene2.removeItem(item)

     def confirmPoints(self, left_coord, right_coord):
        if self.hasPoints == False:
            self.startPoints = np.array([[left_coord[0],left_coord[1]]])
            self.endPoints = np.array([[right_coord[0],right_coord[1]]])
        else:
            self.startPoints = np.vstack((self.startPoints,left_coord))
            self.endPoints = np.vstack((self.startPoints,right_coord))

        #update triangulation
        if self.checkBox.isChecked():
            self.clearTriangles()
        #write confirmed points to file
        with open(self.image1Path + '.txt', 'a+') as f:
            f.writelines([str(np.round(coord[0] * 1440 / 256)) + ' ' + str(np.round(coord[1]*1080 / 192)) + '\n' for coord in self.startPoints.tolist()])
        with open(self.image2Path + '.txt', 'a+') as f:
            f.writelines([str(np.round(coord[0] * 1440 / 256)) + ' ' + str(np.round(coord[1]*1080 / 192)) + '\n' for coord in self.endPoints.tolist()])

if __name__ == "__main__":
     currentApp = QApplication(sys.argv)
     currentForm = Morphing()

     currentForm.show()
     currentApp.exec_()