



NoInGroup = []


GroupName =input("what is the name of the group?")
NoOfPupils = int(input("how many people are in " + GroupName + "?:"))
for counter in range(NoOfPupils):
    counter += 1
    PupilName = input("what is the name of the pupil?" +str(counter))
    NoInGroup.append(PupilName)

    for counter in range(len(NoInGroup)):
      print(NoInGroup[counter])
      
