"""Write code using find() and string slicing (see section 6.10) 
to extract the number at the end of the line below. 

Convert the extracted value to a floating point number and print it out."""

text = "X-DSPAM-Confidence:    0.8475"
a = text.find("0.8475")
x = text[a:30]
y = float(x)
print(y)
