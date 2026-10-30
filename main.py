from js import document

def check_grade(*args):
    user_input = document.getElementById("marksInput").value
    
    if user_input == "":
        document.getElementById("outputDiv").innerHTML = "Please enter a valid number"
        return

    marks = float(user_input)
    percentage = (marks / 60) * 100

    if percentage >= 91:
        grade = "A1"
    elif percentage >= 81:
        grade = "A2"
    elif percentage >= 71:
        grade = "B1"
    elif percentage >= 61:
        grade = "B2"
    elif percentage >= 51:
        grade = "C1"
    elif percentage >= 41:
        grade = "C2"
    elif percentage >= 33:
        grade = "D"
    else:
        grade = "E"

    result_text = f"Percentage: {round(percentage, 2)}%<br>Grade: {grade}"
    document.getElementById("outputDiv").innerHTML = result_text
  
