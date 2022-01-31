def arithmetic_arranger(problems, displayAnswer=False):
  # setup variables
  arranged_problems = ''
  permittedOperators = ['+', '-']
  line_topOperands = ''
  line_operatorsAndBottomOperands = ''
  line_dashes = ''
  line_answers = ''
  firstProblem = True

  # return Error if the number of problems given is greater than 5
  if len(problems) > 5: return "Error: Too many problems."

  # separate each problem's string into [operand, operator, operand] and store each set in a list
  challenges = list(map(lambda x: x.split(), problems))

  # iterate through each problem and validate data
  for challenge in challenges:
    # return Error if any of the operators are not a permitted operator
    if not any(item in permittedOperators for item in challenge[1]): return "Error: Operator must be '+' or '-'."
    # return Error if any of the operands are not digits (0-9)
    if not all(item.isdecimal() for item in [challenge[0], challenge[2]]): return "Error: Numbers must only contain digits."
    # return Error if any of the operands are greater than four numbers
    if not all(len(item) <= 4 for item in [challenge[0], challenge[2]]): return "Error: Numbers cannot be more than four digits."

    # data has been validated, now perform the operation and format it
    spaceAdjustment = max(len(challenge[0]), len(challenge[2])) + 2
    problemSpacing = '' if firstProblem else ' ' * 4
    line_topOperands += problemSpacing + challenge[0].rjust(spaceAdjustment)
    line_operatorsAndBottomOperands += problemSpacing + challenge[1] + challenge[2].rjust(spaceAdjustment-1)
    line_dashes += problemSpacing + '-' * spaceAdjustment
    line_answers += problemSpacing + str(eval(''.join(challenge))).rjust(spaceAdjustment)
    firstProblem = False

  arranged_problems = line_topOperands + '\n' + line_operatorsAndBottomOperands + '\n' + line_dashes
  if displayAnswer == True: arranged_problems += '\n' + line_answers

  return arranged_problems