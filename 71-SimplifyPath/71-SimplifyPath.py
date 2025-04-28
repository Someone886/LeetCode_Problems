# Last updated: 4/28/2025, 2:30:41 AM
class Solution:
    def simplifyPath(self, path: str) -> str:
        stack=[]
        paths = path.split("/")

        for i in paths:
            if i == "..":
                if stack:
                    stack.pop()
            elif i != "" and i != ".":
                stack.append(i)
        
        return "/" + "/".join(stack)

'''
class Solution:
    def simplifyPath(self, path: str) -> str:
        simplified_path = ["/"]
        curr_folder = []

        for char in path[1:]:
            if char == "/" and not curr_folder:
                continue
            
            if char != "/":
                curr_folder.append(char)
            else:
                if curr_folder == ["."]:
                    curr_folder = []

                elif curr_folder == [".", "."]:
                    seen_backslash = 0
                    while len(simplified_path) > 1:
                        if simplified_path[-1] == '/':
                            seen_backslash += 1
                        
                        if seen_backslash == 2:
                            break
                        else:
                            simplified_path.pop()
                    curr_folder = []

                else:
                    simplified_path.extend(curr_folder + ['/'])
                    curr_folder = []
        
        if curr_folder == ["."]:
            curr_folder = []

        elif curr_folder == [".", "."]:
            seen_backslash = 0
            while len(simplified_path) > 1:
                if simplified_path[-1] == '/':
                    seen_backslash += 1
                
                if seen_backslash == 2:
                    break
                else:
                    simplified_path.pop()
            curr_folder = []

        else:
            simplified_path.extend(curr_folder)
            curr_folder = []
            
        if len(simplified_path) > 1 and simplified_path[-1] == "/":
            simplified_path.pop()
        
        return "".join(simplified_path)
         
'''