import tracemalloc
import time
from pathlib import Path
from collections import Counter
from findex.corpus import iter_documents
from findex.tokenize import tokenize


def peak(fn, *args):
    tracemalloc.start()
    start_time = time.time()
    result = fn(*args)
    _, peak_mem = tracemalloc.get_traced_memory()
    tracemalloc.stop()
    return result, peak_mem, time.time() - start_time


def lazy_pipeline(data_dir: Path):
    doc_count = 0
    sink = Counter()
    for doc in iter_documents(data_dir):
        doc_count += 1
        for token in tokenize(doc):
            sink[token] += 1

    return doc_count, sink


def greedy_pipeline(data_dir: Path):
    docs = list(iter_documents(data_dir))
    all_tokens = []
    for doc in docs:
        all_tokens.extend(list(tokenize(doc)))
    return len(docs), Counter(all_tokens)


if __name__ == "__main__":
    path = Path("data")

    (docs, counter), peak_lazy, time_lazy = peak(lazy_pipeline, path)
    print("=== Лінива версія ===")
    print(f"Документів: {docs}, Токенів: {counter.total()}, Словник: {len(counter)}")
    print(f"Топ-5: {counter.most_common(5)}")
    print(f"Пікова пам'ять: {peak_lazy / 1024 / 1024:.2f} MB, Час: {time_lazy:.2f}s\n")

    _, peak_greedy, time_greedy = peak(greedy_pipeline, path)
    print("=== Жадібна версія ===")
    print(f"Пікова пам'ять: {peak_greedy / 1024 / 1024:.2f} MB, Час: {time_greedy:.2f}s")