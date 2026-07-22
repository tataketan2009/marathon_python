if __name__ == '__main__':
    n = int(input())
    student_marks = {}
    for _ in range(n):
        parts = input().split()          
        name = parts[0]                  
        scores = list(map(float, parts[1:]))  
        student_marks[name] = scores
    query_name = input()

    marks = student_marks[query_name]
    average = sum(marks) / len(marks)    
    print(f"{average:.2f}")              