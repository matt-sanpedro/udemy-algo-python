# the use of f-strings
name = "Bob"
# create the template
greeting = f"Hello, {name}"
with_name = greeting.format(name)
print(with_name)

# creating a template for printing
greeting_template = "Hello, {}"

# first name
name = "Kendrick"
with_name = greeting_template.format(name)
print(with_name)

# second name
name = "Frodo"
print(greeting_template.format(name))

# format enables longer templates with many place holders
long_greeting = "Hello, {}.  Today is {}."
format_long_greeting = long_greeting.format(name, "Saturday")
print(format_long_greeting)
