from js import document

def check_grade(*args):
    user_input = document.getElementById("marksInput").value
    
    if user_input == "":
        document.getElementById("outputDiv").innerHTML = "Please enter a valid number!"
        return

    marks = float(user_input)
    percentage = (marks / 60) * 100

    if percentage >= 90:
        feedback = "Outstanding performance!"
    elif percentage >= 75:
        feedback = "Great job, keep it up!"
    elif percentage >= 50:
        feedback = "Good effort, but you can do better."
    else:
        feedback = "Need serious improvement!"

    result_text = f"Percentage: {round(percentage, 2)}%<br>Feedback: {feedback}"
    document.getElementById("outputDiv").innerHTML = result_text
  
