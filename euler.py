from euler.euler_problems import EulerProblems
from performance.performance import Performance

if __name__ == "__main__":
    perf = Performance()
    problem = EulerProblems.find_or_throw('0001')()
    perf.start()
    print(problem.solve())
    perf.end()
    pass
