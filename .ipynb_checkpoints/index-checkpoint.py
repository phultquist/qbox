from scipy.io import wavfile
from scipy import signal
import matplotlib.pyplot as plt
import numpy as np

electromagnetic_strength = 10000
damping = -100*10
spring_coefficient = -0.01

samplerate, data = wavfile.read('./100hz.wav')
print("Total Data Length:", len(data), ", Sample Rate:",samplerate)

def integral(current, last):
    new = last + current
    return new

# data = [0,1,0,1,0,2,1]

max_original = np.amax(np.absolute(data))

data = [e * 0.001 for e in data]

# beg = 50000
# end = 60000
beg = 0
end = len(data)

time=beg
last_input_integral_1 = 0
last_input_integral_2 = 0

values = []
while time<end:
    electromagnetic_force = electromagnetic_strength * data[time] # ElectromagneticStrength * InputSignal
    
    input_integral = integral(data[time], last_input_integral_1) # Integral(InputSignal)
    input_integral_2 = integral(input_integral, last_input_integral_2)  # Integral(Integral(InputSignal))

    damped_signal = damping * input_integral # Damping * Integral(InputSignal)
    springed_signal = spring_coefficient * input_integral_2 # SpringCoefficient * Integral(Integral(InputSignal))

    last_input_integral_1 = input_integral
    last_input_integral_2 = input_integral_2

    output = electromagnetic_force - (damped_signal + springed_signal)
    output = -1*(damped_signal + springed_signal)

    values.append(output)

    time += 1

#################
### ADJUSTING ###
#################

sos = signal.butter(10, 20, "highpass", fs=samplerate, output="sos")
filtered = signal.sosfilt(sos, values)

buttered_original = signal.sosfilt(sos, data)

buttered_adjusted = filtered
unbuttered_adjusted = np.array(values)

to_stabilize = buttered_adjusted

max_adjusted = np.amax(np.absolute(to_stabilize))
stabilized = (max_original / max_adjusted) * 0.99 * to_stabilize / 1000

buttered_adjusted = stabilized

wavfile.write("output.wav", samplerate, stabilized)

################
### PLOTTING ###
################

fig, (ax1, ax2, ax3, ax4) = plt.subplots(4, sharex=True)
fig.suptitle('Original and Adjusted Waves')

ax1.plot(data[beg:end])
ax1.set_title("Original")

ax2.plot(unbuttered_adjusted)
ax2.set_title("Unbuttered Adjusted")

ax3.plot(buttered_adjusted)
ax3.set_title("Buttered Adjusted (Output)")

ax4.plot(buttered_original)
ax4.set_title("Buttered Original")

plt.tight_layout()
plt.show()

# return (ElectromagneticStrength * InputSignal - (Damping * Integral(InputSignal) + SpringCoefficient * Integral(Integral(InputSignal)))