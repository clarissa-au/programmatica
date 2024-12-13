import concurrent.futures
from multiprocessing.dummy import Pool as ThreadPool
import itertools
data = """HIDDEN"""

data = data.split("\n")
data = [i.split(":") for i in data]
data = [[i[0], i[1].split(" ")[1:]] for i in data]
data = [[int(i[0]), [int(j) for j in i[1]]] for i in data]


def ev(value, method):
    accu = value[0]
    for i in range(len(value)-1):
        num = value[i+1]
        m = method[i]
        if (m == "+"):
            accu = accu + num
        elif (m == "*"):
            accu = accu * num
        elif (m == "|"):
            accu = int(str(accu) + str(num))
    return accu


def job_1(inp):
    target, values = inp
    for method in itertools.product("+*", repeat=len(values)-1):
        if ev(values, method) == target:
            return target
    return 0


def job_2(inp):
    target, values = inp
    for method in itertools.product("+*|", repeat=len(values)-1):
        if ev(values, method) == target:
            return target
    return 0

# trying out different kinds of multiprocessing and comparing it to the default

pool = ThreadPool(16)
results = pool.map(job_1, data, chunksize=len(data)//16)
pool.close()
pool.join()

print(f"Part 1 answer: {sum(results)}")

pool = ThreadPool(16)
results = pool.map(job_2, data, chunksize=len(data)//16)
pool.close()
pool.join()

print(f"Part 2 answer: {sum(results)}")

#---

j1 = 0
j2 = 0
for i in range(len(data)):
    j1 += job_1(data[i])
    j2 += job_2(data[i])
print(j1, j2)

#---

def script():

    with concurrent.futures.ThreadPoolExecutor(max_workers=16) as executor:
        futures = {executor.submit(job_1, dat): dat for dat in data}
        sums = 0
        for future in concurrent.futures.as_completed(futures):
            result = future.result()
            sums += result
        print(f"Part 1 answer: {sums}")

    with concurrent.futures.ThreadPoolExecutor(max_workers=16) as executor:
        futures = {executor.submit(job_2, dat): dat for dat in data}
        sums = 0
        for future in concurrent.futures.as_completed(futures):
            result = future.result()
            sums += result
        print(f"Part 2 answer: {sums}")


if __name__ == "__main__":
    script()
