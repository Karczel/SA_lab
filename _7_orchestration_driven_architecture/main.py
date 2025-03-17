from user import User
from orchestrator import Orchestrator

if __name__ == '__main__':
    user = User(1)
    user.deposit(100000)
    orchestrator = Orchestrator()
    orchestrator.run(user)