student_db = {}

def add_student():
    print("\n--- Add New Student ---")
    sid = int(input("Enter Student ID (e.g., 101): "))
    name = input("Enter Student Name: ")
    major = input("Enter Major: ")
    
    # Storing Name and Major as an immutable Tuple
    student_db[sid] = (name, major)
    print(f"Record for {name} added successfully!")

def display_records():
    print("\n--- Current Student Records ---")
    if not student_db:
        print("No records found.")
    else:
        for sid, info in student_db.items():
            name, major = info  # Unpacking the tuple
            print(f"ID: {sid} | Name: {name} | Major: {major}")

# 2. Set Operations (Comparing Clubs/Groups)
def club_analysis():
    print("\n--- Club Membership Analysis ---")
    # Taking multiple inputs and converting to sets
    math_club = set(input("Enter names in Math Club (separated by space): ").split())
    science_club = set(input("Enter names in Science Club (separated by space): ").split())

    print(f"\nStudents in BOTH clubs: {math_club.intersection(science_club)}")
    print(f"All unique students in any club: {math_club.union(science_club)}")
    print(f"Students in Math but NOT Science: {math_club.difference(science_club)}")

# --- Main Execution Loop ---
while True:
    print("\n[1] Add Student [2] Display Records [3] Club Analysis [4] Exit")
    choice = input("Select an option: ")
    
    if choice == '1':
        add_student()
    elif choice == '2':
        display_records()
    elif choice == '3':
        club_analysis()
    elif choice == '4':
        print("Exiting system...")
        break
    else:
        print("Invalid choice, try again.")