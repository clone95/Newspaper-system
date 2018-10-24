class User:

    subscriptions = set()
    news = dict()

    def __init__(self, name='default_user'):
        self.name = name
        self.permissions = 'low'

    def subscribe(self, publisher, aggregator, permissions='low'):
        self.subscriptions.add(publisher.name)
        aggregator.subscribe(self, permissions, publisher)

    def subscribe_all(self, aggregator):
        aggregator.subscribe_me_all(self)

    def print_news(self, publisher=None):
        if publisher is None:
            for element in self.subscriptions:
                print(self.news[element])
        else:
            print(self.news[publisher])

    def delete_subcription(self, publisher):
        self.subscriptions.remove(publisher)


class Publisher:

    documents = dict()
    published = set()
    subs = set()

    def __init__(self, name='default_publisher', aggregator='default_aggregator'):
        self.name = name
        self.aggregator = [aggregator]

    def add_news(self, aggregators, uploading):
        for aggr in aggregators:
            aggr.update(self, uploading, permissions='low')

    def subscribe_to_aggr(self, aggregators):
        for aggr in aggregators:
            aggr.insert_publisher(self)

    def add_sub(self, new_sub):
        self.subs.add(new_sub)


class Aggregator:

    publishers = set()
    subscriptions = dict(dict())

    def __init__(self, name='default_aggregator'):
        self.name = name

    def subscribe(self, caller, permissions='low', publisher=Publisher()):      # publisher wants to enlist itself
        if isinstance(caller, Publisher):
            self.publishers.add(caller)

        else:
            self.subscriptions[publisher.name] = {caller.name: permissions}     # user subscribing to a publisher
            self.notify_to_pub(caller, publisher)
            print(caller.name, "subcribing", publisher.name)

    def remove(self, caller):
        if isinstance(caller, Publisher):
            self.publishers.remove(caller)
        else:
            self.subscriptions.__delitem__(caller)

    @staticmethod
    def notify_to_pub(caller, publisher):
        publisher.add_sub(caller.name)

    def update(self, publisher, permissions):
        for user in (self.subscriptions):
            print(user)









giacomo = User("giacomo")
marco = User("marco")
andrea = User("andrea")
salvatore = Publisher("salvatore aranzulla")
toms = Publisher("Tom's Hardware")
agg = Aggregator()

agg.subscribe(salvatore)



giacomo.subscribe(salvatore, agg, 'mid')
#marco.subscribe(toms, agg, 'high')



print("\n", salvatore.name, "has", salvatore.subs, "as a subcriber")
print("aggregator library:  ", agg.subscriptions)
print(giacomo.name, " -> ", giacomo.subscriptions)
print(marco.name, " -> ", marco.subscriptions)
print(andrea.name, " -> ", andrea.subscriptions)





class a:
    def __init__(self):
        self.nome = "a"
    def printa(self):
        print("metodo printa")







