class Solution:
    def countStudents(self, students: List[int], sand: List[int]) -> int:
        i=0
        n=len(students)
        while students and i<n:
            if students[0]==sand[0]:
                students.pop(0)
                sand.pop(0)
                # i+=1
                i=0
            else:
                students.append(students.pop(0))
                i+=1
        return (len(students))
