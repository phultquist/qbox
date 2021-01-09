# Pseudocode File

```python
#By the way, all Constants are to be determined.

SpringCoefficient = -1
#Driver Spring Coefficient

Damping = -5
#Driver Damping Coefficient

ElectromagneticStrength = 1
#Input Signal Electromagnetic force strength / signal gain

#CompensationP = 1
#CompensationI = 1
#CompensationD = 1
#PID parameters for Corrective pid loop

while True:
#There is probably a better way to do this I just wanted to make it clear that this is a forever repeating loop.

  InputSignal = LowPass(frequency: 200hz, slope: 2nd order or 12db/octave) of (Imported Audio Signal Stream)
#Importing current audio data and applying a lowpass filter to the signal

  return (ElectromagneticStrength * InputSignal - (Damping * Integral(InputSignal) + SpringCoefficient * Integral^2(InputSignal))
#Returns the input signal minus the driver forces, which theoretically creates a total net force on the driver that is proportional to InputSignal
  
```
Addison, here are some things I need you to clarify:
1. What is LowPass? And what is the slope saying and the of makes no sense. I assume the function LowPass acts on something, in which you would do LowPass(of=ImportedAudioSignalStream, frequency="200hz", slope="something"): I assume there is a DSP library that would include such a function, it's basically the most basic kind of filter possible. Slope is the rate at which the high frequencies decrease in relation to frequency. here's a visual of what that means: https://i218.photobucket.com/albums/cc178/daishi00/graphs_charts/bw_compare.jpg
