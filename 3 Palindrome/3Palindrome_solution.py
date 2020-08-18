def palindrome(string, start, end, cc):
    x = (string[start:end])
    if cc == 3:
        if string[start:] == string[start:][::-1]:
            stack.append(''.join(string[start:]))
            return
        else:
            tem = stack.pop()
            start = abs(len(tem) - start)
            end = abs(len(tem) - end) + abs(start-end) - 1
            palindrome(string, start, end, cc-1)
    else:
        if stack == []:
            if x == x[::-1]:
                stack.append(''.join(x))
                if stack  == []:
                    palindrome(string, start+1, start+2, cc+1)
                else:
                    palindrome(string, start+len(stack[-1]), start+len(stack[-1])+1, cc+1)
            else:
                if(end < len(string) and len(x) <= len(string[end:])):
                    if stack != [] and len(x) < len(stack[-1]):
                        t = stack.pop()
                        palindrome(string, start-len(t)-1, len(t)+1, cc-1)
                    else:
                        palindrome(string, start, end+1, cc)
                return False
                
        else:
            if(end < len(string)  and len(x) < len(string)):
                if x == x[::-1]:
                    stack.append(''.join(x))
                    if stack  == []:
                        palindrome(string, start+1, start+2, cc+1)
                    else:
                        palindrome(string, start+len(stack[-1]), start+len(stack[-1])+1, cc+1)
                else:
                    palindrome(string, start, end+1, cc)
            else:
                tem = stack.pop()
                palindrome(string, abs(start-len(tem)), len(tem)+1, cc-1)
        


stack = []
string = list(input())
palindrome(string, 0, 1, 1)
if len(stack) < 3:
    print('Impossible')
else:
    print(stack[0])
    print(stack[1])
    print(stack[-1])