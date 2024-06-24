import sys
import os
import pandas as pd
from PyQt5.QtWidgets import QApplication, QMainWindow, QTableWidget, QTableWidgetItem, QVBoxLayout, QWidget, QLabel, QPushButton, QMessageBox

class UnemploymentApp(QMainWindow):
    def __init__(self):
        super().__init__()

        self.setWindowTitle("Unemployment Data Viewer")
        self.setGeometry(100, 100, 800, 600)

        # Central widget
        self.central_widget = QWidget()
        self.setCentralWidget(self.central_widget)

        # Layout
        self.layout = QVBoxLayout()
        self.central_widget.setLayout(self.layout)

        # Labels
        self.label1 = QLabel("Data from 'unemployment in India.csv':")
        self.layout.addWidget(self.label1)

        # Table 1
        self.unemployment_table1 = QTableWidget()
        self.layout.addWidget(self.unemployment_table1)

        # Label for second table
        self.label2 = QLabel("Data from 'Unemployment_Rate_upto_11_2020.csv':")
        self.layout.addWidget(self.label2)

        # Table 2
        self.unemployment_table2 = QTableWidget()
        self.layout.addWidget(self.unemployment_table2)

        # Button to load data
        self.load_data_button = QPushButton("Load Data")
        self.load_data_button.clicked.connect(self.load_data)
        self.layout.addWidget(self.load_data_button)

    def load_csv(self, filename, table_widget):
        try:
            data = pd.read_csv(filename)

            table_widget.setRowCount(data.shape[0])
            table_widget.setColumnCount(data.shape[1])
            table_widget.setHorizontalHeaderLabels(data.columns)

            for i in range(data.shape[0]):
                for j in range(data.shape[1]):
                    table_widget.setItem(i, j, QTableWidgetItem(str(data.iloc[i, j])))

        except Exception as e:
            QMessageBox.critical(self, "Error", f"Failed to load {filename}: {str(e)}")

    def load_data(self):
        try:
            # Get the absolute path of the current script
            current_dir = os.path.dirname(os.path.abspath(__file__))

            # Absolute paths to your CSV files
            file1 = os.path.join(current_dir, 'unemployment in India.csv')
            file2 = os.path.join(current_dir, 'Unemployment_Rate_upto_11_2020.csv')

            # Load data into tables
            self.load_csv(file1, self.unemployment_table1)
            self.load_csv(file2, self.unemployment_table2)

        except Exception as e:
            QMessageBox.critical(self, "Error", f"Failed to load data: {str(e)}")

if __name__ == "__main__":
    app = QApplication(sys.argv)
    window = UnemploymentApp()
    window.show()
    sys.exit(app.exec_())
