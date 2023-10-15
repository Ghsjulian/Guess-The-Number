import threading
import random 
import color
import os 

os.system("clear")

target_number = str(input(color.BOLD+color.YELLOW+color.BOLD+"\n   [+] Enter Any 8 Digits Number :  "+color.LIGHT_CYAN))






def check_num(num):
    num_len = len(num)
    if len(str(10)) == num_len:
        return random.randint(10,99)
    elif len(str(100)) == num_len:
        return random.randint(100,999)
    elif len(str(1000)) == num_len:
        return random.randint(1000,9999)
    elif len(str(10000)) == num_len:
        return random.randint(10000,99999)
    elif len(str(100000)) >= num_len:
        return random.randint(100000,999999)
    elif len(str(1000000)) >= num_len:
        return random.randint(1000000,9999999)
    elif len(str(10000000)) >= num_len:
        return random.randint(10000000,99999999)
    else:
        return 0
        



def match():
    result = ""
    tm =0
    while True:
        random_number = check_num(target_number)
        if random_number == int(target_number):
            result = f"{target_number}"
            break
        #print(str(random_number)+"  "+str(random_number)+"  "+str(random_number)+"  "+str(random_number)+"  "+str(random_number))
        print(color.BOLD+random.choice(color.color_list)+str(random_number)+"   "+color.BOLD+random.choice(color.color_list)+str(random_number)+"   "+color.BOLD+random.choice(color.color_list)+str(random_number)+"     "+color.BOLD+random.choice(color.color_list)+str(random_number))
        tm+=1
    print(color.BOLD+color.BOLD+color.GREEN+"\nTarget Number Is  : "+color.RED+color.BOLD+ target_number)
    print(color.BOLD+color.BOLD+color.CYAN+"\nTrying Time  : "+color.YELLOW+color.BOLD+ str(tm))


threads = []
num_threads = 1
for _ in range(num_threads):
    thread = threading.Thread(target=match)
    threads.append(thread)
    thread.start()
#Wait for all threads to finish
for thread in threads:
    thread.join()




# Create two threads
#thread1 = threading.Thread(target=match)
#thread2 = threading.Thread(target=match)
# Start the threads
#thread1.start()
#thread2.start()
# Wait for both threads to finish
#thread1.join()
#thread2.join()
#print("Both threads have finished")

