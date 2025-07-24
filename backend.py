# backend.py
attendance_list = []

def mark_attendance(name):
    attendance_list.append(name)
    print(f"{name} marked present.")

# Example usage
mark_attendance("Gayathri")
