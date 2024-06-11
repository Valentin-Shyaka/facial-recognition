import cv2
import psycopg2

# # Function to recognize faces and predict UID
def recognize_face(image):
    # Your face recognition code here, which should return the predicted UID
    predicted_uid = predict_uid(image)
    return predicted_uid

# Function to fetch full name from the database based on UID
def get_full_name(uid):
    #Connect to PostgreSQL database
    conn = psycopg2.connect(
        dbname="facial",
        user="postgres",
        password="vava635",
        host="localhost",
        port="5432"
    )

    # Create a cursor object
    cur = conn.cursor()

    # Query the database to fetch full name based on UID
    cur.execute("SELECT fullname FROM people WHERE uid = %s", (uid,))
    full_name = cur.fetchone()[0]

    # Close cursor and connection
    cur.close()
    conn.close()

    if full_name:
        print("Name was found "+ full_name)
    else:
        print("name not found "+ full_name)

    return full_name

get_full_name(1)
# # Function to display the full name of the recognized person
def display_recognized_person(full_name):
    print("Recognized person:", full_name)

# # Main function
def main():
    # Load image containing a face
    image = cv2.imread("image_with_face.jpg")

    # Recognize face and predict UID
    predicted_uid = recognize_face(image)

    # Fetch full name from the database based on UID
    full_name = get_full_name(predicted_uid)

    # Display the full name of the recognized person
    display_recognized_person(full_name)

if __name__ == "__main__":
    main()