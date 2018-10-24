class User:

    subscriptions = set()
    news = dict()

    def __init__(self, name='default_user'):
        self.name = name
        self.permissions = 'low'

    def subscribe(self, publisher, aggregator, permissions='low'):
        self.subscriptions.add(publisher)
        #aggregator.subscribe(self, permissions, publisher)
        aggregator.printa()
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

    def add_news(self, aggregators):
        for aggr in aggregators:
            aggr.update(self)

    def subscribe_to_aggr(self, aggregators):
        for aggr in aggregators:
            aggr.insert_publisher(self)

    def add_sub(self, new_sub):
        self.subs.add(new_sub)


class List:
    def __init__(self, name='default_list'):
        self.name = name
        self.publisher_list = []

    def add(self, publisher):
        self.publisher_list.append(publisher)


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

    def remove(self, caller):
        if isinstance(caller, Publisher):
            self.publishers.remove(caller)
        else:
            self.subscriptions.__delitem__(caller)

    @staticmethod
    def notify_to_pub(caller, publisher):
        pass

    def printa(self):
        print("a")


   # def update(self, publisher):
 #       pass
#






omino = User()
omino_1 = User("giacomo")
omino_2 = User("marco")
salvatore = Publisher()
agg = Aggregator()
lista = List()
agg.subscribe(salvatore)

omino_1.subscribe(salvatore, agg, 'mid')

print(agg.subscriptions)

class a:
    def __init__(self):
        self.nome = "a"
    def printa(self):
        print("ciao")

e = a()
a.printa(a)




