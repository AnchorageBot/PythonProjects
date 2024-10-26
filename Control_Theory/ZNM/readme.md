The Ziegler-Nichols Method is a heuristic technique for tuning PID controllers, developed to give a good initial setting for the proportional (P), integral (I), and derivative (D) gains. There are two main approaches in the Ziegler-Nichols method: the Open-Loop (or Step Response) method and the Closed-Loop (or Ultimate Gain) method.

- - - -

System (Model) Type:

* The first-order system script works on a first-order system (typically simpler, fewer oscillations unless gains are very specific).
* The second-order system script works on a second-order system (mass-spring-damper), which inherently has the potential for oscillations due to its physical properties.
