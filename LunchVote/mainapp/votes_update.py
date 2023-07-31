import datetime

from .models import Slot, User


def update_votes():
    """
    This task runs daily at 13:00.
    Steps:
     1. Get places with max votes
      1.1 If multiple, check distinct users
      1.2 If one, flag as a winner
     2. Set votes for every user as max_votes attribute
    """
    print('Collecting slots')
    slots = Slot.objects.filter(date__gte=datetime.datetime.today() - datetime.timedelta(hours=24))
    sorted_slots = sorted(slots, key=lambda x: x.votes_count, reverse=True)
    vote_leaders = [sorted_slots[0], ]
    max_votes_num = sorted_slots[0].votes_count
    for slot in sorted_slots:
        if slot.votes_count == max_votes_num:
            vote_leaders.append(slot)
        else:
            break

    print(f"Max votes for: {[slot for slot in vote_leaders]}")
    if len(vote_leaders) > 1:
        winner = sorted(vote_leaders, key=lambda x: x.distinct_votes, reverse=True)[0]
    else:
        winner = vote_leaders[0]

    winner.is_winner = True
    winner.save()
    print(f"Restaurant {winner.restaurant.name} won with {winner.votes_count} points")

    print("Resetting votes")
    for slot in slots:
        for vote in slot.votes.all():
            vote.archieved = True
            vote.save()
    print("Votes reset")


print("this function runs every 10 seconds")
