def findContestMatch(n):
    """
    :type n: int
    :rtype: str
    1,2,3,4,5,6,7,8 - 8
    18 27 36 45 - 4
    1845 2736  - 2
    18452736 - 1

    """

    team_match = [str(i) for i in range(1,n+1)]
    while len(team_match) > 1:
        round = []
        for i in range(len(team_match) // 2):
            new_match = f'({team_match[i]}, {team_match[- i - 1]})'
            round.append(new_match)
        team_match = round # 要及时更新
    return team_match[0]

print(findContestMatch(8))


# 我觉得也可以使用recursion,因为没比完一轮，剩下来的str马上可以作为新的input进行一轮完全一样的操作


