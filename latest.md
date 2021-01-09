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







  #TotalSignal = ElectromagneticStrength * TotalSignal + Damping * Integral(Total Signal) + SpringCoefficient * Integral^2(Total Signal) +   CompensationP * (InputSignal - TotalSignal) + CompensationI * Integral(InputSignal - TotalSignal) + CompensationI * Derivative(InputSignal - TotalSignal)
#TotalSignal represents the total force on the driver at all times, which is ideally equal to InputSignal. The terms with ElectromagneticStrength, Damping, and SpringCoefficient represent the forces that create the resonant properties of the driver. The "Compensation" terms are the agressive, corrective PID loop that attempts to force TotalSignal to equal InputSignal. I assumed that you would know the most efficient way to calculate derivatives and integrals of a data stream, so I didn't try to approximate them.
  
  #Return (Input Signal + CompensationP * (InputSignal - TotalSignal) + CompensationI * Integral(InputSignal - TotalSignal) + CompensationI * Derivative(InputSignal - TotalSignal))
#Finally, the InputSignal plus the corrective factors are returned.
```
Addison, here are some things I need you to clarify:
1. What is LowPass? And what is the slope saying and the of makes no sense. I assume the function LowPass acts on something, in which you would do LowPass(of=ImportedAudioSignalStream, frequency="200hz", slope="something")
2. What is all the things at the bottom?
3. Also just so you know almost every language, including Python, uses lowerCamelCase not UpperCamelCase

Pretty good pseudocode though.
