import math
def list_animals(animals):
    return ''.join('{}. {}\n'.format(i, x) for (i, x) in enumerate(animals, 1))
def list_animals2(animals):
    list = ""
    j=0
    for i in animals:
        j+=1;
        list+=(str(j) + '. ' + i + '\n')
    return list


def sale_hotdogs(n):
    if n<5:
        return 100*n
    else:
        if (n>=5 and n<10):
            return 95*n
    return 90*n;
def sale_hotdogs2(n):
    return n * (100 if n < 5 else 95 if n < 10 else 90)
def uni_total(string):
    suma=0;
    for x in string:
        suma+=ord(x);
    return suma;

def uni_total2(string):
    return sum(map(ord, string))
def uni_total3(string):
    return sum(ord(c) for c in string)

def positive_sum(arr):
    suma=0;
    for x in arr:
        if x>0: suma+=x
    return suma
positive_sum2=lambda arr:sum(map(lambda x:x>0,arr))
positive_sum4 = lambda lst: sum(list(filter(lambda _: _ > 0, lst)))
def positive_sum3(a):
  return sum(i for i in a if i>0)

multiply = lambda a,b: a * b

class Python:
    name=''
    def __init__(self, name):
      self.name = name
#unexpected Parsing
def get_status(is_busy):
    status = "busy" if is_busy else "available"
    return {"status": status }
def get_status2(is_busy):
    answer = {}
    answer['status'] = "busy" if is_busy else "available"
    return answer
#Stringy Strings
def stringy(size):
    result = ""
    for i in range(size):
        if i%2==0:
            result+="1"
        else:
            result+="0"
    return result
def stringy2(size):
    return "".join([str(i % 2) for i in range(1, size + 1)])
stringy3=lambda n:('10'*n)[:n]
#Formatting decimal places #0
def two_decimal_places(n):
    return round(n*100)/100
def two_decimal_places2(n):
    return round(n, 2)
def two_decimal_places3(n):
    return float("%.2f" % n)
#Conver a Boolean to a String
def boolean_to_string(b):
    if b:
        return "True"
    return "False"
def boolean_to_string2(b):
    return 'True' if b else 'False'
def boolean_to_string3(b):
    return str(b)
#Multiples2
def multiples(x):
    if x%49==0 and x%3==0:
        return "Fang"
    elif x%7==0:
        return "Fizz"
    elif x%15==0:
        return "Foo"
    else:
        return "Far"
def multiples2(x):
    return "Fang" if int(x) % (49*3) == 0 else "Fizz" if int(x) % 7 == 0 else "Foo" if int(x) % 15 == 0 else "Far"
#Super Duper Easy
def problem(a):
    if((isinstance(a, float)) or (isinstance(a, int))):
        return a*50+6;
    return "Error"
def problem2(a):
    return "Error" if isinstance(a,str) else a*50+6
#Remove First and Last Character
def remove_char(s):
    return s[1:-1]
#Beginner Series #4 Cockroach
def cockroach_speed(s):
    return int((s*27.7778))
#Friend or Foe?
def friend(x):
    return [elem for elem in x if len(elem)==4]
def friend2(x):
    return filter(lambda name: len(name) == 4, x)
#Grasshopper - Debug
def weather_info(temp):
    c = convertToCelsius(temp)
    if (c > 0):
        return (str(c) + " is freezing temperature")
    else:
        return (str(c) + " is above freezing temperature")
def convertToCelsius(fahrenheit):
    celsius = (fahrenheit - 32) * (5 / 9)
    return celsius
#Finding Averages
def average(x):
    suma=0
    i=0
    for value in x:
        if ((isinstance(value, float)) or (isinstance(value, int))):
            suma+=value
            i+=1
        else:
            return "Incorrect"
    srednia=suma/i
    return int(srednia)
def average2(xs):
    try:
        return sum(xs)/len(xs)
    except:
        return "Incorrect"
#Convert natural number to its binary representation.
def int_to_bin(n):
    return bin(n)[2:]
def int_to_bin2(n):
    return '{:b}'.format(n)
int_to_bin3=lambda n:bin(n)[2:]
#Heron's Formula
def heron(a, b, c):
    s=(a+b+c)/2.0;
    return math.sqrt(s*(s-a)*(s-b)*(s-c))
heron2=lambda a, b, c: (lambda p: (p*(p-a)*(p-b)*(p-c))**0.5)((a+b+c)/2.0)
#Unique Sum
def unique_sum(lst):
    if len(lst)<1:
        return None
    return sum(set(lst))
def unique_sum2(lst):
    return sum(set(lst)) if lst else None
#Who ate the cookie?
def cookie(x):
    result="Who ate the last cookie? "
    if (isinstance(x, bool)):
        return result + "It was the dog!"
    elif ((isinstance(x, float)) or (isinstance(x, int))):
        return result+"It was Monica!"
    elif (isinstance(x, str)):
        return result+"It was Zach!"
    return result+"It was the dog!"
def cookie2(x):
    return "Who ate the last cookie? It was %s!" % {str:"Zach", float:"Monica", int:"Monica"}.get(type(x), "the dog")
#Summations: 1
def summation(x):
    if isinstance(x, int):
        suma=0
        for value in range(x):
            suma+=value;
        return suma
    else:
        return "Error 404"
def summation2(x):
    return sum(range(x+1)) if isinstance(x, int) else "Error 404";
#Return a string's even characters.
def evenChars(string):
    return string[1::2]
def greet(name):
    return "Hello, %s how are you doing today?" %name
def greet2(name):
    return "Hello, {} how are you doing today?".format(name)
greet3 = lambda name: "Hello, %s how are you doing today?" % name
#Regex count lowercase letters
def lowercase_count(strng):
    suma=0
    for x in strng:
        if ord(x)>=97 and ord(x)<=122:
            suma+=1
    return suma
def lowercase_count2(strng):
    return sum(a.islower() for a in strng)
lowercase_count3=lambda s: len([x for x in s if x in "abcdefghijklmnopqrstuvwxyz"])
def lowercase_count4(strng):
    return len(''.join(filter(lambda s: s.islower(), str(strng))))
#Freudian translator
def to_freud(sentence):
    return " ".join("sex" for i in sentence.split())
def to_freud2(s):
    return (len(s.split()) * "sex ").strip()
#Printing Array elements with Comma delimiters
def print_array(arr):
    return ",".join(str(i) for i in arr)
print(print_array([2,4,5,2]))
def billboard(name, price=30):
    return len(name)*price
print(billboard("Jeong-Ho Aristotelis",40))



