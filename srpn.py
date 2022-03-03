"""SRPN ADVANCED CALCULATOR"""

numbers = set('0123456789')
random_List = [1804289383, 846930886, 1681692777, 1714636915, 1957747793,
              424238335, 719885386, 1649760492, 596516649,1189641421,
              1025202362,1350490027,783368690,1102520059,2044897763,
              1967513926,1365180540,1540383426,304089172,1303455736,
              35005211,521595368]
random_Index=0
stackNum = []

def format_result(result_to_Format):
    """This function format the results based on the Saturation point."""
    if result_to_Format is not None:
        if int(result_to_Format) != 0:
            if int(result_to_Format) > 2147483647:
                result_to_Format = 2147483647
            elif int(result_to_Format) < -2147483648:
                result_to_Format = -2147483648
    return int(result_to_Format)

def isNum(s):
    """This function return true if its a number, false if its an operator."""
    try:
        float(s)
    except Exception:
        return False
    else:
        return True

def perform_calc(string, num1, num2):
    """This function returns the value after the operation."""
    if num1==0 and len(stackNum)>0:
        num1=float(stackNum.pop())
    if string == '+':
        output_value = num1+num2
    elif string == '-':
        output_value = num1-num2
    elif string == '*':
        output_value = num1*num2
    elif string == '/':
        output_value = num1/num2
    elif string == '%':
        output_value = num1 % num2
    elif string == '^':
        if num2<0:
            print('Negative power.')
            return None
        else:
            output_value = pow(num1, num2)
    else:
        output_value = 0
    return int(output_value)

def is_numbers(s):
    """This function returns the number value."""
    return s in numbers

def get_number(cmdStr):
    """This function returns the number and its length."""
    if cmdStr[0] !='=':
        try:
            f = ""
            if (len(cmdStr)>0 and cmdStr[0] == '-'):
                f += "-"
                cmdStr = cmdStr[1:]
            for c in cmdStr:
                if not is_numbers(c):
                    break
                f += c
            return (int(f), len(f),True)
        except Exception:
            return (0,0, False)

def split_ops_Oprnd(command):
    """This function returns the list after seperating
    operation and operands"""
    linecmd=[]
    num=''
    i=0
    for c in command:
        if i==0 and c == '-':
            num += "-"
        elif isNum(c):
            num+=c
        elif c == " ":
            if num !='':
                linecmd.append(num)
                num = ''
        elif c =='-':
            if command[i-1]==' ' or command[i-1]=='-':
                num += c
            else:
                if num != '':
                    linecmd.append(num)
                    num = ''
                linecmd.append(c)
        else:
            if num != '':
                linecmd.append(num)
                num = ''
            linecmd.append(c)
        i+=1
    return linecmd

def process_command(command):
    """This function triggers up on user
    entering value one by one after enter."""
    global random_Index
    if command == 'd':
        if len(stackNum)>0:
            for dResult in stackNum:
                print(format_result(dResult))
        else:
            print(format_result(-2147483648))
        return None
    elif command == '=':
        if len(stackNum)>0:
            print(format_result(stackNum[len(stackNum)-1]))
        else:
            print('Stack empty.')
        return None
    elif isNum(command):
        if len(stackNum) < 23:
            stackNum.append(format_result(int(command)))
        else:
            print('Stack overflow.')
    elif command.replace(" ", "").isalpha():
        command=command.replace(" ", "")
        for i in command:
            if i == 'd':
                if len(stackNum) > 0:
                    for dResult in stackNum:
                        print(format_result(dResult))
                else:
                    print(format_result(-2147483648))
            elif i=='r':
                if len(stackNum) < 23:
                    stackNum.append(format_result
                                    (int(random_List[random_Index])))
                    random_Index += 1
                else:
                    print('Stack overflow.')
            else:
                print('Unrecognised operator or operand "{}"'.format(i))
    elif command in ('+', '-', '*', '/', '%', '^'):
        if len(stackNum)>1:
            try:
                number2 = float(stackNum.pop())
                number1 = float(stackNum.pop())
                output = perform_calc(command, number1, number2)
                if len(stackNum) < 23 and output is not None:
                    stackNum.append(format_result(int(output)))
                elif output is not None:
                    print('Stack overflow.')
                elif command == '^' and output is None:
                    stackNum.append(format_result(int(number1)))
                    stackNum.append(format_result(int(number2)))
            except ZeroDivisionError:
                print('Divide by 0.')
            except Exception as e:
                print('process_calc_line', e)
        else:
            print('Stack underflow.')
        return None
    elif ' ' in command:
        if len(command) > 0:
            lineCmd=split_ops_Oprnd(command)
            if len(lineCmd) > 0:
                i=0
                next_no_used = False
                for element in lineCmd:
                    if isNum(element) and next_no_used is False:
                        if len(stackNum) < 23:
                            stackNum.append(format_result(int(element)))
                            printnum = element
                        else:
                            print('Stack overflow.')
                    elif isNum(element) is False and element!="=":
                        if len(stackNum)<2:
                            if element.count('=') != len(element):
                                if isNum(lineCmd[i+1]):
                                    number2 = float(lineCmd[i+1])
                                    next_no_used = True
                                    number1 = float(stackNum.pop())
                                    output = \
                                        perform_calc(element, number1, number2)
                                    if len(stackNum) < 23 and \
                                            output is not None:
                                        stackNum.append(format_result
                                                        (int(output)))
                                    elif output is not None:
                                        print('Stack overflow.')
                                    elif command == '^' \
                                            and output is None:
                                        stackNum.append(format_result
                                                        (int(number1)))
                                        stackNum.append(format_result
                                                        (int(number2)))
                                else:
                                    print('Stack underflow.')
                            else:
                                for i in element:
                                    try:
                                        print(format_result(output))
                                    except NameError:
                                        print(format_result(printnum))
                        else:
                            try:
                                number2 = float(stackNum.pop())
                                next_no_used = False
                                number1 = float(stackNum.pop())
                                if len(element)<2:
                                    output = \
                                        perform_calc(element, number1, number2)
                                    if len(stackNum) < 23 and \
                                            output is not None:
                                        stackNum.append(format_result
                                                        (int(output)))
                                    elif output is not None:
                                        print('Stack overflow.')
                                    elif command == '^' \
                                            and output is None:
                                        stackNum.append(format_result
                                                        (int(number1)))
                                        stackNum.append(format_result
                                                        (int(number2)))
                                else:
                                    stackNum.append(format_result(int(number1)))
                                    stackNum.append(format_result(int(number2)))
                                    for ops in element:
                                        if ops != '=':
                                            number2 = float(stackNum.pop())
                                            number1 = float(stackNum.pop())
                                            output = \
                                                perform_calc(ops, number1,
                                                             number2)
                                            if len(stackNum) < 23 \
                                                    and output is not None:
                                                stackNum.append(format_result
                                                                (int(output)))
                                                printnum = number2
                                                number1=0
                                                number2=0
                                            elif output is not None:
                                                print('Stack overflow.')
                                            elif command == '^' \
                                                    and output is None:
                                                stackNum.append(format_result
                                                                (int(number1)))
                                                stackNum.append(format_result
                                                                (int(number2)))
                                        if ops == '=':
                                            print(format_result(printnum))
                            except ZeroDivisionError:
                                print('Divide by 0.')
                                print(format_result(0))
                            except Exception:
                                if number1 >0:
                                    stackNum.append(format_result
                                                    (int(number1)))
                                if number2 >0:
                                    stackNum.append(format_result
                                                    (int(number2)))
                                if len(stackNum)>0:
                                    print(format_result
                                          (stackNum[len(stackNum)-1]))
                                print('Stack underflow.')
                                break
                    elif element == "=":
                        try:
                            print(format_result(output))
                        except NameError:
                            print(format_result(printnum))
                    i+=1
    elif len(command)>0:
        success = False
        while True:
            try:
                if len(command) > 0:
                    if len(command)>1 and command.count('=') == len(command):
                        is_num=False
                        command=command[1:]
                    else:
                        num1, end_num1,is_num = get_number(command)
                    if is_num:
                        if success is False:
                            printNum=num1
                        command = command[end_num1:]
                        op = command[0]
                        if op != '=':
                            command = command[1:]
                            if len(command) > 0 and command!='=':
                                num2, end_num2,is_num = get_number(command)
                                if is_num:
                                    printNum = num2
                                    num1 = perform_calc(op, num1, num2)
                                    if len(stackNum) < 23:
                                        stackNum.append(format_result
                                                        (int(num1)))
                                        success=True
                                    else:
                                        print('Stack overflow.')
                                    if len(command[end_num2:])>1:
                                        command = str(num1) + \
                                                  command[end_num2:]
                            elif command=='=':
                                if op !='=' and len(stackNum)>0 \
                                        and success is False:
                                    number1=printNum
                                    number2=float(stackNum.pop())
                                    result1 = perform_calc(op, number1, number2)
                                    if len(stackNum) < 23:
                                        stackNum.append(format_result
                                                        (int(result1)))
                                    else:
                                        print('Stack overflow.')
                                print(format_result(printNum))
                        elif op == "=":
                            print(format_result(printNum))
                    else:
                        op = command[0]
                        if op != '=':
                            command = command[1:]
                            if len(command) > 0 and command!='=':
                                num2, end_num2,is_num = get_number(command)
                                if is_num:
                                    printNum = num2
                                    num1 = perform_calc(op, num1, num2)
                                    if len(stackNum) < 23:
                                        stackNum.append(format_result
                                                        (int(num1)))
                                    else:
                                        print('Stack overflow.')
                                    if len(command[end_num2:])>1:
                                        command = str(stackNum.pop()) + \
                                                  command[end_num2:]
                                else:
                                    print('Stack empty.')
                            elif command=='=' and len(op)>0:
                                if len(stackNum) > 1:
                                    number2 = float(stackNum.pop())
                                    number1 = float(stackNum.pop())
                                    output = perform_calc(op, number1, number2)
                                    if len(stackNum) < 23 and \
                                            output is not None:
                                        stackNum.append(format_result
                                                        (int(output)))
                                    elif output is not None:
                                        print('Stack overflow.')
                                    elif command == '^' and output is None:
                                        stackNum.append(format_result
                                                        (int(number1)))
                                        stackNum.append(format_result
                                                        (int(number2)))
                                    print(format_result(number2))
                                elif len(stackNum) > 0:
                                    printNum=stackNum[0]
                                    print(format_result(printNum))
                                    print('Stack underflow.')
                                elif len(stackNum) <= 0:
                                    print('Stack empty.')
                                    print('Stack underflow.')
                                elif printNum >=0:
                                    print(format_result(printNum))
                        elif op == "=":
                            print(format_result(printNum))
            except ZeroDivisionError:
                print('Divide by 0.')
                return format_result(0)
            except Exception:
                break
        return None

def filter_comments(rem_cmd):
    """This function Will remove the comments."""
    position_1 = rem_cmd.find('#')
    if position_1 > -1:
        if position_1< len(rem_cmd)-2:
            position_2=rem_cmd[position_1+1:].find('#') + position_1 + 1
        if position_2 < len(rem_cmd) - 1:
            rem_cmd = rem_cmd[0:position_1] + rem_cmd[position_2 + 1:]
        else:
            rem_cmd = rem_cmd[0:position_1]
    return rem_cmd

#This is the entry point for the program.
#Do not edit the below
if __name__ == "__main__":
    while True:
        try:
            cmd = input()
            cmd1 = filter_comments(cmd)
            result = process_command(cmd1)
            if result is not None:
                print(result)
        except Exception:
            exit()
