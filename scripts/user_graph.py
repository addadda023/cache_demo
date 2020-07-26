# User data graph
import collections


def return_degree(user1, user2):
    if user1 is user2:
        return 0
    elif user1.is_friend(user2):
        return 1
    else:
        # depth first search to find degree of connection
        q = collections.deque()
        q.append((user1, 0))
        while q:
            user, degree = q.popleft()
            if user is user2:
                return degree
            elif degree > 5:
                return -1
            for friend in user.friends:
                q.append((friend, degree+1))

        return -1
