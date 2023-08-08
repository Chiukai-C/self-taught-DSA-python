def two_sum(numbers, ind1, ans):
    ind2 = ind1 + 1
    ind3 = len(numbers) - 1
    while ind2 < ind3:
        num = numbers[ind2] + numbers[ind3]
        if num == -numbers[ind1]:
            ans.append([numbers[ind1], numbers[ind2], numbers[ind3]])
            ind2 += 1
            ind3 -= 1
            while ind2 < ind3 and numbers[ind2 - 1] == numbers[ind2]:
                ind2 += 1
        elif num < -numbers[ind1]:
            ind2 += 1
        else:
            ind3 -= 1


def three_sum(numbers):
    numbers = sorted(numbers)
    ans = []
    for ind1 in range(len(numbers)):
        if numbers[ind1] > 0:
            break
        if ind1 == 0 or numbers[ind1 - 1] != numbers[ind1]:
            two_sum(numbers, ind1, ans)
    return ans
