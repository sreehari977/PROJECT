students=[]
def add(name, grade):
    students.append({'name': name, 'grade': grade})
def display():
    if not students:
        print("No students to display.")
        return
    for i in students:
        print(f"Name: {i['name']}, Grade: {i['grade']}")
def search(name):
    if not students:
        print("No students to search.")
        return
    for i in students:
        if i['name'].lower()==name.lower():
            print(f"Name: {i['name']}, Grade: {i['grade']}")
def sort():
    if not students:
        print("No students to sort.")
        return
    grade_weights={"S": 5, "A": 4, "B": 3, "C": 2, "D": 1, "F": 0}
    lst =list(students)
    for i in range(len(lst)):
        for j in range (len(lst)-i-1):
            l1=lst[j]['grade'].upper()
            l2=lst[j+1]['grade'].upper()
            g1=grade_weights[l1]
            g2=grade_weights[l2]
            if g1<g2:
                lst[j],lst[j+1]=lst[j+1],lst[j]
    print("\n---Leaderboard---")
    for i in lst:
        print(f"Name: {i['name']}, Grade: {i['grade']}")
while True:
    print("\n---Student performance tracker---")
    print("1. Add student")
    print("2. View students")
    print("3. Search students") 
    print("4. Sort students")
    print("5. Exit")
    choice = input("Enter your choice: ")
    if choice == '1':
        name = input("Enter student name: ")
        grade = input("Enter student grade: ").upper()
        add(name, grade)
        print(f"Student {name} with grade {grade} added successfully.")
    elif choice == '2':
        print("Displaying all students...")
        display()
    elif choice == '3':
        search_name = input("Enter student name to search: ")
        print(f"Searching for student {search_name}...")
        search(search_name)
    elif choice == '4':
        print("Sorting students by grade...")
        sort()
    elif choice == '5':
        print("Exiting the program. Goodbye!")
        break
    else:
        print("Invalid choice. Please try again.")    
