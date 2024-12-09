class Student:  
    def __init__(self, name):  
        self.name = name  
        self.clubs = []  # List to store clubs the student is a member of  

    def join_club(self, club):  
        if club not in self.clubs:  
            self.clubs.append(club)  
            club.add_member(self)  # Add this student to the club's member list  
            print(f"{self.name} has joined the {club.name} club.")  
        else:  
            print(f"{self.name} is already a member of the {club.name} club.")  

    def list_clubs(self):  
        if self.clubs:  
            print(f"{self.name} is a member of the following clubs:")  
            for club in self.clubs:  
                print(club.name)  
        else:  
            print(f"{self.name} is not a member of any clubs.")  

    def __str__(self):  
        return self.name  


class Club:  
    def __init__(self, name):  
        self.name = name  
        self.members = []  # List to store members of the club  

    def add_member(self, student):  
        if student not in self.members:  
            self.members.append(student)  
        else:  
            print(f"{student.name} is already a member of the {self.name} club.")  

    def display_members(self):  
        if self.members:  
            print(f"Members of the {self.name} club:")  
            for member in self.members:  
                print(member.name)  
        else:  
            print(f"The {self.name} club has no members.")  

    def list_students(self):  
        return [str(member) for member in self.members]  

    def __str__(self):  
        return self.name  


# Example usage  
# Creating clubs  
club_football = Club("Football")  
club_dance = Club("Dance")  
club_science = Club("Science")  

# Creating students  
student1 = Student("Milly")  
student2 = Student("Mark")  
student3 = Student("Brian")  

# Students joining clubs  
student1.join_club(club_football)  
student1.join_club(club_dance)  
student2.join_club(club_football)  
student3.join_club(club_science)  

# Displaying club members  
club_football.display_members()  
club_dance.display_members()  
club_science.display_members()  

# Listing clubs for a student  
student1.list_clubs()  
student2.list_clubs()  

# Checking if students are members of a specific club  
print(f"{student1.name} is a member of: {[club.name for club in student1.clubs]}")  
print(f"{club_football.name} has the following members: {[str(member) for member in club_football.members]}")