from string import Template

class MyTemplate(Template):
    delimiter = "%"


sentence = """Today we are learning the %language programming language!
              I am learning this for %day days
"""

src = MyTemplate(sentence)

result = src.safe_substitute(
    {
        "language" : "Java",
        "day" : 10
    }
)
print(result)