class Member:  
    def __init__(self, name):  
        self.name = name  

    def __str__(self):  
        return self.name  


class Team:  
    def __init__(self, name):  
        self.name = name  
        self.team_members = []  # List to store members of the team  

    def add_member(self, member):  
        if member not in self.team_members:  
            self.team_members.append(member)  
            print(f"{member.name} has been added to the {self.name} team.")  
        else:  
            print(f"{member.name} is already a member of the {self.name} team.")  

    def display_members(self):  
        if self.team_members:  
            print(f"Members of the {self.name} team:")  
            for member in self.team_members:  
                print(member)  
        else:  
            print(f"The {self.name} team has no members.")  

    def __str__(self):  
        return self.name  


class Project:  
    def __init__(self, name):  
        self.name = name  
        self.teams = []  # List to store teams assigned to the project  

    def add_team(self, team):  
        if team not in self.teams:  
            self.teams.append(team)  
            print(f"The {team.name} team has been added to the {self.name} project.")  
        else:  
            print(f"The {team.name} team is already assigned to the {self.name} project.")  

    def members_in_project(self):  
        """Returns a set of unique members across all teams in the project."""  
        unique_members = set()  
        for team in self.teams:  
            unique_members.update(team.team_members)  
        return unique_members  

    def display_members(self):  
        """Display all unique members of the project."""  
        unique_members = self.members_in_project()  
        if unique_members:  
            print(f"Unique members involved in the {self.name} project:")  
            for member in unique_members:  
                print(member)  
        else:  
            print(f"There are no members assigned to the {self.name} project.")  

    def total_unique_members_count(self):  
        """Return the total count of unique members across all teams in the project."""  
        return len(self.members_in_project())  

    def __str__(self):  
        return self.name  


# Example usage  
# Creating members  
member1 = Member("Eugene")  
member2 = Member("Bradley")  
member3 = Member("Anthony")  
member4 = Member("Theo")  

# Creating teams  
team_alpha = Team("Alpha")  
team_beta = Team("Beta")  

# Adding members to teams  
team_alpha.add_member(member1)  
team_alpha.add_member(member2)  
team_alpha.add_member(member1)  # Should give a message that Alice is already a member  

team_beta.add_member(member3)  
team_beta.add_member(member4)  

# Creating a project  
project_x = Project("Project X")  

# Assigning teams to the project  
project_x.add_team(team_alpha)  
project_x.add_team(team_beta)  

# Displaying members in the project  
project_x.display_members()  

# Total unique members count in the project  
print(f"Total unique members in '{project_x.name}': {project_x.total_unique_members_count()}")  

# Adding a member to a team that's already a member in another team  
team_alpha.add_member(member3)  # Alice from Alpha and Charlie from Beta can be in multiple teams  

# Final output displaying the members of each team  
team_alpha.display_members()  
team_beta.display_members()