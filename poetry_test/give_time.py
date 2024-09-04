import pendulum
import arrow

time_pn=pendulum.now()
time_ar=arrow.now()

print(f"{time_pn} (pendulum library)")

print(f"{time_ar} (arrow library)")
