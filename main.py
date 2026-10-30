from js import document

def check_grade(*args):
    user_input = document.getElementById("marksInput").value
    
    if user_input == "":
        document.getElementById("outputDiv").innerHTML = "Please enter a valid number"
        return

    marks = float(user_input)
    percentage = (marks / 60) * 100

    if percentage >= 91:
        feedback = "A1"
    elif percentage >= 81:
        feedback = "A2"
    elif percentage >= 71:
        feedback = "B1"
    elif percentage >= 61:
        feedback = "B2"
    elif percentage >= 51:
        feedback = "C1"
    elif percentage >= 41:
        feedback = "C2"
    elif percentage >= 33:
        feedback = "D"
    else:
        feedback = "E"

    result_text = f"Percentage: {round(percentage, 2)}%<br>Feedback: {feedback}"
    document.getElementById("outputDiv").innerHTML = result_text
  
