""" 
You are given two ropes, each of which takes exactly T minutes to burn completely.
However, these ropes do not burn at a uniform rate—some parts may burn faster or slower than others.
Using only these two ropes and a source of fire, your task is to measure a specific duration of time accurately.
"""
def measure_time(T):
    total_time=0
    print(f"Step1:Light Rope1 from both ends and Rope 2 from one end.")
    total_time += T//2
    print(f"After {total_time} minutes → Rope 1 is fully burned.")
    print(f"Step 2: Now, light Rope 2 from the other end.")
    total_time += T//4
    print(f"After {total_time} minutes → Rope 2 is fully burned.")
    print(f"Exactly {total_time} minutes measured using two ropes")
T=int(input("Enter the total burning time of onr rope(in minutes):"))
measure_time(T)
