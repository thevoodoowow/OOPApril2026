from abc import abstractmethod


class Work:
    @abstractmethod
    def work(self):
        pass


class Eat:
    @abstractmethod
    def eat(self):
        pass


class HumanWorker(Work, Eat):
    def work(self):
        print("Человек работает")

    def eat(self):
        print("Человек обедает")


class RobotWorker(Work):
    def work(self):
        print("Робот работает")


def manage_work(workers: list[Work]):
    for w in workers:
        w.work()


def manage_lunch(beings: list[Eat]):
    for b in beings:
        b.eat()


workers = [HumanWorker(), RobotWorker()]
manage_work(workers)

eaters = [HumanWorker()]
manage_lunch(eaters)
