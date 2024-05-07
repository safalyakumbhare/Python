#!/usr/bin/env python
import cgi

# Parse form data
form = cgi.FieldStorage()

# Get field values
field1 = form.getvalue('field1')
field2 = form.getvalue('field2')

# Print field values
print("Content-type: text/html\n")
print("<html>")
print("<head>")
print("<title>Form Submission Result</title>")
print("</head>")
print("<body>")
print("<h2>Form Submission Result</h2>")
print("<p>Field 1: {}</p>".format(field1))
print("<p>Field 2: {}</p>".format(field2))
print("</body>")
print("</html>")
