Control Theory

- - - -

# PID (Proportional-Integral-Derivative) Control Algorithm

The PID control algorithm is defined as:

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

[What is a PID Controller? | DigiKey - Shawn Hymel - YouTube](https://youtu.be/tFVAaUcOm4I?si=Z2U_stCSXwVZDC8v)
