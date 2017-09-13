#Warmup-2>string_times
def string_times(str, n):
    return str*n

    #front_times

def front_times(str, n):
  return str[0:3] * n


    #string_bits

def string_bits(str):
  result = ""
  for i in range(len(str)):
    if i % 2 == 0:
      result = result + str[i]
  return result
    
    
    #lone_sum

def lone_sum(a, b, c):
  if a == b ==c:
    return 0
  elif a == b:
    return c
  elif a == c:
    return b
  elif b == c:
    return a
  else:
    return a + b + c


    #string_splosion

def string_splosion(str):
    result = ''
    for i in range(len(str)+1):
        result += str[:i]
    return result


    #cigar_party

def cigar_party(cigars, is_weekend):
  if is_weekend:
    return (cigars >= 40)
  else:
    return (cigars >= 40 and cigars <= 60)

    #caught_speeding

def caught_speeding(speed, is_birthday):
  if is_birthday:
    speed -= 5    
  if speed <= 60:
      return 0
  if 60 < speed <= 80:
    return 1
  return 2
