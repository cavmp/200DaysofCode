"""
File: averagescores.py
----------------------
This program reads score values from a user and computes their
average.  
"""

def get_scores():
    """
    Asks the user for a list of scores (numbers).
    Returns a list containing the scores
    """
    score_list = []
    while True:
        score = float(input("Enter score (0 to stop): "))
        if score == 0:
            break
        score_list.append(score)
    return score_list


def compute_average(score_list):
    """
    Returns the average value of the list of scores passed in.
    """
    num_scores = len(score_list)
    total = sum(score_list)
    return total / num_scores


def print_list(alist):
    """
    Prints all the values in the list passed in
    """
    for value in alist:
        print(value)


def main():
    """
    Computes average for a set of scores entered by the user.
    """
    scores = get_scores()
    print("Scores are:")
    print_list(scores)
    avg = compute_average(scores)
    print('Average score is ' + str(avg))

if __name__ == '__main__':
    main()
