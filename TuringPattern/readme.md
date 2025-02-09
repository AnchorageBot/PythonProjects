Articles
* [How the Tiger Really Got His Stripes - Rivka Galchen - The New Yorker](https://www.newyorker.com/science/elements/how-the-tiger-really-got-his-stripes)

Models
* [Diffusion equation - Wiki](https://en.wikipedia.org/wiki/Diffusion_equation)
  
* [Swift–Hohenberg equation - Wiki](https://en.wikipedia.org/wiki/Swift–Hohenberg_equation)

Papers

Videos
* [Turing's Cake (and other wrinkly math) - Physics for the Birds](https://youtu.be/icQ_BTtNGEo?si=fSh-SmWKEw19m7je)

- - - -

Tutor: Google Gemini 2.0, Experimental Advanced 

**1. Diffusion Equation (Heat Equation)**

The diffusion equation, also known as the heat equation, describes how a quantity (like temperature, concentration, etc.) spreads out over time due to diffusion. In its most common form, it's a partial differential equation (PDE):

```
∂u/∂t = α ∇²u
```

Where:

*   **u(x, t):**  The quantity of interest (e.g., temperature) at position `x` and time `t`.  `x` can be in one, two, or three dimensions.
*   **∂u/∂t:** The partial derivative of `u` with respect to time. This represents the rate of change of `u` at a fixed point.
*   **α (alpha):** The diffusion coefficient (or thermal diffusivity, if `u` is temperature). This is a positive constant that determines how quickly the diffusion occurs.  Larger α means faster diffusion.
*   **∇² (nabla squared):** The Laplacian operator.  This represents the "curvature" or "second spatial derivative" of `u`.  Its form depends on the number of dimensions:
    *   **1D:** ∇²u = ∂²u/∂x²
    *   **2D:** ∇²u = ∂²u/∂x² + ∂²u/∂y²
    *   **3D:** ∇²u = ∂²u/∂x² + ∂²u/∂y² + ∂²u/∂z²

**Alternative Notation (using subscripts):**

Sometimes, partial derivatives are denoted using subscripts.  The same equation can be written as:

```
u_t = α (u_xx + u_yy + u_zz)  // 3D
```

or

```
u_t = α u_xx  // 1D
```

**Boundary and Initial Conditions:**

To get a unique solution to the diffusion equation, you need to specify *boundary conditions* (what happens at the edges of the domain) and an *initial condition* (the value of `u` at time t=0). For example:

*   **Initial Condition:** u(x, 0) = f(x)  (The initial distribution of `u`)
*   **Boundary Conditions (Example - Dirichlet):** u(0, t) = g₁(t),  u(L, t) = g₂(t) (The values of `u` are fixed at the boundaries x=0 and x=L)

**2. Swift-Hohenberg Equation**

The Swift-Hohenberg equation is a PDE that models pattern formation in systems driven away from equilibrium.  It's often used to study phenomena like Rayleigh-Bénard convection (patterns in a heated fluid).

```
∂u/∂t = r*u - (∇² + k_c² )²u + N(u)
```

Where:

*   **u(x, t):** The field variable (e.g., temperature deviation) at position `x` and time `t`.
*   **∂u/∂t:** The partial derivative of `u` with respect to time.
*   **r:** A control parameter (often related to the Rayleigh number in convection). This determines how far the system is from equilibrium.
*   **k_c:** The critical wavenumber. This determines the characteristic length scale of the patterns that form.
*   **∇²:** The Laplacian operator (as described above).
*   **(∇² + k_c² )²:**  This is the biharmonic operator (∇⁴) with an added term. It's applied twice:  (∇² + k_c²)((∇² + k_c²)u). It's a fourth-order spatial derivative.
* **N(u):** A nonlinear term.  This is what makes the Swift-Hohenberg equation more complex than the simple diffusion equation. Common choices for N(u) include:
    *   **N(u) = -u³:**  The most common form, leading to a cubic nonlinearity.
    *   **N(u) = εu² - u³:**  Includes a quadratic term, which can break the symmetry of the solutions.

**Alternative Notation (using subscripts and expanding the biharmonic operator):**

```
u_t = r*u - (∇⁴u + 2*k_c²*∇²u + k_c⁴*u) + N(u)

// Or, expanding the Laplacian in 2D:
u_t = r*u - (u_xxxx + 2*u_xxyy + u_yyyy + 2*k_c²*(u_xx + u_yy) + k_c⁴*u) + N(u)
```

**Boundary and Initial Conditions:**

Similar to the diffusion equation, you need boundary and initial conditions. Common boundary conditions for Swift-Hohenberg are periodic, Neumann (zero derivative), or Dirichlet (fixed value).

**Simplified form with N(u) = -u³**

Using the cubic non-linearity, it is common practice to show the following simplification of the Swift-Hohenberg Equation:

```
∂u/∂t = (r - (1 + ∇²)²)u - u³
```

