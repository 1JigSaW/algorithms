'''
По данным nn отрезкам необходимо найти 
множество точек минимального размера, 
для которого каждый из отрезков содержит 
хотя бы одну из точек.
В первой строке дано число 1 <= n <= 100 отрезков. 
Каждая из последующих nn строк содержит по 
два числа 0 <= l <= r <= 10^9, задающих 
начало и конец отрезка. 
Выведите оптимальное число mm точек и сами mm точек. 
Если таких множеств точек несколько, 
выведите любое из них.
Sample Input 1:
3
1 3
2 5
3 6

Sample Output 1:
1
3 

Sample Input 2:
4
4 7
1 3
2 5
5 6

Sample Output 2:
2
3 6 
'''

def dots(segments):
    resulting_segments = []
    while len(segments) > 0:
        if len(segments) < 2:
            seg = segments.pop()
            resulting_segments.append(seg)
        else:
            a, b = segments[0], segments[1]
            print(a, b)
            if b[0] <= a[1]:
                left, right = b[0], b[1] if b[1] <= a[1] else a[1]
                #print(left, right)
                overlapping = (left, right)
                segments = segments[2:]
                #print(segments)
                segments = [overlapping] + segments
                #print(segments)
            else:
                resulting_segments.append(segments[0])
                segments = segments[1:]
    return [x[1] for x in resulting_segments]


def main():
    n = int(input())
    segments = []
    for i in range(n):
        segments.append(tuple(map(int, input().split())))
    segments.sort(key=lambda x: (x[0], x[1]))
    result = dots(segments)
    print(len(result))
    print(' '.join(map(str, result)))


if __name__ == "__main__":
    main()