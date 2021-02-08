class Solution:
    def interpret(self, command: str) -> str:
        s=command.replace('()','o')
        d=s.replace('(','')
        f=d.replace(')','')
        return f