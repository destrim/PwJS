import threading
import time


class Philosopher(threading.Thread):
    hungry = True

    def __init__(self, index, leftFork, rightFork, isDeadlock=False):
        threading.Thread.__init__(self)
        self.index = index
        self.leftFork = leftFork
        self.rightFork = rightFork
        self.isDeadlock = isDeadlock

    def run(self):
        while self.hungry:
            time.sleep(2)
            print('%s is hungry' % self.index)
            if self.isDeadlock:
                self.deadlock()
            else:
                self.no_deadlock()

    def deadlock(self):
        fork1, fork2 = self.rightFork, self.leftFork
        while self.hungry:
            has1 = fork1.acquire()  # philosopher picks right fork
            has2 = fork2.acquire()  # then he try to pick left, holding right all the time
            if has1 and has2:  # if he has both, starts eating
                break
        else:
            return
        self.eat()
        fork2.release()
        fork1.release()

    def no_deadlock(self):
        fork1, fork2 = self.rightFork, self.leftFork
        while self.hungry:
            fork1.acquire()  # philosopher picks right fork
            locked = fork2.acquire(False)  # trying to pick left fork
            if locked:  # if left fork free, he starts eating
                break
            fork1.release()  # if not, he puts the right fork back
            print('%s will try other fork' % self.index)
            fork1, fork2 = fork2, fork1  # and next time try to pick other fork first
        else:
            return
        self.eat()
        fork2.release()
        fork1.release()

    def eat(self):
        print('%s starts eating' % self.index)
        time.sleep(2)
        print('%s finishes eating and thinking' % self.index)


def main():

    forks = [threading.Semaphore() for n in range(5)]

    # no deadlock
    philosophers = [Philosopher(i, forks[i % 5], forks[(i+1) % 5]) for i in range(5)]

    Philosopher.hungry = True
    for x in philosophers:
        x.start()
    time.sleep(10)
    Philosopher.hungry = False
    print('---Done---')

    # deadlock
    philosophers = [Philosopher(i, forks[i % 5], forks[(i+1) % 5], True) for i in range(5)]

    Philosopher.hungry = True
    for x in philosophers:
        x.start()
    time.sleep(10)
    Philosopher.hungry = False
    print('---Done---')


if __name__ == '__main__':
    main()
