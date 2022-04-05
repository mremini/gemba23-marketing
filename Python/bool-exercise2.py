def should_get_hired(interview_one_score, interview_two_score):
    if interview_one_score > 4 and interview_two_score > 4:
        action = 'hire'
    elif interview_one_score > 4 or interview_two_score > 4:
        action = 'interview again'
    else:
        action = 'nope'
        return action