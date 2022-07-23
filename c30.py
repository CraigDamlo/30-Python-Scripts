# Define a list of participants
participant = ['Mona Lisa', 'Akbar Hossain', 'Jakir Hasan', 'Zahadur Rahman', 'Zenifer Lopez']
# Define the function to filters selected candidates
def SelectedPerson(participant):
    selected = ['Akbar Hossain', 'Zillur Rahman', 'Mona Lisa']
    if(participant in selected):
        return True
selectedList = filter(SelectedPerson, participant)
print('The selected candidates are:')
for candidate in selectedList:
    print(candidate)
