# Lectures on Component Reliability Analysis

In 2025 there were 2 lectures on component reliability analysis, which are summarized below.

## Lecture 1: Introduction to Component Reliability Analysis

The main topics covered in this lecture were:
- Refresher on MCS and illustrating that it is one of many ways to perform a component reliability analysis.
- Noting that the key ingredients of MCS include a function
- Review of the week 1 workshop assignment, and seeing how it can be reformulated as a limit-state function
- Review of the 2 river discharge example and exploring the probability of various combinations of events (e.g., review and/or and introduce the more general "region of interest")
- Emphasize the importance of visualizing the probability _density_ in a 2 variable case (e.g., contours of density and regions of interest)
- Introduce the linearized function of random variables and connect it to similar concepts from MUDE (uncertainty propagation)
- Explain that MCS is nice because it is easy to implement; other methods are challenging to implement but can be much more efficient
- Define the 5 key ingredients of a component reliability analysis
- Define the FORM algorithm

## Lecture 2: 

- Review the 5 key ingredients of a component reliability analysis
- Review how to calculate probabilities with univariate distributions, including the standard normal distribution
- Explain that the standard normal distribution can be calculated easily as a linear transformation of any random variable with the normal distribution
- Illustrate the standard normal distribution with a 2D example, and how to visualize the probability density function
- Illustrate the linearized limit state function and how it can be used to calculate the probability of failure
- Define the multivariate standard normal distribution and illustrate rotational invariance; density is only a function of the distance from the origin
- Confirm that simple linear algebra relationships can be used to evaluate the probability of failure, once the algorithm finds the design point.
- Define and explain the three key parts of a FORM solution: the design point, $x_i$, the reliability index, $\beta$, and the importance factors, $\alpha_i$.