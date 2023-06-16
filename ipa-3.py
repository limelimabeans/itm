#!/usr/bin/env python
# coding: utf-8

# In[ ]:


def relationship_status(from_member, to_member, social_graph):
    '''Relationship Status.
    20 points.

    Let us pretend that you are building a new app.
    Your app supports social media functionality, which means that users can have
    relationships with other users.

    There are two guidelines for describing relationships on this social media app:
    1. Any user can follow any other user.
    2. If two users follow each other, they are considered friends.

    This function describes the relationship that two users have with each other.

    Please see "assignment-4-sample-data.py" for sample data. The social graph
    will adhere to the same pattern.

    Parameters
    ----------
    from_member: str
        the subject member
    to_member: str
        the object member
    social_graph: dict
        the relationship data

    Returns
    -------
    str
        "follower" if fromMember follows toMember,
        "followed by" if fromMember is followed by toMember,
        "friends" if fromMember and toMember follow each other,
        "no relationship" if neither fromMember nor toMember follow each other.
    '''
    # Replace `pass` with your code.
    # Stay within the function. Only use the parameters as input. The function should return your answer.
    from_follow_to = to_member in social_graph[from_member]["following"]
    to_follow_from = from_member in social_graph[to_member]["following"]
    if from_follow_to == True:
        if to_follow_from == True:
            return "friends"
        return "following"
    if from_follow_to == False:
        if to_follow_from == True:
            return "followed by"
        return "no relationship"


# In[ ]:


def tic_tac_toe(board):
    '''Tic Tac Toe.
    25 points.

    Tic Tac Toe is a common paper-and-pencil game.
    Players must attempt to successfully draw a straight line of their symbol across a grid.
    The player that does this first is considered the winner.

    This function evaluates a tic tac toe board and returns the winner.

    Please see "assignment-4-sample-data.py" for sample data. The board will adhere
    to the same pattern. The board may by 3x3, 4x4, 5x5, or 6x6. The board will never
    have more than one winner. The board will only ever have 2 unique symbols at the same time.

    Parameters
    ----------
    board: list
        the representation of the tic-tac-toe board as a square list of lists

    Returns
    -------
    str
        the symbol of the winner or "NO WINNER" if there is no winner
    '''
    # Replace `pass` with your code.
    # Stay within the function. Only use the parameters as input. The function should return your answer.
    for row in board:
        if len(set(row)) == 1 and row[0] != " ":
            return row[0]

    for col in range(len(board)):
        column = [board[row][col] for row in range(len(board))]
        if len(set(column)) == 1 and column[0] != " ":
            return column[0]

    negative_diagonal = []
    positive_diagonal = []
    for i in range(len(board)):
        negative_diagonal.append(board[i][i])
        positive_diagonal.append(board[i][len(board) - 1 - i])
    if len(set(negative_diagonal)) == 1 and negative_diagonal[0] != " ":
        return negative_diagonal[0]
    if len(set(positive_diagonal)) == 1 and positive_diagonal[0] != " ":
        return positive_diagonal[0]

    return "NO WINNER"


# In[ ]:


def eta(first_stop, second_stop, route_map):
    '''ETA.
    25 points.

    A shuttle van service is tasked to travel along a predefined circlar route.
    This route is divided into several legs between stops.
    The route is one-way only, and it is fully connected to itself.

    This function returns how long it will take the shuttle to arrive at a stop
    after leaving another stop.

    Please see "mod-4-ipa-1-sample-data.py" for sample data. The route map will
    adhere to the same pattern. The route map may contain more legs and more stops,
    but it will always be one-way and fully enclosed.

    Parameters
    ----------
    first_stop: str
        the stop that the shuttle will leave
    second_stop: str
        the stop that the shuttle will arrive at
    route_map: dict
        the data describing the routes

    Returns
    -------
    int
        the time it will take the shuttle to travel from first_stop to second_stop
    '''
    # Replace `pass` with your code.
    # Stay within the function. Only use the parameters as input. The function should return your answer.
    keys = list(route_map.keys())
    if (first_stop, second_stop) in keys:
        return route_map[(first_stop, second_stop)]["travel_time_mins"]

    start_index = 0
    for key in keys:
        if key[0] == first_stop:
            start_index = keys.index(key)

    # assuming stops aren't sorted in route_map
    total_travel_time = 0
    start_stop = first_stop
    while start_stop != second_stop:
        if keys[start_index][0] != start_stop:
            start_index = (start_index + 1) % len(keys)
            continue
        total_travel_time += route_map[keys[start_index]]["travel_time_mins"]
        start_stop = keys[start_index][1]
        start_index = (start_index + 1) % len(keys)

    return total_travel_time

