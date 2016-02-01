def draw(number):
    if number == 0:
        return

    print "*" * number
    draw(number - 1)
    print "#" * number

draw(5)


def reverse_draw(number, acc = 1):
    if acc == number:
        return

    print "*" * acc
    reverse_draw(number, acc + 1)
    print "#" * acc

reverse_draw(5)

def ddraw(number):
    m = 1
    if m >= number:
        return

    print "*" * m
    m += 1
    ddraw(number - 1)
    print "#" * m

ddraw(10)


# The way it works:
# Suzdava funkciq vuv funkciqta dokato ne stigne do 0, kogato stigne 0
# izliza ot fuknciqta i izplnqva tova sled neq, kato v sluchaq predi 0 e 1
# i umnojava po 1, izliza ot fuknciqta umnojava s prednoto chislo i t.n.
"""
draw(5):
  if 5 == 0:
      return

  print "*" * 5
  draw(5 - 1):
    if 4 == 0:
        return

    print "*" * 4
    draw(4 - 1):
      if 3 == 0:
          return

      print "*" * 3
      draw(3 - 1):
        if 2 == 0:
            return

        print "*" * 2
        draw(2 - 1):
          if 1 == 0:
              return

          print "*" * 1
          draw(1 - 1):
            if 0 == 0:
                return
          print "#" * 1
        print "#" * 2
      print "#" * 3
    print "#" * 4
  print "#" * 5
"""
