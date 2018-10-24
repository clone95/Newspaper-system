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

    def add_news(self, aggregator, uploading, permissions='low'):
            aggregator.update(self, uploading, permissions)

    def write_news(self, document):
        self.documents[self.counter] = document
        self.counter += 1

    def subscribe_to_aggr(self, aggregators):
        for aggr in aggregators:
            aggr.insert_publisher(self)

    def add_sub(self, new_sub):
        self.subs.add(new_sub)


class User:

    def __init__(self, name='default_user'):
        self.name = name
        self.permissions = 'low'
        self.subscriptions = []
        self.news = dict()
        self.counter = 0

    def subscribe(self, publisher, aggregator, permissions='low'):
        self.subscriptions.append(publisher.name)
        aggregator.subscribe(self, permissions, publisher)

    def receive(self, publisher, document):
        self.news[publisher.name] = document

    def subscribe_all(self, aggregator, permissions='low'):
        aggregator.subscribe_me_all(self, permissions)

    def print_news(self, publisher=None):
        if publisher is None:
            for element in self.subscriptions:
                print(self.news[element])
        else:
            print(self.news[publisher])

    def delete_subcription(self, publisher):
        self.subscriptions.remove(publisher)


class Aggregator:

    def __init__(self, name='default_aggregator'):
        self.name = name
        self.publishers = set()
        self.subscriptions = dict(dict())
        self.counter = 0

    def subscribe(self, caller, permissions='low', publisher=Publisher()):      # publisher wants to enlist itself
        if isinstance(caller, Publisher):
            self.publishers.add(caller)

        else:
            self.subscriptions[publisher.name + "_" + str(self.counter)] = {caller: permissions}     # user subscribing to a publisher
            self.notify_to_pub(caller, publisher)
            self.counter += 1
            # print(caller.name, "subscribing", publisher.name)

    def subscribe_me_all(self, caller, permissions):
        for paper in self.publishers:
            caller.subscribe(paper, self, permissions)

    def remove(self, caller):
        if isinstance(caller, Publisher):
            self.publishers.remove(caller)
        else:
            self.subscriptions.__delitem__(caller)

    @staticmethod
    def notify_to_pub(caller, publisher):
        publisher.add_sub(caller.name)

    def update(self, publisher, document, permissions):
        to_reach = self.get_users_for_publisher(publisher)

        for user in range(0, len(to_reach)):
            if list(to_reach[user].values())[0] == permissions:
                list(to_reach[user].keys())[0].receive(publisher, document)

    def get_users_for_publisher(self, publisher):
        users = []
        for sub in self.subscriptions:
            if sub[:-2] == publisher.name:
                users.append(self.subscriptions[sub])
        return users

giacomo = User("giacomo")
marco = User("marco")
andrea = User("andrea")
salvatore = Publisher("salvatore aranzulla")
toms = Publisher("Tom's Hardware")
agg = Aggregator()

agg.subscribe(salvatore)        # subscribing publisher
agg.subscribe(toms)             # subscribing publisher

#giacomo.subscribe(salvatore, agg, 'mid')        # subscribe giacomo -> salvatore
#giacomo.subscribe(toms, agg, 'mid')             # subscribe giacomo -> toms
marco.subscribe(salvatore, agg, 'high')          # subscribe marco -> toms
marco.subscribe(toms, agg, 'high')               # subscribe marco -> toms
giacomo.subscribe_all(agg, 'mid')                       # subscribe giacomo --> to all

salvatore.write_news("buon giorno")
salvatore.write_news("attacco al cairo")
salvatore.write_news("processori 4 nanometri")

salvatore.add_news(agg, salvatore.documents[0], 'high')


# print("\n", salvatore.name, "has", salvatore.subs, "as subscriber")
# print("aggregator library:  ", agg.subscriptions)
# print(giacomo.name, " -> ", giacomo.subscriptions)
# print(marco.name, " -> ", marco.subscriptions)
# print(andrea.name, " -> ", andrea.subscriptions)

to_notify = agg.get_users_for_publisher(salvatore)
# print("\n\nin giacomo mailbox there are: ", giacomo.news)
# print("in marco mailbox there are: ", marco.news)
print("giacomo --> ", giacomo.subscriptions)
print(agg.subscriptions)



class a:
    def __init__(self):
        self.nome = "a"

    def printa(self):
        print("metodo printa")







