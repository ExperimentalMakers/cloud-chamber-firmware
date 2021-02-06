from machine import Pin, Signal, PWM, SoftI2C, UART


class Mosfet:
	def __init__(self, pin, pwm_base_freq, pwm_max):
		self.__pwm = PWM(pin, freq=pwm_base_freq, duty=pwm_max)
		self.off()

	def pwm(self, pwm):
		self.__pwm.duty(invert_pwm(pwm))

	def on(self):
		self.__pwm.duty(pwm_min)

	def off(self):
		self.__pwm.duty(pwm_max)


def invert_pwm(pwm):
	return pwm_min+(pwm_max-pwm)

def led(value):
	Pin(32, Pin.OUT).value(value)

def fan(value):
	PWM(Pin(23), freq=pwm_fan_freq, duty=value)



pwm_fan_freq  = 25000
pwm_base_freq = 1000
pwm_min = 0
pwm_max = 1023


i2c  = SoftI2C(scl=Pin(22), sda=Pin(21))
uart = UART(2, 9600)

q1 = Mosfet(Pin(33), pwm_base_freq, pwm_max)
q2 = Mosfet(Pin(25), pwm_base_freq, pwm_max)
q3 = Mosfet(Pin(27), pwm_base_freq, pwm_max)
q4 = Mosfet(Pin(14), pwm_base_freq, pwm_max)
q5 = Mosfet(Pin(13), pwm_base_freq, pwm_max)
q6 = Mosfet(Pin(4 ), pwm_base_freq, pwm_max)
q7 = Mosfet(Pin(18), pwm_base_freq, pwm_max)

q8 = Signal(Pin(19, Pin.OUT), invert=True)



