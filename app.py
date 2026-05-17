from flask import Flask, render_template, request

app = Flask(__name__)

@app.route("/", methods=["GET", "POST"])
def home():

    FinalGPA = None

    if request.method == "POST":

        gradesList = []
        GPA_grade = []
        count = 0
        count2 = 0
        total = 0

        grades_input = request.form["grades"]
        boolean = request.form["honors"]

        gradesList = [int(x.strip()) for x in grades_input.split(",")]

        num_courses = len(gradesList)

        def convert(number):
            minus = 0
            newgrade = 100-number

            for i in range(newgrade):
                minus += 0.1

            if boolean.lower() == "yes" or boolean.lower() == "ye" or boolean.lower() == "y":
                finalGpa = 6-minus
                finalGpa = float(finalGpa)
                return finalGpa

            elif boolean.lower() == "no" or boolean.lower() == "nah" or boolean.lower() == "n":
                finalGpa = 5-minus
                finalGpa = float(finalGpa)
                return finalGpa

        def printGPA(totalGPA):
            length = len(gradesList)
            FinalGPA = totalGPA/length
            return FinalGPA

        for i in range(num_courses):
            GPA = convert(gradesList[count])
            GPA_grade.append(GPA)
            count += 1

        for grades in gradesList:

            grade = GPA_grade[count2]

            if grade >= 3.0:
                total += grade
            else:
                total += 0

            count2 += 1

        FinalGPA = printGPA(total)

    return render_template("index.html", gpa=FinalGPA)

import os

if __name__ == "__main__":
    port = int(os.environ.get("PORT", 5000))
    app.run(host="0.0.0.0", port=port)