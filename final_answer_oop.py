import sys
from math import gcd, sqrt, log

class LuyThua:
    def __init__(self, l):
        self.l=l

    def to_string(self):
        arr= self.l.split( )

        components_copy = []
        original=[]
        for i in arr:
            switch = 0
            copy_fraction1 = i.split("/")
            a, b= int(copy_fraction1[0]), int(copy_fraction1[1])
            original.append(a)
            original.append(b)
            if b == 0:
                components_copy.append(a)
                components_copy.append(0)
                switch=1
            if a == 0 and switch==0:
                components_copy.append(0)
                components_copy.append(1)
                switch=1
            c = gcd(a, b)
            if c!=0:
                a //= c
                b //= c
            if b < 0:
                a, b = -a, -b
            if b == 1 and switch==0:
                components_copy.append(a)
                components_copy.append(b)
                switch = 1
            if switch==0:
                components_copy.append(a)
                components_copy.append(b)

        #Deal with the conditions(part 1)
        x=components_copy[0]
        y=components_copy[1]
        z=components_copy[2]
        t=components_copy[3]

        if y==0 or t==0 or (x==0 and z<0) or (x==0 and z==0):
            return f"({original[0]}/{original[1]})^({original[2]}/{original[3]})"
        if x==0:
            return "(0/1)^(1/1)"
        if z==0:
            return "(1/1)^(0/1)"
        if t%2==0 and x<0:
            return f"({original[0]}/{original[1]})^({original[2]}/{original[3]})"
        if z<0:
            x,y=y,x
            z=-z
            if y<0:
                x,y=-x,-y
        if z % 2 == 0:
            x,y=abs(x),abs(y)
        phanTich_tu = []
        for a in range(2, int(sqrt(abs(x)) + 1)):
            b = round(log(abs(x), a))
            if a ** b == x:
                if x<0:
                    phanTich_tu.append((-a, b))
                elif x>0:
                    phanTich_tu.append((a, b))
        phanTich_mau=[]
        for a in range(2, int(sqrt(abs(y)) + 1)):
            b = round(log(y, a))
            if a ** b == y:
                phanTich_mau.append((a, b))


        options = list()
        options.append(x)
        options.append(y)
        options.append(z)
        options.append(t)

        if len(phanTich_tu):
            for each_pair in phanTich_tu:
                b = round(pow(y, 1 / each_pair[1]))
                if b ** each_pair[1] == y:
                    options.append(each_pair[0])
                    options.append(b)
                    if t % each_pair[1] == 0:
                        options.append(z)
                        options.append(t // each_pair[1])
                    elif each_pair[1] % t == 0:
                        x = (each_pair[1] // t)
                        options.append(z * x)
                        options.append(1)
                    else:
                        options.append(z * each_pair[1])
                        options.append(t)
                    z_copy=z*each_pair[1]

                    for i in range (2,int(z_copy+1)):
                        if z_copy%i==0:
                            options.append(x**i)
                            options.append(y**i)
                            options.append(z//i)
                            options.append(t)
        if len(phanTich_mau):
            for each_pair in phanTich_mau:
                b = round(pow(abs(x), 1 / each_pair[1]))
                if b ** each_pair[1] == x:
                    if x<0:
                        options.append(-b)
                        options.append(each_pair[0])
                    else:
                        options.append(b)
                        options.append(each_pair[0])
                    if t % each_pair[1] == 0:
                        options.append(z)
                        options.append(t // each_pair[1])
                    elif each_pair[1] % t == 0:
                        x = (each_pair[1] // t)
                        options.append(z * x)
                        options.append(1)
                    else:
                        options.append(z * each_pair[1])
                        options.append(t)
                    z_copy=z*each_pair[1]

                    for i in range (2,int(z_copy+1)):
                        if z_copy%i==0:
                            options.append(x**i)
                            options.append(y**i)
                            options.append(z//i)
                            options.append(t)
        for i in range (2,z+1):
            if z%i==0:
                options.append(x**i)
                options.append(y**i)
                options.append(z//i)
                options.append(t)
        option_divided=[]
        for i in range(0,len(options)-2):
            blank=[]
            if i%4==0:
                blank.append(options[i:i+4])
                option_divided.append(blank)
        final_options=[option_divided[0]]
        prev_option=option_divided[0]

        for i in range(1,len(option_divided)):
            len_option = 0
            len_prev_option = 0
            for num in option_divided[i]:
                len_option += len(str(num))
            for num in prev_option:
                len_prev_option += len(str(num))
            if len_option <= len_prev_option:
                final_options.append(option_divided[i])
                prev_option=option_divided[i]
                if len_option < len_prev_option:
                    final_options = [option_divided[i]]
        x,y,z,t = sorted(final_options)[0][0]

        if x==1==y:
            return f'(1/1)^(0/1)'
        if z%2==0:
            return f'({abs(x)}/{abs(y)})^({z}/{t})'

        return f'({x}/{y})^({z}/{t})'


def main():
    sys.stdin = open('input1.txt', 'r')
    for l in sys.stdin.read().split('\n'):
        if l.strip():
            print(LuyThua(l.strip()).to_string())

if __name__ == '__main__':
    main()
