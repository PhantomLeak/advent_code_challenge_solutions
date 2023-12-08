D = open("input.txt", "r").read().strip()
L = D.split('\n')

t, d = L  # Split time and distance

time = [int(x) for x in t.split(':')[1].split()]
distance = [int(x) for x in d.split(':')[1].split()]


def num_record_breaks(time, distance):
    answer = 0
    for x in range(time + 1):
        print(x)
        dx = x * (time - x)
        if dx >= distance:
            answer += 1
    return answer

def concat_time_and_dist():
    D = ''
    T = ''
    for t in time:
        T += str(t)
    T = int(T)

    for d in distance:
        D += str(d)
    D = int(D)
    return T, D


def main():
    answer_one = 1
    for i in range(len(time)):  # loop through the num of races
        answer_one *= num_record_breaks(time[i], distance[i])

    print(answer_one)

    concat_distance, concat_time = concat_time_and_dist()
    print(concat_distance, concat_time)
    answer_two = num_record_breaks(concat_time, concat_distance)

    print(answer_two)


if __name__ == "__main__":
    main()
