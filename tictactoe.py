import streamlit as st

def calculate(expression):
  """
  Calculates the expression using eval.

  Args:
      expression: The mathematical expression to calculate.

  Returns:
      The result of the calculation or None if there's an error.
  """
  try:
    return eval(expression)
  except:
    return None

st.title("Simple Calculator")

# Input field for expression
expression = st.text_input("Enter expression:")

# Calculate button
if st.button("Calculate"):
  # Calculate the expression and display the result
  result = calculate(expression)
  if result is not None:
    st.write(f"Result: {result}")
  else:
    st.error("Invalid expression")
