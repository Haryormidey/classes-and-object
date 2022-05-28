class Student:
    # [assignment] Skeleton class. Add your code here
    def __init__(self, name, age, tracks, score):
        self.name = str(name)
        self.age = int(age)
        self.track = list(tracks)
        self.score = float(score )
    #method
    def change_name(self, new_name):
        self.new_name = new_name
        return self.new_name
        #print ("This is the changed name: ", new_name)

    def change_age(self, new_age):
        self.new_age = new_age
        return self.new_age
        #print ("This is the changed age: ", new_age)

    def add_track(self, tracks):
        self.track.append(tracks)
        return self.track
        #print ("This is the new track: ", track)

    def get_score(self):
        return self.score
        #print ("This is the score: ", self.score)


Bob = Student(name="Bob", age=26, tracks=["FE","BE"],score=20.90)

# Expected methods
print ("This is the changed name: ",Bob.change_name("Peter"))
print("This is the changed age: " ,Bob.change_age(34))
print("These are the tracks: ", Bob.add_track("UI/UX"))
print("This is the score: ", Bob.get_score())
