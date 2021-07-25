from .__base__ import register

@register
def myfunc():
    print("hello function [A.A]")

@register
class Aclass:
    
    @staticmethod
    def test():
        print("hello world [A.A]")