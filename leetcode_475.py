def findRadius(houses, heaters):
    """
    :type houses: List[int]
    :type heaters: List[int]
    :rtype: int
    对于每一个房子，用二分法找到离他最近的heater，然后取他们距离的绝对值，如果有两个，则取二者的min，同时
    keep track of 一个最大值，这个最小值当遍历完之后就是答案
    """

    # def binary_search(house_pos):#给定一个房子的位置，找离他最近的heater(s)
    #     dist1, dist2 = float('inf'), float('inf')
    #     left, right = 0, len(heaters) - 1
    #     while left <= right:
    #         mid = (left + right) // 2
    #         if heaters[mid] < house_pos:
    #             left = mid + 1
    #         else:
    #             right = mid - 1
    #
    #     if 0 <= left < len(heaters):
    #         dist1 = abs(heaters[left] - house_pos)
    #     else:
    #         dist1 = float('inf')
    #     if len(heaters) > right >= 0:
    #         dist2 = abs(heaters[right] - house_pos)
    #     else:
    #         dist2 = float('inf')
    #
    #     return min(dist1, dist2)
    #
    # max_radius = 0
    # for house in houses:
    #     min_dist = binary_search(house)
    #     max_radius = max(max_radius, min_dist)
    #
    # return max_radius

    '''
    或者，由于heater和houses都是递增的，我们只要找到每一个heater - houses的绝对值的最大值就可以得到
    答案
    '''
    heaters.sort()
    houses.sort()
    heater_pointer = 0
    dist = 0
    for house in houses:
        while heater_pointer < len(heaters) - 1:
            cur_dist = abs(heaters[heater_pointer] - house)
            next_dist = abs(heaters[heater_pointer + 1] - house)
            if next_dist <= cur_dist:
                heater_pointer += 1
            else:
                break
        cur_dist = abs(heaters[heater_pointer] - house)
        dist = max(dist, cur_dist)
    return dist




