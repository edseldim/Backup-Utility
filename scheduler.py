import schedule
import subprocess
import time

def program():
    subprocess.Popen(['bash', "backup-utility.sh"], shell=True)

if __name__ == "__main__":
    schedule.every(10).seconds.do(program)
    while True:
        print("running programs...")
        schedule.run_pending()
        time.sleep(20) # every hour check