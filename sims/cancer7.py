import sys
from PyQt5 import QtCore, QtWidgets
from PyQt5.QtCore import QTimer
from PyQt5.QtGui import QCursor
from PyQt5.QtGui import QIcon
import random

class Ui_Form(object):
    def setupUi(self, Form):

        #self.ct = "Breast"
        #self.ct = "Prostate"
        #self.ct = "Lung"
        #self.ct = "Colon/Rectal"
        #self.ct = "Melanoma"
        #self.ct = "Bladder"
        self.ct = "Kidney"
        #self.ct = "Non-Hodgkin Lymphoma (NHL)"
        #self.ct = "Endometrial"
        #self.ct = "Pancreatic"

        self.array1 = []
        self.array2 = []

        self.hormonalMultiplyer = 1
        self.hasRunWave = False
        self.count = 0
        self.count2 = 0
        self.flag = False
        self.spreadRateVal = 20
        self.overcomeProb = 0.05
        self.bal = 400000
        self.cellStates = {}
        self.sides = []
        self.makeVisible = False
        self.makeVisible2 = False
        self.metaCount = 0

        Form.setObjectName("Form")
        Form.setStyleSheet("background-color : rgba(20,20,20,250); color: white")

        Form.resize(900, 900)
        self.groupBox_2 = QtWidgets.QGroupBox(Form)
        self.groupBox_2.setGeometry(QtCore.QRect(10, 660, 631, 231))
        self.groupBox_2.setObjectName("groupBox_2")

        self.scrollArea = QtWidgets.QScrollArea(self.groupBox_2)
        self.scrollArea.setGeometry(QtCore.QRect(10, 20, 211, 201))
        self.scrollArea.setVerticalScrollBarPolicy(QtCore.Qt.ScrollBarAlwaysOff)
        self.scrollArea.setWidgetResizable(True)
        self.scrollArea.setObjectName("scrollArea")
        self.scrollAreaWidgetContents = QtWidgets.QWidget()
        self.scrollAreaWidgetContents.setGeometry(QtCore.QRect(0, 0, 209, 199))
        self.scrollAreaWidgetContents.setObjectName("scrollAreaWidgetContents")
        self.checkBox = QtWidgets.QCheckBox(self.scrollAreaWidgetContents)
        self.checkBox.setGeometry(QtCore.QRect(10, 10, 181, 17))
        self.checkBox.setObjectName("checkBox")

        self.checkBox.stateChanged.connect(self.surgPrompt)

        self.checkBox_2 = QtWidgets.QCheckBox(self.scrollAreaWidgetContents)
        self.checkBox_2.setGeometry(QtCore.QRect(10, 30, 161, 17))
        self.checkBox_2.setObjectName("checkBox_2")
        self.checkBox_3 = QtWidgets.QCheckBox(self.scrollAreaWidgetContents)
        self.checkBox_3.setGeometry(QtCore.QRect(10, 50, 191, 17))
        self.checkBox_3.setObjectName("checkBox_3")
        self.checkBox_4 = QtWidgets.QCheckBox(self.scrollAreaWidgetContents)
        self.checkBox_4.setGeometry(QtCore.QRect(10, 70, 161, 17))
        self.checkBox_4.setObjectName("checkBox_4")

        self.checkBox_4.hide()

        self.checkBox_5 = QtWidgets.QCheckBox(self.scrollAreaWidgetContents)
        self.checkBox_5.setGeometry(QtCore.QRect(10, 70, 161, 17))
        self.checkBox_5.setObjectName("checkBox_5")
        self.checkBox_6 = QtWidgets.QCheckBox(self.scrollAreaWidgetContents)
        self.checkBox_6.setGeometry(QtCore.QRect(10, 90, 161, 17))
        self.checkBox_6.setObjectName("checkBox_6")
        self.checkBox_7 = QtWidgets.QCheckBox(self.scrollAreaWidgetContents)
        self.checkBox_7.setGeometry(QtCore.QRect(10, 110, 161, 17))
        self.checkBox_7.setObjectName("checkBox_7")
        self.checkBox_8 = QtWidgets.QCheckBox(self.scrollAreaWidgetContents)
        self.checkBox_8.setGeometry(QtCore.QRect(10, 130, 161, 17))
        self.checkBox_8.setObjectName("checkBox_8")
        self.checkBox_9 = QtWidgets.QCheckBox(self.scrollAreaWidgetContents)
        self.checkBox_9.setGeometry(QtCore.QRect(10, 150, 161, 17))
        self.checkBox_9.setObjectName("checkBox_9")
        self.scrollArea.setWidget(self.scrollAreaWidgetContents)
        self.scrollArea_2 = QtWidgets.QScrollArea(self.groupBox_2)
        self.scrollArea_2.setGeometry(QtCore.QRect(230, 20, 391, 201))
        self.scrollArea_2.setVerticalScrollBarPolicy(QtCore.Qt.ScrollBarAlwaysOff)
        self.scrollArea_2.setWidgetResizable(True)
        self.scrollArea_2.setObjectName("scrollArea_2")
        self.scrollAreaWidgetContents_2 = QtWidgets.QWidget()
        self.scrollAreaWidgetContents_2.setGeometry(QtCore.QRect(0, 0, 389, 199))
        self.scrollAreaWidgetContents_2.setObjectName("scrollAreaWidgetContents_2")
        self.textBrowser = QtWidgets.QTextBrowser(self.scrollAreaWidgetContents_2)
        self.textBrowser.setGeometry(QtCore.QRect(10, 32, 371, 161))
        self.textBrowser.setObjectName("textBrowser")
        self.label_2 = QtWidgets.QLabel(self.scrollAreaWidgetContents_2)
        self.label_2.setGeometry(QtCore.QRect(10, 0, 331, 30))
        self.label_2.setObjectName("label_2")
        self.scrollArea_2.setWidget(self.scrollAreaWidgetContents_2)
        self.groupBox_3 = QtWidgets.QGroupBox(Form)
        self.groupBox_3.setGeometry(QtCore.QRect(650, 10, 241, 882))
        self.groupBox_3.setObjectName("groupBox_3")
        self.label = QtWidgets.QLabel(self.groupBox_3)
        self.label.setGeometry(QtCore.QRect(10, 20, 40, 21))
        self.label.setObjectName("label")
        self.textBrowser_2 = QtWidgets.QTextBrowser(self.groupBox_3)
        self.textBrowser_2.setGeometry(QtCore.QRect(59, 20, 171, 21))
        self.textBrowser_2.setVerticalScrollBarPolicy(QtCore.Qt.ScrollBarAlwaysOff)
        self.textBrowser_2.setObjectName("textBrowser_2")
        self.line = QtWidgets.QFrame(self.groupBox_3)
        self.line.setGeometry(QtCore.QRect(10, 42, 221, 16))
        self.line.setFrameShape(QtWidgets.QFrame.HLine)
        self.line.setFrameShadow(QtWidgets.QFrame.Sunken)
        self.line.setObjectName("line")
        self.textBrowser_3 = QtWidgets.QTextBrowser(self.groupBox_3)
        self.textBrowser_3.setGeometry(QtCore.QRect(10, 60, 221, 610))
        self.textBrowser_3.setObjectName("textBrowser_3")
        self.label_3 = QtWidgets.QLabel(self.groupBox_3)
        self.label_3.setGeometry(QtCore.QRect(10, 680, 131, 21))
        self.label_3.setObjectName("label_3")
        self.label_4 = QtWidgets.QLabel(self.groupBox_3)
        self.label_4.setGeometry(QtCore.QRect(10, 700, 131, 21))
        self.label_4.setObjectName("label_4")
        self.scrollArea_3 = QtWidgets.QScrollArea(self.groupBox_3)
        self.scrollArea_3.setGeometry(QtCore.QRect(10, 730, 221, 141))
        self.scrollArea_3.setWidgetResizable(True)
        self.scrollArea_3.setObjectName("scrollArea_3")
        self.scrollAreaWidgetContents_3 = QtWidgets.QWidget()
        self.scrollAreaWidgetContents_3.setGeometry(QtCore.QRect(0, 0, 219, 139))
        self.scrollAreaWidgetContents_3.setObjectName("scrollAreaWidgetContents_3")
        self.startTreatment = QtWidgets.QToolButton(self.scrollAreaWidgetContents_3)
        
        # start timer
        self.startTreatment.setGeometry(QtCore.QRect(20, 20, 91, 101))
        self.startTreatment.setObjectName("startTreatment")
        
        start = self.startTreatment
        start.pressed.connect(self.Start)

        # pause timer
        self.startTreatment_2 = QtWidgets.QToolButton(self.scrollAreaWidgetContents_3)
        self.startTreatment_2.setGeometry(QtCore.QRect(110, 20, 91, 101))
        self.startTreatment_2.setObjectName("startTreatment_2")

        pause = self.startTreatment_2
        pause.pressed.connect(self.Pause)

        timer = QTimer(Form)
        timer.timeout.connect(self.showTime)
        timer.timeout.connect(self.updateDiag)
        timer.start(100)

        self.scrollArea_3.setWidget(self.scrollAreaWidgetContents_3)
        self.ImmCtdwn = QtWidgets.QTextBrowser(self.groupBox_3)
        self.ImmCtdwn.setGeometry(QtCore.QRect(140, 680, 111, 21))
        self.ImmCtdwn.setVerticalScrollBarPolicy(QtCore.Qt.ScrollBarAlwaysOff)
        self.ImmCtdwn.setObjectName("ImmCtdwn")
        self.Duration = QtWidgets.QTextBrowser(self.groupBox_3)
        self.Duration.setGeometry(QtCore.QRect(140, 700, 111, 21))
        self.Duration.setVerticalScrollBarPolicy(QtCore.Qt.ScrollBarAlwaysOff)
        self.Duration.setObjectName("Duration")

        self.groupBox_4 = QtWidgets.QGroupBox(Form)
        self.groupBox_4.setGeometry(QtCore.QRect(10, 10, 631, 645))
        self.groupBox_4.setObjectName("groupBox_4")
        self.retranslateUi(Form)
        QtCore.QMetaObject.connectSlotsByName(Form)

        self.gridLayoutWidget = QtWidgets.QWidget(self.groupBox_4)
        self.gridLayoutWidget.setGeometry(QtCore.QRect(10, 20, 611, 631))  # Adjust geometry if needed
        self.gridLayoutWidget.setObjectName("gridLayoutWidget")
        self.gridLayout = QtWidgets.QGridLayout(self.gridLayoutWidget)
        self.gridLayout.setObjectName("gridLayout")

        self.cellButtons = {}  # Store cell buttons with IDs

        self.rcc = 20
        for i in range(self.rcc):
            for j in range(self.rcc):
                cell_id = f"cell_{i}_{j}"  # Unique ID for each cell
                button = QtWidgets.QPushButton(self.gridLayoutWidget)
                button.setFixedSize(24, 24)
                button.setObjectName(cell_id)
                button.clicked.connect(lambda _, x=i, y=j: self.cellClicked(x, y))
                self.cellButtons[cell_id] = button  # Store button in a dictionary
                self.gridLayout.addWidget(button, i, j)

        self.initializeCells()

        budget = self.textBrowser_2
        budget.setText("$" + f"{self.bal:,}")
        self.textBrowser_3.setText(" ")

     # Timer for updating the cursor-following position
        self.timer = QTimer()
        self.timer.timeout.connect(self.update_text_box_position)

        # Create text box but don't show it yet
        self.text_box = QtWidgets.QLineEdit(Form)
        self.text_box.returnPressed.connect(self.return_text)
        self.text_box.setGeometry(QtCore.QRect(0, 0, 400, 20))
        self.text_box.hide()

    def surgPrompt(self):
        if self.checkBox.isChecked():
            # Show the text box and start the timer to follow the cursor
            self.text_box.setText('Enter the cell range to remove in the form "X.Y : X.Y"\n\n(0.0 is top left, 19.19 is bottom right)')
            self.text_box.show()
            self.text_box.selectAll()
            self.text_box.setFocus()
            self.timer.start(10)  # Update position every 10 milliseconds

    def update_text_box_position(self):
        # Move the text box to follow the cursor
        cursor_pos = QCursor.pos()
        local_pos = self.text_box.parent().mapFromGlobal(cursor_pos)
        self.text_box.move(local_pos)

    def return_text(self):
        # Capture text, stop timer, and hide text box
        entered_text = self.text_box.text()
        print("Entered Text:", entered_text)  # Replace with desired action for entered text
        self.formatAndSend(entered_text)
        self.timer.stop()
        self.text_box.hide()

    def formatAndSend(self, input_str):
        # Split the input string into the two parts (X.Y and A.B)
        part1, part2 = input_str.split(":")

        # Split each part into the respective numbers
        x, y = map(int, part1.split("."))
        a, b = map(int, part2.split("."))

        # Create the first array of numbers from x to a
        first_array = list(range(x, a + 1))

        # Create the second array of numbers from y to b
        second_array = list(range(y, b + 1))

        self.array1 = first_array
        self.array2 = second_array


    def initializeCells(self):
        # Initialize all cells to green
        for i in range(self.rcc):
            for j in range(self.rcc):
                cell_id = f"cell_{i}_{j}"
                self.cellStates[cell_id] = "green"  # Set all cells initially to green
                self.cellButtons[cell_id].setStyleSheet("background-color : green; color: white;")

        # Define starting point for the main "tumor" cluster near the center
        center_i, center_j = self.rcc // 2, self.rcc // 2
        initial_cluster = [(center_i, center_j)]
        self.cellStates[f"cell_{center_i}_{center_j}"] = "red"
        self.cellButtons[f"cell_{center_i}_{center_j}"].setStyleSheet("background-color : red; color: white;")
        
        # Parameters for controlling blob size and spread
        expansion_probability = 0.5  # Lower probability for smaller spread
        max_blob_size = int(self.rcc * 1.5)  # Define a cap on the blob size
        
        # Blob growth logic: Expand outward from the center, limiting the size
        blob_size = 1  # Start with 1 red cell
        while initial_cluster and blob_size < max_blob_size:
            i, j = initial_cluster.pop(0)
            
            # Check neighboring cells to spread red color
            neighbors = [
                (i - 1, j), (i + 1, j),  # vertical neighbors
                (i, j - 1), (i, j + 1)   # horizontal neighbors
            ]
            
            for ni, nj in neighbors:
                if 0 <= ni < self.rcc and 0 <= nj < self.rcc:
                    neighbor_id = f"cell_{ni}_{nj}"
                    
                    # Spread red to this neighbor with a certain probability
                    if self.cellStates[neighbor_id] == "green" and random.random() < expansion_probability:
                        self.cellStates[neighbor_id] = "red"
                        self.cellButtons[neighbor_id].setStyleSheet("background-color : red; color: white;")
                        initial_cluster.append((ni, nj))  # Add this cell to continue spreading
                        blob_size += 1  # Increase the blob size count

        # Optionally add a few scattered red cells as outliers
        num_outliers = int(self.rcc * 0.05)  # Fewer outliers for a smaller cluster
        for _ in range(num_outliers):
            outlier_i, outlier_j = random.randint(0, self.rcc - 1), random.randint(0, self.rcc - 1)
            outlier_id = f"cell_{outlier_i}_{outlier_j}"
            
            if self.cellStates[outlier_id] == "green":  # Only turn green cells to red
                self.cellStates[outlier_id] = "red"
                self.cellButtons[outlier_id].setStyleSheet("background-color : red; color: white;")

        if self.checkReds() < 5:
            self.checkBox_2.setCheckable(False)
            self.checkBox_3.setCheckable(False)
        else:
            self.checkBox_2.setCheckable(True)
            self.checkBox_3.setCheckable(True)

    def updateCellStatesNonCancer(self):
        new_cell_states = self.cellStates.copy()  # To avoid changing states mid-iteration

        for i in range(self.rcc):
            for j in range(self.rcc):
                cell_id = f"cell_{i}_{j}"
                
                if self.cellStates[cell_id] == "green":  # Healthy cell
                    neighbors = [(i-1, j), (i+1, j), (i, j-1), (i, j+1)]
                    for ni, nj in neighbors:
                        neighbor_id = f"cell_{ni}_{nj}"
                        if 0 <= ni < self.rcc and 0 <= nj < self.rcc and self.cellStates.get(neighbor_id) == "red":
                            if random.random() < self.overcomeProb:
                                new_cell_states[neighbor_id] = "green"
                        if 0 <= ni < self.rcc and 0 <= nj < self.rcc and self.cellStates.get(neighbor_id) == "black":
                            if random.random() < (self.overcomeProb*2):
                                new_cell_states[neighbor_id] = "green"

                elif self.cellStates[cell_id] == "yellow": #damaged cell
                    check = random.random()
                    if check < 0.05:
                        new_cell_states[cell_id] = "black"
                    elif check < 0.3:
                        new_cell_states[cell_id] = "green"
                    elif check < 0.5:
                        new_cell_states[cell_id] = "red"
                
        # Apply the updated states and refresh colors
        for cell_id, new_state in new_cell_states.items():
            if self.cellStates[cell_id] != new_state:  # If state has changed
                self.cellStates[cell_id] = new_state
                self.cellButtons[cell_id].setStyleSheet(f"background-color : {new_cell_states[cell_id]}; color : white;")
                self.cellButtons[cell_id].setText(" ")

    def updateCellStatesCancer(self):
        new_cell_states = self.cellStates.copy()  # To avoid changing states mid-iteration

        for i in range(self.rcc):
            for j in range(self.rcc):
                cell_id = f"cell_{i}_{j}"

                if self.cellStates[cell_id] == "red":  # Cancer cell
                    neighbors = [(i-1, j), (i+1, j), (i, j-1), (i, j+1)]
                    for ni, nj in neighbors:
                        neighbor_id = f"cell_{ni}_{nj}"
                        if 0 <= ni < self.rcc and 0 <= nj < self.rcc and self.cellStates.get(neighbor_id) == "green":
                            if random.random() < 0.5:
                                new_cell_states[neighbor_id] = "red"
                
                    if random.random() < 0.01 and self.cellButtons[cell_id].text() == "*":
                        new_cell_states[cell_id] = "black"

                    if random.random() < 0.002:
                        self.metaCount += 1
                
        # Apply the updated states and refresh colors
        for cell_id, new_state in new_cell_states.items():
            if self.cellStates[cell_id] != new_state:  # If state has changed
                self.cellStates[cell_id] = new_state
                self.cellButtons[cell_id].setStyleSheet(f"background-color : {new_cell_states[cell_id]}; color : white;")
                self.cellButtons[cell_id].setText(" ")

    def updateDiag(self):
        if self.flag:
            # Initialize counters for each cell type
            healthy_count = 0
            damaged_count = 0
            cancer_count = 0
            dead_count = 0
            
            # Count each type based on cellStates
            for cell_id, color in self.cellStates.items():
                if color == "green":
                    healthy_count += 1
                elif color == "yellow":
                    damaged_count += 1
                elif color == "red":
                    cancer_count += 1
                elif color == "black":
                    dead_count += 1
            
            # Total cell count
            total_cells = self.rcc * self.rcc
            
            # Calculate percentages
            healthy_percent = (healthy_count / total_cells) * 100
            damaged_percent = (damaged_count / total_cells) * 100
            cancer_percent = (cancer_count / total_cells) * 100
            dead_percent = (dead_count / total_cells) * 100
            
            if self.sides == []:
                sidesText = "No noted side effects"

            else:
                sidesText = f"Treatment Side Effects: {', '.join(map(str, self.sides))}"

            # Format the display text
            diag_text = (
                f"Cancer Type:  {self.ct}\n\n"
                f"Healthy Cells: {healthy_count}/{total_cells} ({healthy_percent:.2f}%)\n"
                f"Damaged Cells: {damaged_count}/{total_cells} ({damaged_percent:.2f}%)\n"
                f"Cancer Cells: {cancer_count}/{total_cells} ({cancer_percent:.2f}%)\n"
                f"Dead Cells: {dead_count}/{total_cells} ({dead_percent:.2f}%)\n\n"
                f"{sidesText}\n\n"
                f"Cancer cells metastasized: {self.metaCount}"
            )
            
            # Display the diagnostics in the text browser
            self.textBrowser_3.setText(diag_text)

    def showTime(self):
        if self.metaCount >9:
            self.gameover()

        if self.flag:
            self.count += 1
            self.count2 += 1

            if self.count2 == 200:
                self.count2 = 0
                for i in range(self.rcc):
                    for j in range(self.rcc):
                        miniCell = f"cell_{i}_{j}"
                        self.cellButtons[miniCell].setStyleSheet("background-color : white; color: white;")
                self.hasRunWave = True
            else:
                if self.count % (self.spreadRateVal*self.hormonalMultiplyer) == 0:
                    self.updateCellStatesCancer()
                if self.count % self.spreadRateVal == 0:
                    self.updateCellStatesNonCancer()
                

            if self.count2 == 20:                
                if self.makeVisible & self.hasRunWave:
                    for i in range(self.rcc):
                        for j in range(self.rcc):
                            cell_id = f"cell_{i}_{j}"
                            if self.cellStates[cell_id] == "red":  # Critical cells are cancerous (red cells)
                                check = random.random()
                                if check < 0.2:
                                    self.cellButtons[cell_id].setStyleSheet("background-color : yellow; color: white;")
                                    self.cellStates[cell_id] = "yellow"
                                elif check < 0.8:
                                    self.cellButtons[cell_id].setStyleSheet("background-color : green; color: white;")
                                    self.cellStates[cell_id] = "green"
                                self.cellButtons[cell_id].setText(" ")
                    self.makeVisible = False
                    self.checkBox_7.setChecked(False)
                
                if self.makeVisible2 & self.hasRunWave:
                    for i in range(self.rcc):
                        for j in range(self.rcc):
                            cell_id = f"cell_{i}_{j}"
                            if self.cellStates[cell_id] == "red" and self.cellButtons[cell_id].text() == "*":  # Critical cells are cancerous (red cells)
                                check = random.random()
                                if check < 0.9:
                                    self.cellButtons[cell_id].setStyleSheet("background-color : green; color : white;")
                                    self.cellStates[cell_id] = "green"
                                self.cellButtons[cell_id].setText(" ")
                                
                    self.makeVisible2 = False
                    self.checkBox_8.setChecked(False)

                for i in range(self.rcc):
                    for j in range(self.rcc):
                        miniCell = f"cell_{i}_{j}"
                        original_color = self.cellStates[miniCell]
                        self.cellButtons[miniCell].setStyleSheet(f"background-color : {original_color}; color: white;")

        text = str(self.count / 10)
        text2 = str((200 - self.count2) / 10)
        self.Duration.setText(text)
        self.ImmCtdwn.setText(text2)

    def gameover(self):
        for i in range(self.rcc):
            for j in range(self.rcc):
                cell_id = f"cell_{i}_{j}"
                self.cellStates[cell_id] = "gray"
                self.cellButtons[cell_id].setStyleSheet("background-color : gray")
        print("game over")
        self.metaCount = 0
        self.textBrowser_3.setText("Game Over (10+ Cancer Cells Metastasized)")
        
        self.startTreatment.setEnabled(False)
        self.startTreatment_2.setEnabled(False)
        
        self.checkBox.setEnabled(False)
        self.checkBox_2.setEnabled(False)
        self.checkBox_3.setEnabled(False)
        self.checkBox_4.setEnabled(False)
        self.checkBox_5.setEnabled(False)
        self.checkBox_6.setEnabled(False)
        self.checkBox_7.setEnabled(False)
        self.checkBox_8.setEnabled(False)
        self.checkBox_9.setEnabled(False)

        self.flag = False

    def runChemo(self):
        self.chemoCost = 50000

        if self.bal >= self.chemoCost:
            if self.ct != "Kidney":
                self.bal -= self.chemoCost
                self.spreadRateVal = 40
                self.overcomeProb = 0.15

                self.sides = []
                chemoChoices = ['Hair Loss', 'Nausea & Vomiting', 'Anemia']
                probCheck1 = random.choice([chemoChoices[0], chemoChoices[0], chemoChoices[0], chemoChoices[0], chemoChoices[0], chemoChoices[0], chemoChoices[0], chemoChoices[0], chemoChoices[0], False])
                probCheck2 = random.choice([chemoChoices[1], chemoChoices[1], chemoChoices[1], False, False])
                probCheck3 = random.choice([chemoChoices[2], False])

                if probCheck1 == chemoChoices[0]: self.sides.append(probCheck1)
                if probCheck2 == chemoChoices[1]: self.sides.append(probCheck2)
                if probCheck3 == chemoChoices[2]: self.sides.append(probCheck3)

        else:
            self.highlightBalance()
            self.checkBox_5.setChecked(False)

    def runHormonal(self):
        self.hormonalCost = 60000

        if self.bal >= self.hormonalCost:
            if self.ct != "Lung" or  self.ct != "Colon/Rectal" or self.ct != "Melona" or self.ct != "Bladder" or self.ct != "Kidney" or self.ct != "Non-Hodgkin Lymphoma (NHL)" or self.ct != "Pancreatic":
                self.bal -= self.hormonalCost
                self.hormonalMultiplyer = 2
        else:
            self.highlightBalance()
            self.checkBox_6.setChecked(False)

    def resetChemo(self):
        self.spreadRateVal = 20
        self.overcomeProb = 0.05

    def highlightBalance(self):
        self.label.setStyleSheet("color : red")

    def runCheckpoints(self):
        self.checkpointsCost = 30000
        if self.bal >= self.checkpointsCost:
            if self.ct != "Pancreatic":
                self.makeVisible = True
                self.bal -= self.checkpointsCost
        else:
            self.highlightBalance()
            self.checkBox_7.setChecked(False)

    def runAntibodies(self):
        self.antibodiesCost = 80000
        if self.bal >= self.antibodiesCost:
            if self.ct != "Prostate" or self.ct != "Melanoma" or self.ct != "Endometrial" or self.ct != "Pancreatic":
                self.makeVisible2 = True
                self.bal -= self.antibodiesCost
                for i in range(self.rcc):
                            for j in range(self.rcc):
                                cell_id = f"cell_{i}_{j}"
                                if self.cellStates[cell_id] == "red":  # Critical cells are cancerous (red cells)
                                    self.cellButtons[cell_id].setText("*")
                                    self.cellButtons[cell_id].setStyleSheet("background-color : red; color: white;")
                                
        else:
            self.highlightBalance()
            self.checkBox_8.setChecked(False)

    def runRadio1(self):
        self.radio1Cost = 15000
        if self.bal >= self.radio1Cost:
            if self.ct != "Melanoma" or self.ct != "Kidney":
                self.bal -= self.radio1Cost

                new_cell_states = self.cellStates.copy()

                for i in range(self.rcc):
                    for j in range(self.rcc):
                        cell_id = f"cell_{i}_{j}"
                        
                        if self.cellStates[cell_id] == "red":  # Healthy cell
                            neighbors = [(i-1, j), (i+1, j), (i, j-1), (i, j+1)]
                            for ni, nj in neighbors:
                                neighbor_id = f"cell_{ni}_{nj}"
                                if 0 <= ni < self.rcc and 0 <= nj < self.rcc and self.cellStates.get(neighbor_id) == "red":
                                    if random.random() < 0.75:
                                        new_cell_states[cell_id] = "green"
                                    elif random.random() < 0.5:
                                        new_cell_states[cell_id] = "red"
                                    elif random.random() < 0.5:
                                        new_cell_states[cell_id] = "black"
                                    else:
                                        new_cell_states[cell_id] = "yellow"

                for cell_id, new_state in new_cell_states.items():
                    if self.cellStates[cell_id] != new_state:  # If state has changed
                        self.cellStates[cell_id] = new_state
                        self.cellButtons[cell_id].setStyleSheet(f"background-color : {new_cell_states[cell_id]}; color : white;")
                        self.cellButtons[cell_id].setText(" ")
                        
        else:
            self.highlightBalance()
            self.checkBox_2.setChecked(False)

    def runRadio2(self):
        self.radio2Cost = 30000
        if self.bal >= self.radio2Cost:
            if self.ct != "Melanoma" or self.ct != "Kidney":
                self.bal -= self.radio2Cost
                
                new_cell_states = self.cellStates.copy()

                for i in range(self.rcc):
                    for j in range(self.rcc):
                        cell_id = f"cell_{i}_{j}"
                        
                        if self.cellStates[cell_id] == "red":  # Healthy cell
                            neighbors = [(i-1, j), (i+1, j), (i, j-1), (i, j+1)]
                            for ni, nj in neighbors:
                                neighbor_id = f"cell_{ni}_{nj}"
                                if 0 <= ni < self.rcc and 0 <= nj < self.rcc and self.cellStates.get(neighbor_id) == "red":
                                    if random.random() < 0.95:
                                        new_cell_states[cell_id] = "green"
                                    else:
                                        new_cell_states[cell_id] = "red"

                for cell_id, new_state in new_cell_states.items():
                    if self.cellStates[cell_id] != new_state:  # If state has changed
                        self.cellStates[cell_id] = new_state
                        self.cellButtons[cell_id].setStyleSheet(f"background-color : {new_cell_states[cell_id]}; color : white;")
                        self.cellButtons[cell_id].setText(" ")

        else:
            self.highlightBalance()
            self.checkBox_3.setChecked(False)

    def runRadio2Alt(self):
        self.radio2Cost = 30000
        if self.bal >= self.radio2Cost:
            if self.ct != "Melanoma" or self.ct != "Kidney":
                self.bal -= self.radio2Cost
                
                new_cell_states = self.cellStates.copy()

                for i in range(self.rcc):
                    for j in range(self.rcc):
                        cell_id = f"cell_{i}_{j}"
                        
                        if self.cellStates[cell_id] == "red":  # Healthy cell
                            neighbors = [(i-1, j), (i+1, j), (i, j-1), (i, j+1)]
                            for ni, nj in neighbors:
                                neighbor_id = f"cell_{ni}_{nj}"
                                if 0 <= ni < self.rcc and 0 <= nj < self.rcc and self.cellStates.get(neighbor_id) == "red":
                                    if random.random() < 0.5:
                                        new_cell_states[cell_id] = "green"
                                    else:
                                        new_cell_states[cell_id] = "red"

                for cell_id, new_state in new_cell_states.items():
                    if self.cellStates[cell_id] != new_state:  # If state has changed
                        self.cellStates[cell_id] = new_state
                        self.cellButtons[cell_id].setStyleSheet(f"background-color : {new_cell_states[cell_id]}; color : white;")
                        self.cellButtons[cell_id].setText(" ")

            else:
                self.highlightBalance()
                self.checkBox_3.setChecked(False)

    def checkReds(self):
        reds = 0

        for i in range(self.rcc):
            for j in range(self.rcc):
                cell_id = f"cell_{i}_{j}"
                    
                if self.cellStates[cell_id] == "red":
                    reds += 1
        return reds

    def runSurgery(self):
        price = 1000+1000*(len(self.array1))*(len(self.array2))
        if self.bal >= price:

            self.bal -= price
            new_cell_states = self.cellStates.copy()
            
            for i in self.array1:
                for j in self.array2:
                    cell_id = f"cell_{i}_{j}"
                    if random.random() < 0.95:
                        new_cell_states[cell_id] = "green"
                    else:
                        new_cell_states[cell_id] = "yellow"

            for cell_id, new_state in new_cell_states.items():
                if self.cellStates[cell_id] != new_state:  # If state has changed
                    self.cellStates[cell_id] = new_state
                    self.cellButtons[cell_id].setStyleSheet(f"background-color : {new_cell_states[cell_id]}; color : white;")
                    self.cellButtons[cell_id].setText(" ")

        else:
            self.highlightBalance()
            self.checkBox.setChecked(False)

    def Start(self):
        self.flag = True

        if self.checkBox.isChecked():
            self.runSurgery()

        if self.checkBox_5.isChecked():
            self.runChemo()
        else:
            self.resetChemo()

        if self.checkBox_6.isChecked():
            self.runHormonal()

        if self.checkBox_7.isChecked():
            self.runCheckpoints()

        if self.checkBox_8.isChecked():
            self.runAntibodies()

        if self.checkBox_2.isChecked():
            self.runRadio1()

        if self.checkBox_3.isChecked():
            if self.checkReds() >= 15:
                self.runRadio2()
            else:
                self.runRadio2Alt()

        self.startTreatment.setEnabled(False)
        self.startTreatment_2.setEnabled(True)
        
        self.checkBox.setEnabled(False)
        self.checkBox_2.setEnabled(False)
        self.checkBox_3.setEnabled(False)
        self.checkBox_4.setEnabled(False)
        self.checkBox_5.setEnabled(False)
        self.checkBox_6.setEnabled(False)
        self.checkBox_7.setEnabled(False)
        self.checkBox_8.setEnabled(False)
        self.checkBox_9.setEnabled(False)

        if self.checkReds() < 5:
            self.checkBox_2.setChecked(False)
            self.checkBox_3.setChecked(False)

        self.textBrowser_2.setText("$" + f"{self.bal:,}")

    def Pause(self):
        self.flag = False
        self.startTreatment.setEnabled(True)
        self.startTreatment_2.setEnabled(False)

        self.checkBox.setChecked(False)
        self.checkBox_2.setChecked(False)
        self.checkBox_3.setChecked(False)
        self.checkBox_4.setChecked(False)
        self.checkBox_5.setChecked(False)
        self.checkBox_6.setChecked(False)
        self.checkBox_7.setChecked(False)
        self.checkBox_8.setChecked(False)
        self.checkBox_9.setChecked(False)


        self.checkBox.setEnabled(True)
        self.checkBox_2.setEnabled(True)
        self.checkBox_3.setEnabled(True)
        self.checkBox_4.setEnabled(True)
        self.checkBox_5.setEnabled(True)
        self.checkBox_6.setEnabled(True)
        self.checkBox_7.setEnabled(True)
        self.checkBox_8.setEnabled(True)
        self.checkBox_9.setEnabled(True)

        if self.checkReds() < 5:
            self.checkBox_2.setCheckable(False)
            self.checkBox_3.setCheckable(False)
        else:
            self.checkBox_2.setCheckable(True)
            self.checkBox_3.setCheckable(True)

    def cellClicked(self, row, col):
        pass

    def retranslateUi(self, Form):
        _translate = QtCore.QCoreApplication.translate
        Form.setWindowTitle(_translate("Form", "Form"))
        self.groupBox_2.setTitle(_translate("Form", "Treatment Plans"))
        self.checkBox.setText(_translate("Form", "Tissue Surgery"))
        self.checkBox_2.setText(_translate("Form", "External Beam Radiotherapy"))
        self.checkBox_3.setText(_translate("Form", "Intensity Modulated Radiotherapy"))
        self.checkBox_4.setText(_translate("Form", "Brachytherapy"))
        self.checkBox_5.setText(_translate("Form", "Chemotherapy"))
        self.checkBox_6.setText(_translate("Form", "Hormonal Therapy"))
        self.checkBox_7.setText(_translate("Form", "Checkpoint Inhibitors"))
        self.checkBox_8.setText(_translate("Form", "Monoclonal Antibodies"))
        self.checkBox_9.setText(_translate("Form", "Herbal*"))
        self.textBrowser.setHtml(_translate("Form", "<!DOCTYPE HTML PUBLIC \"-//W3C//DTD HTML 4.0//EN\" \"http://www.w3.org/TR/REC-html40/strict.dtd\">\n"
"<html><head><meta name=\"qrichtext\" content=\"1\" /><style type=\"text/css\">\n"
"p, li { white-space: pre-wrap; }\n"
"</style></head><body style=\" font-family:\'MS Shell Dlg 2\'; font-size:8.25pt; font-weight:400; font-style:normal;\">\n"
"<p style=\" margin-top:0px; margin-bottom:0px; margin-left:0px; margin-right:0px; -qt-block-indent:0; text-indent:0px;\"><span style=\" font-family:\'Courier New\'; font-size:10pt; color:#FFFFFF;\"> </span><span style=\" font-family:\'Courier New\'; font-size:10pt; font-style:italic; color:#FFFFFF;\">&quot;Tissue Surgery</span></p>\n"
"<p style=\" margin-top:0px; margin-bottom:0px; margin-left:0px; margin-right:0px; -qt-block-indent:0; text-indent:0px; line-height:120%; background-color:transparent;\"><span style=\" font-family:\'Courier New\'; font-size:10pt; font-style:italic; color:#FFFFFF; background-color:transparent;\"> - Enter a cell range when prompted to </span></p>\n"
"<p style=\" margin-top:0px; margin-bottom:0px; margin-left:0px; margin-right:0px; -qt-block-indent:0; text-indent:0px; line-height:120%; background-color:transparent;\"><span style=\" font-family:\'Courier New\'; font-size:10pt; font-style:italic; color:#FFFFFF; background-color:transparent;\">   remove the rectangle between the cells.</span></p>\n"
"<p style=\"-qt-paragraph-type:empty; margin-top:0px; margin-bottom:0px; margin-left:0px; margin-right:0px; -qt-block-indent:0; text-indent:0px; line-height:120%; font-family:\'Courier New\'; font-size:10pt; font-style:italic; color:#FFFFFF; background-color:transparent;\"><br /></p>\n"
"<p style=\" margin-top:0px; margin-bottom:0px; margin-left:0px; margin-right:0px; -qt-block-indent:0; text-indent:0px; line-height:120%; background-color:transparent;\"><span style=\" font-family:\'Courier New\'; font-size:10pt; font-style:italic; color:#FFFFFF; background-color:transparent;\"> External Beam Radiotherapy</span></p>\n"
"<p style=\" margin-top:0px; margin-bottom:0px; margin-left:0px; margin-right:0px; -qt-block-indent:0; text-indent:0px; line-height:120%; background-color:transparent;\"><span style=\" font-family:\'Courier New\'; font-size:10pt; font-style:italic; color:#FFFFFF; background-color:transparent;\"> -  Removes a contiguous portion of cells.</span></p>\n"
"<p style=\" margin-top:0px; margin-bottom:0px; margin-left:0px; margin-right:0px; -qt-block-indent:0; text-indent:0px; line-height:120%; background-color:transparent;\"><span style=\" font-family:\'Courier New\'; font-size:10pt; font-style:italic; color:#FFFFFF; background-color:transparent;\"> - (75% effective)</span></p>\n"
"<p style=\"-qt-paragraph-type:empty; margin-top:0px; margin-bottom:0px; margin-left:0px; margin-right:0px; -qt-block-indent:0; text-indent:0px; line-height:120%; font-family:\'Courier New\'; font-size:10pt; font-style:italic; color:#FFFFFF; background-color:transparent;\"><br /></p>\n"
"<p style=\" margin-top:0px; margin-bottom:0px; margin-left:0px; margin-right:0px; -qt-block-indent:0; text-indent:0px; line-height:120%; background-color:transparent;\"><span style=\" font-family:\'Courier New\'; font-size:10pt; font-style:italic; color:#FFFFFF; background-color:transparent;\"> Intensity Modulated Radiotherapy</span></p>\n"
"<p style=\" margin-top:0px; margin-bottom:0px; margin-left:0px; margin-right:0px; -qt-block-indent:0; text-indent:0px; line-height:120%; background-color:transparent;\"><span style=\" font-family:\'Courier New\'; font-size:10pt; font-style:italic; color:#FFFFFF; background-color:transparent;\"> -  Removes a contiguous portion of cells</span></p>\n"
"<p style=\" margin-top:0px; margin-bottom:0px; margin-left:0px; margin-right:0px; -qt-block-indent:0; text-indent:0px; line-height:120%; background-color:transparent;\"><span style=\" font-family:\'Courier New\'; font-size:10pt; font-style:italic; color:#FFFFFF; background-color:transparent;\"> - (99% effective)</span><span style=\" font-size:10pt; font-style:italic;\"><br /></span></p>\n"
"<p style=\" margin-top:0px; margin-bottom:0px; margin-left:0px; margin-right:0px; -qt-block-indent:0; text-indent:0px; line-height:120%; background-color:transparent;\"><span style=\" font-family:\'Courier New\'; font-size:10pt; font-style:italic; color:#FFFFFF; background-color:transparent;\"> Chemotherapy</span></p>\n"
"<p style=\" margin-top:0px; margin-bottom:0px; margin-left:0px; margin-right:0px; -qt-block-indent:0; text-indent:0px; line-height:120%; background-color:transparent;\"><span style=\" font-family:\'Courier New\'; font-size:10pt; font-style:italic; color:#FFFFFF; background-color:transparent;\"> - Limits cell division, but may lead to unwanted side effects. </span></p>\n"
"<p style=\"-qt-paragraph-type:empty; margin-top:0px; margin-bottom:0px; margin-left:0px; margin-right:0px; -qt-block-indent:0; text-indent:0px; font-style:italic;\"><br /></p>\n"
"<p style=\" margin-top:0px; margin-bottom:0px; margin-left:0px; margin-right:0px; -qt-block-indent:0; text-indent:0px; line-height:120%; background-color:transparent;\"><span style=\" font-family:\'Courier New\'; font-size:10pt; font-style:italic; color:#FFFFFF; background-color:transparent;\"> Hormonal Therapy</span></p>\n"
"<p style=\" margin-top:0px; margin-bottom:0px; margin-left:0px; margin-right:0px; -qt-block-indent:0; text-indent:0px; line-height:120%; background-color:transparent;\"><span style=\" font-family:\'Courier New\'; font-size:10pt; font-style:italic; color:#FFFFFF; background-color:transparent;\"> - Limits cancer cell division</span></p>\n"
"<p style=\" margin-top:0px; margin-bottom:0px; margin-left:0px; margin-right:0px; -qt-block-indent:0; text-indent:0px; line-height:120%; background-color:transparent;\"><span style=\" font-size:10pt; font-style:italic;\">   </span><span style=\" font-family:\'Courier New\'; font-size:10pt; font-style:italic; color:#FFFFFF; background-color:transparent;\">- May only be effective in SPECIFIC ENVIRONMENTS</span><span style=\" font-size:10pt; font-style:italic;\"><br /></span></p>\n"
"<p style=\" margin-top:0px; margin-bottom:0px; margin-left:0px; margin-right:0px; -qt-block-indent:0; text-indent:0px; line-height:120%; background-color:transparent;\"><span style=\" font-family:\'Courier New\'; font-size:10pt; font-style:italic; color:#FFFFFF; background-color:transparent;\"> Checkpoint Inhibitors</span></p>\n"
"<p style=\" margin-top:0px; margin-bottom:0px; margin-left:0px; margin-right:0px; -qt-block-indent:0; text-indent:0px; line-height:120%; background-color:transparent;\"><span style=\" font-family:\'Courier New\'; font-size:10pt; font-style:italic; color:#FFFFFF; background-color:transparent;\"> - Removes checkpoint proteins on the surface of cancer cells. </span></p>\n"
"<p style=\" margin-top:0px; margin-bottom:0px; margin-left:0px; margin-right:0px; -qt-block-indent:0; text-indent:0px; line-height:120%; background-color:transparent;\"><span style=\" font-family:\'Courier New\'; font-size:10pt; font-style:italic; color:#FFFFFF; background-color:transparent;\"> - Cancer cells become &quot;visible&quot; to immunity waves.</span></p>\n"
"<p style=\" margin-top:0px; margin-bottom:0px; margin-left:0px; margin-right:0px; -qt-block-indent:0; text-indent:0px;\"><span style=\" font-size:10pt; font-style:italic;\"><br />  </span><span style=\" font-family:\'Courier New\'; font-size:10pt; font-style:italic; color:#FFFFFF; background-color:transparent;\">Monoclonal Antibodies</span></p>\n"
"<p style=\" margin-top:0px; margin-bottom:0px; margin-left:0px; margin-right:0px; -qt-block-indent:0; text-indent:0px; line-height:120%; background-color:transparent;\"><span style=\" font-family:\'Courier New\'; font-size:10pt; font-style:italic; color:#FFFFFF; background-color:transparent;\"> - Adds a “white tracker” on all present cancer cells. </span></p>\n"
"<p style=\" margin-top:0px; margin-bottom:0px; margin-left:0px; margin-right:0px; -qt-block-indent:0; text-indent:0px; line-height:120%; background-color:transparent;\"><span style=\" font-family:\'Courier New\'; font-size:10pt; font-style:italic; color:#FFFFFF; background-color:transparent;\"> - These cells become &quot;visible&quot; to immunity waves. </span></p>\n"
"<p style=\" margin-top:0px; margin-bottom:0px; margin-left:0px; margin-right:0px; -qt-block-indent:0; text-indent:0px; line-height:120%; background-color:transparent;\"><span style=\" font-family:\'Courier New\'; font-size:10pt; font-style:italic; color:#FFFFFF; background-color:transparent;\"> - The cells may also self-destruct.</span><span style=\" font-size:10pt; font-style:italic;\"><br /></span></p>\n"
"<p style=\" margin-top:0px; margin-bottom:0px; margin-left:0px; margin-right:0px; -qt-block-indent:0; text-indent:0px; line-height:120%; background-color:transparent;\"><span style=\" font-family:\'Courier New\'; font-size:10pt; font-style:italic; color:#FFFFFF; background-color:transparent;\"> Bottle of Ginger &amp; Silymarin</span></p>\n"
"<p style=\" margin-top:0px; margin-bottom:0px; margin-left:0px; margin-right:0px; -qt-block-indent:0; text-indent:0px; line-height:120%; background-color:transparent;\"><span style=\" font-family:\'Courier New\'; font-size:10pt; font-style:italic; color:#FFFFFF; background-color:transparent;\"> - Looks suspicious... I\'m not sure I\'d trust it.</span></p>\n"
"<p dir=\'rtl\' style=\" margin-top:0px; margin-bottom:0px; margin-left:0px; margin-right:0px; -qt-block-indent:0; text-indent:0px; line-height:120%; background-color:transparent;\"><span style=\" font-family:\'Courier New\'; font-size:10pt; font-style:italic; color:#FFFFFF; background-color:transparent;\"> </span></p>\n"
"<p dir=\'rtl\' style=\" margin-top:0px; margin-bottom:0px; margin-left:0px; margin-right:0px; -qt-block-indent:0; text-indent:0px; line-height:120%; background-color:transparent;\"><span style=\" font-family:\'Courier New\'; font-size:10pt; font-style:italic; color:#FFFFFF; background-color:transparent;\">              </span><span style=\" font-size:10pt;\">-</span><span style=\" font-family:\'Courier New\'; font-size:10pt; font-style:italic; color:#FFFFFF; background-color:transparent;\">Dr. Trachtenberg&quot;</span></p></body></html>"))
        self.textBrowser.setStyleSheet("border-radius: 5px; background-color: rgba(0,0,0,250)")
        self.label_2.setText(_translate("Form", "It looks like your professor left you some notes..."))
        self.groupBox_3.setTitle(_translate("Form", "Diagnostics"))
        self.label.setText(_translate("Form", "Budget: "))
        self.label_3.setText(_translate("Form", "Next Immunity Wave:"))
        self.label_4.setText(_translate("Form", "Experiment Duration:"))
        self.startTreatment.setText(_translate("Form", "START\n"
" TREATMENT"))
        self.startTreatment_2.setText(_translate("Form", "STOP\n"
"TREATMENT"))
        self.startTreatment.setStyleSheet("border-radius: 5px; border : 1px solid black; margin: 2px")
        self.startTreatment_2.setStyleSheet("border-radius: 5px; border : 1px solid black; margin: 2px")
        self.groupBox_4.setTitle(_translate("Form", "Tissue Imagery"))
        self.groupBox_2.setStyleSheet("border-radius : 5px; background-color : rgba(0,0,0,250); font: 11pt 'Power Green';")
        self.groupBox_3.setStyleSheet("border-radius : 5px; background-color : rgba(0,0,0,250); font: 11pt'Power Green';")
        self.groupBox_4.setStyleSheet("border-radius : 5px; background-color : rgba(0,0,0,250); font: 11pt 'Power Green';")
        Form.setWindowIcon(QIcon("CANCERVGICON.PNG"))



if __name__ == "__main__":
    import sys
    app = QtWidgets.QApplication(sys.argv)
    Form = QtWidgets.QWidget()
    ui = Ui_Form()
    ui.setupUi(Form)
    Form.setWindowTitle("Case 7")
    Form.show()
    sys.exit(app.exec_())