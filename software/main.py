import e32cb as cb
from time import sleep
import _thread as th

def startSequention():

	pump.on()

	sleep(1)

	peltiers12V[0].on()
	peltiers12V[1].on()

	sleep(1)

	peltiers3V[0].on()
	peltiers3V[1].on()

	print("Start sequention done")

	return


peltiers3V = [
	cb.q1,
	cb.q2
]

peltiers12V = [
	cb.q3,
	cb.q4
]

pump = cb.q7



th.start_new_thread(startSequention, ())

while True:
	cb.led(1)

	sleep(0.1)

	cb.led(0)

	sleep(0.1)


