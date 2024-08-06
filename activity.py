def maximumActivities(start, finish):
    n = len(start)
    m = len(finish)
    activity = []
    for i in range(n):
        activity.append((finish[i],start[i]))

    # Sort the meetings according to their Finishing Time.
    activity.sort()
    maxActivity = 1
    currentTime = activity[0][0]
    for i in range(1,n):

        # Find the next meeting available.
        if (activity[i][1] >= currentTime):
            maxActivity+=1
            currentTime = activity[i][0]
    return maxActivity   

if __name__== '__main__':
    start = [1, 3, 0, 5, 8, 5]
    finish = [2, 4, 6, 7, 9, 9]
    print(maximumActivities(start, finish))  # Output: 4
    