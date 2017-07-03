import time
from hyperdash.sdk import monitor


@monitor(job_name="cats v. dogs")
def main():
    # while True:
    print("Doing the machine learning...")
    time.sleep(2)
    print("accuracy: 0%")
    time.sleep(2)
    print("accuracy: 25%")
    time.sleep(2)
    print("accuracy: 50%")
    time.sleep(2)
    print("accuracy: 75%")
    time.sleep(2)
    print("accuracy: 100%")

main()