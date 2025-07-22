from capture_faces import capture_images
from gen_encoding import generate_encodings
from detect_attendence import mark_attendance_with_face
from attendence_on_email import send_attendence_email

def main():
    print("********** Welcome to F-AI ATTENDANCE ***********")
    
    while True:
        print("\nSelect the option you want to perform:")
        print("1. Register a new student")
        print("2. Mark attendance")
        print("3. Send Attendance Report via Email")
        print("4. Exit")

        option = input("Enter your choice (1-4): ")

        if option == "1":
            capture_images()
            generate_encodings()
        elif option == "2":
            mark_attendance_with_face()
        elif option == "3":
            send_attendence_email()
        elif option == "4":
            print("Exiting the system. Goodbye!")
            break
        else:
            print("❌ Invalid choice. Please try again.")

if __name__ == "__main__":
    main()
