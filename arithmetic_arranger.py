def arithmetic_arranger(problems, displayAnswer=False):
  num1List = []
  num2List = []
  operatorList = []
  answersList = []
  if len(problems) > 5:
    return "Error: Too many problems."
  for problem in problems:
    problemSplit = problem.split()
    operator = problemSplit[1]
    num1 = problemSplit[0]
    num2 = problemSplit[2]
    if operator=='+' or operator=='-':
      if num1.isdecimal() and num2.isdecimal():
        if len(num1) <= 4 and len(num2) <= 4:
          num1List.append(num1)
          num2List.append(num2)
          operatorList.append(operator)
          answersList.append(str(int(num1)+int(num2)) if operator=='+' else str(int(num1)-int(num2)))
        else:
          return "Error: Numbers cannot be more than four digits."
      else:
          return "Error: Numbers must only contain digits."
    else:
      return "Error: Operator must be '+' or '-'."
  # arrange the problems
  line1=''
  line2=''
  line3=''
  line4=''
  problemSpacing=''
  for i in range(len(num1List)):
    if i == 1:
      problemSpacing = '    '
    adjustment = len(num2List[i])+2 if len(num2List[i]) > len(num1List[i]) else len(num1List[i])+2
    line1 += problemSpacing + num1List[i].rjust(adjustment)
    line2 += problemSpacing + operatorList[i] + ' ' + num2List[i].rjust(adjustment-2)
    line3 += problemSpacing + '-' * adjustment
    line4 += problemSpacing + answersList[i].rjust(adjustment)

  arranged_problems = line1 + '\n' + line2 + '\n' + line3
  if displayAnswer == True:
    arranged_problems += '\n' + line4
    
  return arranged_problems