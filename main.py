class Student:
    # [assignment] Skeleton class. Add your code here
    def __init__(self, name, age, tracks, score):
        self.name = name
        self.age = age
        self.tracks = tracks
        self.score = score 
        
    def change_name(self, change_name):
        self.name = change_name
        
    def change_age(self, change_age):
        self.age = change_age
        
    def add_track(self, add_track):
        self.tracks.append(add_track)

    def get_score(self):
        return self.score 
    
    def show(self):
        print("Name: ", str(self.name))
        print("Age: ", int(self.age))
        print("Tracks: ", str(self.tracks))
        print("Score: ", float(self.score))




Bob = Student(name="Bob", age=26, tracks=["FE","BE"],score=20.90)

Bob.show()

# Expected methods
Bob.change_name("Peter")
Bob.change_age(34)
Bob.add_track("UI/UX")
Bob.get_score()

Bob.show()



