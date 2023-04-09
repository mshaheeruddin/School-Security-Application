import sqlite3
import pyzbar.pyzbar as pyzbar
import cv2
from frontend import verificationScreen

def qrscan():
    # Open a connection to the SQLite database
    conn = sqlite3.connect('../database/school.db')

    # Initialize the video stream
    cap = cv2.VideoCapture(0)

    while True:
        # Capture the current frame from the video stream
        ret, frame = cap.read()

        # Read the QR code from Parents
        decoded = pyzbar.decode(frame)
        if decoded:
            student_id = decoded[0].data.decode()

            # Query the database for the student's information
            result = conn.execute("SELECT first_name FROM student WHERE student_id = ?", [student_id]).fetchone()
            if result is not None:
                return True
                break
        # Display the current frame
        cv2.imshow('QR Scanner', frame)

        # Exit if the 'q' key is pressed
        if cv2.waitKey(1) & 0xFF == ord('q'):
            break

    # Release the video stream and close the window
    cap.release()
    cv2.destroyAllWindows()

    return False


