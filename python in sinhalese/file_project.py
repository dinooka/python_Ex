lines = None
with open('marks.txt') as r_file:
    lines = r_file.readlines()

if not lines:
    print("file reading failed")
    exit()

header_line = lines[:1]
marks_lines = lines[1:]
# print(marks_lines)
# print(len(marks_lines))

def get_top_std(subject : str, dataset : dict):
    max_marks = 0
    max_std = ""

    for name,marks in dataset.items():
        if max_marks < marks : 
            max_marks = marks            
            max_std = name

    # print(max_std, subject,max_marks)
    return max_std, subject,max_marks 

subject_marks = {}
std_marks = {}

for line in marks_lines:
    entries = line.split(',')
    # print(entries)
    name = entries[0].strip()   
    subject = entries[1].strip()   
    marks = int(entries[2].strip())      

    if subject not in subject_marks:
        subject_marks[subject] = {}

    subject_marks[subject][name] = marks
    
    prev_marks = std_marks.get(name,0)
    std_marks[name] = prev_marks + marks


for subject,dataset in subject_marks.items():
    name, sub, marks = get_top_std(subject,dataset)
    msg = f"Top student for {sub} is {name} with {marks} marks."
    print(msg)

# print(std_marks)


marks_list = [(name,marks) for name,marks in std_marks.items()]

# def get_marks(record:tuple):
#     return record[1]
get_marks = lambda record : record[1]

marks_list.sort(key=get_marks,reverse=True)
top = marks_list[0]
print(f"Top student for all subjects is {top[0]} with {top[1]} marks.")

# print(subject_marks)