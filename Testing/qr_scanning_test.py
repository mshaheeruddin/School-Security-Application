import unittest
from unittest.mock import MagicMock, patch
import sqlite3
import pyzbar.pyzbar as pyzbar
import cv2

from controller.QrScanning import qrscan
from frontend import verificationScreen


class TestQRScanner(unittest.TestCase):

    def test_qrscan(self):
        # Define a mock SQLite database connection
        conn = sqlite3.connect(':memory:')
        cursor = conn.cursor()
        cursor.execute("CREATE TABLE student (first_name TEXT, student_id TEXT)")
        cursor.execute("INSERT INTO student (first_name, student_id) VALUES (?, ?)", ('John', 'S001'))

        # Define a mock video stream and a mock decoded QR code
        cap_mock = MagicMock()
        decoded_mock = [MagicMock(b'S001')]

        with patch('cv2.VideoCapture') as cap:
            cap.return_value = cap_mock
            with patch('pyzbar.pyzbar.decode') as decoded:
                decoded.return_value = decoded_mock

                # Test that the function returns True when a valid QR code is scanned
                with patch('cv2.imshow') as imshow:
                    self.assertTrue(qrscan(conn))
                    imshow.assert_called()

                # Test that the function returns False when an invalid QR code is scanned
                decoded_mock = [MagicMock(b'S002')]
                decoded.return_value = decoded_mock
                with patch('cv2.imshow') as imshow:
                    self.assertFalse(qrscan(conn))
                    imshow.assert_called()