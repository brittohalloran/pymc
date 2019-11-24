A python library for running Monte-Carlo analyses

## Usage

```python
import monte_carlo as mc

# Make some input random variables
a = mc.Norm(interval=(5, 10)) # 90% confidence interval
b = mc.Norm(interval=(5, 10), proportion = 0.95) # 95% CI
c = mc.Norm(mean=0, sd=1)
d = mc.Binom(p=0.75) # 75% chance of 1, 25% chance of 0
print(c.s) # single sample

# Make a function that returns a single sample
stackup = lambda: a.s + b.s - c.s + 10 * d.s

sim = mc.Simulation(f=stackup)
sim.run()

```

![example_plot](plot.png)

## Retirement simulation
```python
import monte_carlo as mc

sim = mc.RetirementSimulation(
    start_date="2019-11-01",
    start_balance=1000,
    monthly_savings=500,
    withdrawls={
        "2030-01-01": 80000  # All dates must be first of month
    },
    retirement_date="2051-01-01",
)
sim.run()

```