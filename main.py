import psutil

processes = psutil.process_iter()
for p in processes:
    print(p)