Tutor:
* Anthropic's AI Claude

- - - -

The differences between likelihood and probability.

While these terms are sometimes used interchangeably in casual conversation, they have distinct meanings in statistics and mathematics:

Probability describes the chance of a future event occurring or the chance of a hypothesis being true, given fixed parameters. It answers questions like "Given these parameters, what's the chance of observing this data?" Probability must sum to 1 across all possible outcomes.

Likelihood measures how well a statistical model with different parameters explains already observed data. It answers questions like "Given this observed data, how well do different parameter values explain what we've seen?" Likelihood doesn't need to sum to 1 and can be any non-negative number.

A concrete example might help:
Imagine flipping a coin. The probability asks "If the coin has a 70% chance of heads, what's the probability of getting 3 heads in 5 flips?" Likelihood asks "After observing 3 heads in 5 flips, what's the likelihood that the coin's true probability of heads is 70% versus 50% versus 30%?"

The key differences are:
- Probability goes from parameters to data (forward)
- Likelihood goes from data to parameters (backward)
- Probability has to sum to 1 across outcomes
- Likelihood can take any non-negative value
