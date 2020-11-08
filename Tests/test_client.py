import unittest
import Client
import sys
from PyQt5.QtTest import QTest
from PyQt5 import QtGui, QtCore

app = QtGui.QGuiApplication(sys.argv)
ui = Client.AppWindow()


class TestClient(unittest.TestCase):

    def test_lambda(self):
        # Test if the Lambda lineEdit accepts characters besides digits.
        # Arrange
        text = "123abc"
        expected_result = "123"

        # Act
        QTest.keyClicks(ui.lambda_value, text)

        # Assert
        self.assertEqual(expected_result, ui.lambda_value.text())

    def test_sigma(self):
        # Test if the Sigma lineEdit accepts characters besides digits.
        # Arrange
        text = "123abc"
        expected_result = "123"

        # Act
        QTest.keyClicks(ui.sigma_value, text)

        # Assert
        self.assertEqual(expected_result, ui.sigma_value.text())

    def test_m(self):
        # Test if the M lineEdit accepts characters besides digits.
        # Arrange
        text = "123abc"
        expected_result = "123"

        # Act
        QTest.keyClicks(ui.m_value, text)

        # Assert
        self.assertEqual(expected_result, ui.m_value.text())

    def test_w(self):
        # Test if the W lineEdit accepts characters besides digits.
        # Arrange
        text = "123abc"
        expected_result = "123"

        # Act
        QTest.keyClicks(ui.w_value, text)

        # Assert
        self.assertEqual(expected_result, ui.w_value.text())

    def test_l1(self):
        # Test if the L1 lineEdit accepts characters besides digits.
        # Arrange
        text = "123abc"
        expected_result = "123"

        # Act
        QTest.keyClicks(ui.l1_value, text)

        # Assert
        self.assertEqual(expected_result, ui.l1_value.text())

    def test_l2(self):
        # Test if the L2 lineEdit accepts characters besides digits.
        # Arrange
        text = "123abc"
        expected_result = "123"

        # Act
        QTest.keyClicks(ui.l2_value, text)

        # Assert
        self.assertEqual(expected_result, ui.l2_value.text())

    def test_choose_file(self):
        # Test if the choose file button is handled once it's clicked
        # Arrange
        expected_result = True

        # Act
        QTest.mouseClick(ui.choose_file_button, QtCore.Qt.LeftButton)

        # Assert
        self.assertEqual(expected_result, ui.choose_file_isClicked)

    def test_start(self):
        # Test if the choose file button is handled once it's clicked
        # Arrange
        expected_result = True

        # Act
        QTest.mouseClick(ui.start_button, QtCore.Qt.LeftButton)

        # Assert
        self.assertEqual(expected_result, ui.start_isClicked)

    def test_export(self):
        # Test if the choose file button is handled once it's clicked
        # Arrange
        expected_result = True

        # Act
        QTest.mouseClick(ui.export_button, QtCore.Qt.LeftButton)

        # Assert
        self.assertEqual(expected_result, ui.export_isClicked)

    def test_file_name(self):
        # Test if the QLineEdit that contains the file name is ReadOnly
        # Arrange
        text = "123abc"
        expected_result = ""

        # Act
        QTest.keyClicks(ui.file_name, text)

        # Assert
        self.assertEqual(expected_result, ui.file_name.text())

    def test_hash_combobox(self):
        # Test if the hash combobox contains the correct elements
        # Arrange
        expected_result = 3
        expected_list = ["MD5", "SHA1", "SHA256"]

        # Act
        all_items = [ui.hash_combobox.itemText(i) for i in range(ui.hash_combobox.count())]

        # Assert
        self.assertEqual(expected_result, ui.hash_combobox.count())
        self.assertEqual(expected_list, all_items)

    def test_prf_combobox(self):
        # Test if the prf combobox contains the correct elements
        # Arrange
        expected_result = 2
        expected_list = ["PRF1", "PRF2"]

        # Act
        all_items = [ui.prf_combobox.itemText(i) for i in range(ui.prf_combobox.count())]

        # Assert
        self.assertEqual(expected_result, ui.prf_combobox.count())
        self.assertEqual(expected_list, all_items)

    def test_ot_combobox(self):
        # Test if the ot combobox contains the correct elements
        # Arrange
        expected_result = 2
        expected_list = ["OTMultiPoint", "OTRandomOracle"]

        # Act
        all_items = [ui.ot_combobox.itemText(i) for i in range(ui.ot_combobox.count())]

        # Assert
        self.assertEqual(expected_result, ui.ot_combobox.count())
        self.assertEqual(expected_list, all_items)


if __name__ == '__main__':
    unittest.main()

