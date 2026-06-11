students = [
    {"name": "Alice", "scores": [92, 88, 95]},
    {"name": "Bob", "scores": [60, 55, 58]},
    {"name": "Carol", "scores": [78, 82, 74]},
    {"name": "David", "scores": [95, 98, 100]},
    {"name": "Eve", "scores": [40, 45, 38]},
]

def process(s):
    r = []
    for x in s:
        t = 0
        for n in x["scores"]:
            t += n
        a = t / len(x["scores"])
        if a >= 90:
            g = "A"
        elif a >= 80:
            g = "B"
        elif a >= 70:
            g = "C"
        elif a >= 60:
            g = "D"
        else:
            g = "F"
        if g == "F":
            st = "Fail"
        else:
            st = "Pass"
        r.append({"name": x["name"], "average": a, "grade": g, "status": st})
    return r

def show(r):
    for x in r:
        print(x["name"] + " | Avg: " + str(round(x["average"], 2)) + " | Grade: " + x["grade"] + " | " + x["status"])

show(process(students))