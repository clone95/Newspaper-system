# coding : utf-8
"""

|   User - Publisher - Aggregator   |  SYSTEM

"""


class Publisher:

    def __init__(self, name='default_publisher', aggregator='default_aggregator'):
        self.name = name
        self.aggregator = [aggregator]
        self.documents = dict()
        self.published = set()
        self.subs = set()
        self.counter = 0

    def add_news(self, aggregator, uploading, permissions='low'):           # publish a news
            aggregator.update(self, uploading, permissions)

    def write_news(self, document):                                         # write a news to publish later
        self.documents[self.counter] = document
        self.counter += 1

    def subscribe_to_aggr(self, aggregators):                               # subscribe a publisher to an aggregator
        for aggr in aggregators:                                            # tom's hardware -> aggregator
            aggr.insert_publisher(self)

    def add_sub(self, new_sub):                                             # new user following tom's hardware
        self.subs.add(new_sub)


class User:

    def __init__(self, name='default_user'):
        self.name = name
        self.permissions = 'low'
        self.subscriptions = []
        self.news = dict()
        self.counter = 0

    def subscribe(self, publisher, aggregator, permissions='low'):          # subscribe to a pub
        self.subscriptions.append(publisher.name)
        aggregator.subscribe(self, permissions, publisher)

    def receive(self, publisher, document):                                 # send the news to all users subscribed
        self.news[publisher.name] = document

    def subscribe_all(self, aggregator, permissions='low'):                 # subscribes to all pubs in the aggregator
        aggregator.subscribe_me_all(self, permissions)

    def print_news(self, publisher=None):                                   # prints the news in my mailbox
        if publisher is None:
            for element in self.subscriptions:
                print(self.news[element])
        else:
            print(self.news[publisher])

    def delete_subscription(self, publisher):                               # remove me from a publisher's list
        self.subscriptions.remove(publisher)


class Aggregator:

    def __init__(self, name='default_aggregator'):
        self.name = name
        self.publishers = set()
        self.subscriptions = dict(dict())
        self.counter = 0

    def subscribe(self, caller, permissions='low', publisher=Publisher()):  # subscribe: works for both users and pubs.
        if isinstance(caller, Publisher):
            self.publishers.add(caller)
        else:
            self.subscriptions[publisher.name + "_" + str(self.counter)] = {caller: permissions}
            self.notify_to_pub(caller, publisher)
            self.counter += 1
            # print(caller.name, "subscribing", publisher.name)

    def subscribe_me_all(self, caller, permissions):                        # subscribes a user to all pubs
        for paper in self.publishers:
            caller.subscribe(paper, self, permissions)

    def remove(self, caller):                                               # removes a user from a publisher
        if isinstance(caller, Publisher):
            self.publishers.remove(caller)
        else:
            self.subscriptions.__delitem__(caller)

    @staticmethod
    def notify_to_pub(caller, publisher):                                   # tell to the pub that has a new sub
        publisher.add_sub(caller.name)

    def update(self, publisher, document, permissions):                     # send the news
        to_reach = self.get_users_for_publisher(publisher)

        for user in range(0, len(to_reach)):
            if list(to_reach[user].values())[0] == permissions:              # you can receive it just if you own
                list(to_reach[user].keys())[0].receive(publisher, document)  # the required permissions

    def get_users_for_publisher(self, publisher):                           # return the list of users subscribed
        users = []                                                          # to a given publisher
        for sub in self.subscriptions:
            if sub[:-2] == publisher.name:
                users.append(self.subscriptions[sub])
        return users


################################################################

# let's play a bit with the system!!
# some users
giacomo = User("giacomo")
marco = User("marco")
andrea = User("andrea")

# some publishers
salvatore = Publisher("salvatore aranzulla")
toms = Publisher("Tom's Hardware")

# an aggregator
agg = Aggregator()

agg.subscribe(salvatore)        # subscribing publisher
agg.subscribe(toms)             # subscribing publisher

# giacomo.subscribe(salvatore, agg, 'mid')        # subscribe giacomo -> salvatore
# giacomo.subscribe(toms, agg, 'mid')             # subscribe giacomo -> toms
marco.subscribe(salvatore, agg, 'high')          # subscribe marco -> toms
marco.subscribe(toms, agg, 'high')               # subscribe marco -> toms
giacomo.subscribe_all(agg, 'mid')                       # subscribe giacomo --> to all

salvatore.write_news("buon giorno")             # let's  write some news.....
salvatore.write_news("attacco al cairo")        # ...
salvatore.write_news("processori 4 nanometri")  # ...

salvatore.add_news(agg, salvatore.documents[0], 'high')   # send this news!

# print("\n", salvatore.name, "has", salvatore.subs, "as subscriber")
# print("aggregator library:  ", agg.subscriptions)
# print(giacomo.name, " -> ", giacomo.subscriptions)
# print(marco.name, " -> ", marco.subscriptions)
# print(andrea.name, " -> ", andrea.subscriptions)
# print("\n\nin giacomo mailbox there are: ", giacomo.news)
# print("in marco mailbox there are: ", marco.news)

print("giacomo --> ", giacomo.subscriptions)         # giacomo's followings









