from .__base__ import register

@register
def myfunc():
    print("hello function [B.A]")

@register
class Aclass:
    
    @staticmethod
    def test():
        print("hello world [B.A]")