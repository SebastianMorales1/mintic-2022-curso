def list_operation(a, b, oper='add'):
    c = []
    if oper == 'add':
        for i in range(len(a)):
            c.append(a[i] + b[i])
    elif oper == 'sub':
        for i in range(len(a)):
            c.append(a[i] - b[i])
    elif oper == 'mult':
        for i in range(len(a)):
            c.append(a[i] * b[i])
    elif oper == 'div':
        for i in range(len(a)):
            c.append(a[i] / b[i])
    return c


def matrix_operation(a, b, oper='add'):
    c = []
    for i in range(len(a)):
        if oper == 'add':
            c.append(list_operation(a[i], b[i], oper=oper))
        elif oper == 'sub':
            c.append(list_operation(a[i], b[i], oper=oper))
        elif oper == 'mult':
            c.append(list_operation(a[i], b[i], oper=oper))
        elif oper == 'div':
            c.append(list_operation(a[i], b[i], oper=oper))
    return c


def get_elem_index(a, elem=None):
    if elem == 'min':
        return min(a), a.index(min(a))
    elif elem == 'max':
        return max(a), a.index(max(a))
    else:
        return elem, a.index(elem)


def get_average(ext_list):
    if len(ext_list) > 0:
        return sum(ext_list) / len(ext_list)
    return 0


def get_min_max_avg(existences):
    result = []
    for exist in existences:
        if len(exist) > 0:
            result.append([min(exist), get_average(exist), max(exist)])
        else:
            result.append([0 for i in range(3)])
    return result


def get_avg_per_patient(meds, n_patients):
    if n_patients > 0:
        return sum(meds) / n_patients
    return 0


def main():
    n = 0
    k = 0
    while n < 1 or k < 1:
        initial_data = input().split(' ')
        n, k, m = int(initial_data[0]), int(initial_data[1]), int(initial_data[2])
    actual_ex, request_ex, branch_count = [], [], []

    for i in range(n):
        read_ex = list(map(lambda x: int(x), input().split(' ')))
        actual_ex.append(read_ex)
        request_ex.append([0 for i in range(k)])
        branch_count.append(0)

    for i in range(m):
        read_info = input().split(' ')
        branch, med_type, n_dosis, sis, dia = int(read_info[0]), int(read_info[1]), int(read_info[2]), int(read_info[3]), int(read_info[4])
        if 0 < branch <= n and 0 < med_type <= k and n_dosis >= 0:
            if sis < 70 and dia < 50:
                request_ex[branch - 1][med_type - 1] += n_dosis
            elif 120 <= sis < 130 and 75 <= dia < 80:
                request_ex[branch - 1][med_type - 1] += n_dosis
            elif 130 <= sis < 150 and 80 <= dia < 90:
                request_ex[branch - 1][med_type - 1] += n_dosis
            elif 150 <= sis < 170 and 90 <= dia < 100:
                request_ex[branch - 1][med_type - 1] += n_dosis
            elif sis >= 170 and dia >= 100:
                request_ex[branch - 1][med_type - 1] += n_dosis
            elif sis >= 130 and dia < 80:
                request_ex[branch - 1][med_type - 1] += n_dosis
            branch_count[branch - 1] += 1

    final_ex = matrix_operation(actual_ex, request_ex, oper='sub')
    min_max_avg = get_min_max_avg(request_ex)

    for i in range(n):
        min_, index_min = get_elem_index(final_ex[i], elem='min')
        max_, index_max = get_elem_index(final_ex[i], elem='max')

        print(i + 1)
        print(index_min + 1, min_)
        print(index_max + 1, max_)
        print('{:.2f} {:.2f} {:.2f}'.format(min_max_avg[i][0], min_max_avg[i][1], min_max_avg[i][2]))
        print('{:.2f}'.format(get_avg_per_patient(request_ex[i], branch_count[i])))

    med1 = [ex[0] for ex in request_ex]
    min_, index_min = get_elem_index(med1, elem='min')
    max_, index_max = get_elem_index(med1, elem='max')
    print(index_min + 1, min_)
    print(index_max + 1, max_)


if __name__ == "__main__":
    main()