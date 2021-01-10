from scipy.io import wavfile
import matplotlib.pyplot as plt

electromagnetic_strength = 1
damping = -5*1000
spring_coefficient = -100

samplerate, data = wavfile.read('./test.wav')
print("Total Data Length:", len(data), ", Sample Rate:",samplerate)

def integral(current, last):
    new = last + current
    return new

# data = [0,1,0,1,0,2,1]

beg = 50000
end = 50500
# beg = 0
# end = len(data)

time=beg
last_input_integral_1 = 0
last_input_integral_2 = 0

values = []
while time<end:
    # electromagnetic_force = [e * electromagnetic_strength for e in data[0:time]] # ElectromagneticStrength * InputSignal
    electromagnetic_force = electromagnetic_strength * data[time]
    
    input_integral = integral(data[time], last_input_integral_1) # Integral(InputSignal)
    input_integral_2 = integral(input_integral, last_input_integral_2)  # Integral(Integral(InputSignal))

    damped_signal = damping * input_integral # Damping * Integral(InputSignal)
    springed_signal = spring_coefficient * input_integral_2 # SpringCoefficient * Integral(Integral(InputSignal))

    last_input_integral_1 = input_integral
    last_input_integral_2 = input_integral_2

    output = electromagnetic_force - (damped_signal + springed_signal)
    print(data[time], output)
    values.append(output)

    time += 1

# plt.plot(values)
# plt.show()

fig, (ax1, ax2) = plt.subplots(2)
fig.suptitle('Vertically stacked subplots')
ax1.plot(data)
ax2.plot(values)
plt.show()

quit()
# return (ElectromagneticStrength * InputSignal - (Damping * Integral(InputSignal) + SpringCoefficient * Integral(Integral(InputSignal)))