Control Theory

- - - -

# PID (Proportional-Integral-Derivative) Control Algorithm

The PID control algorithm is informally defined as:

 * Output ~ Error now + Errors past + Error future

The PID control algorithm is formally defined as:

```
u(t) = Kp * e(t) + Ki * ∫e(τ)dτ + Kd * de(t)/dt
```

## Glossary of Terms and Symbols

| Term/Symbol | Description |
|-------------|-------------|
| PID | Proportional-Integral-Derivative |
| `u(t)` | Control signal at time t |
| `e(t)` | Error signal at time t |
| `Kp` | Proportional gain |
| `Ki` | Integral gain |
| `Kd` | Derivative gain |
| Setpoint | Desired value of the process variable |
| Process Variable | The variable being controlled in the process |
| Proportional Term | Responds to the current error (`Kp * e(t)`) |
| Integral Term | Responds to the accumulated error over time (`Ki * ∫e(τ)dτ`) |
| Derivative Term | Responds to the rate of change of error (`Kd * de(t)/dt`) |
| Overshoot | When the process variable exceeds the setpoint |
| Steady-state Error | Constant error between setpoint and process variable after transient response |
| Rise Time | Time taken for the output to reach a specified percentage of its final value |
| Settling Time | Time taken for the system to reach and stay within a specified range of its final value |

- - - -
Lectures

* [What is a PID Controller? | DigiKey - Shawn Hymel - YouTube](https://youtu.be/tFVAaUcOm4I?si=Z2U_stCSXwVZDC8v)

* [PID Controller Basics for Beginners - RealPars - YouTube](https://youtube.com/playlist?list=PLln3BHg93SQ_Ejn6godXbxromegXSMYOl&si=V3rPZRMiMtk2jlkb)

* [EEVacademy #6 - PID Controllers Explained - EEVBlog - YouTube](https://youtu.be/VVOi2dbtxC0?si=TrsaRtYvVDxNWW4A)

* [PID Math Demystified - Scott Hayes - YouTube](https://youtu.be/JEpWlTl95Tw?si=-HeIVarZ4614TvjI)

* [Process Control - ABB Process Automation - Youtube](https://youtube.com/playlist?list=PLOgEb39vsYlu2WFdWSe5kvOtmJyC-ew2e&si=sVZRDJyVjkxGjApu)
