from .__base__ import register


@register
class Bclass:
    @staticmethod
    def test():
        print("hello world [A.B]")
