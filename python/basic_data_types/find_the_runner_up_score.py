if __name__ == '__main__':
    n = int(input())
    arr = map(int, input().split())
    scores = sorted([score for score in arr], reverse=True)

    for score in scores:
        if score != scores[0]:  # First different score is the runner-up score
            print(score)
            break
