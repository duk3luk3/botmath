import parsley
import random

class BotMath:

  rng = random.SystemRandom()

  def calculate(self, start, pairs):
      result = start
      for op, value in pairs:
          if op == '+':
              result += value
          elif op == '-':
              result -= value
          elif op == '*':
              result *= value
          elif op == '/':
              result /= value
      return result

  def roll(self,ndice, neyes, floating):
    sum = 0
    for i in range(ndice):
      while True:
        roll = self.rng.randint(1,neyes)
        sum = sum + roll
        if roll != neyes or not floating:
          break
    return sum

  x = None

  def parse(self, expr):
    if not self.x:
      self.x = parsley.makeGrammar("""
        number = <digit+>:ds -> int(ds)
        purenum = <number>:n ~ 'd' -> int(n)
        parens = '(' ws expr:e ws ')' -> e
        value = purenum | parens | basicroll
        ws = ' '*
        add = '+' ws expr2:n -> ('+', n)
        sub = '-' ws expr2:n -> ('-', n)
        mul = '*' ws value:n -> ('*', n)
        div = '/' ws value:n -> ('/', n)

        basicroll = number:ndice 'd' number:neyes ~ 'f' -> roll(ndice, neyes, False)
        basicroll = number:ndice 'd' number:neyes   'f' -> roll(ndice, neyes, True)

        addsub = ws (add | sub)
        muldiv = ws (mul | div)

        expr = expr2:left addsub*:right -> calculate(left, right)
        expr2 = value:left muldiv*:right -> calculate(left, right)
      """, {"calculate": self.calculate, "roll": self.roll})

    return self.x(expr).expr()

